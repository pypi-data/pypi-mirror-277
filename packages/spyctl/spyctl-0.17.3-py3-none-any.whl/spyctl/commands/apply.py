"""Handles the apply subcommand for the spyctl."""

import json
import sys
from typing import Dict, List

import click

import spyctl.config.configs as cfg
import spyctl.resources as _r
import spyctl.spyctl_lib as lib
from spyctl import cli
from spyctl.api.notifications import (
    get_notification_policy,
    put_notification_policy,
)
from spyctl.api.policies import (
    post_new_policy,
    put_policy_update,
    get_policies,
)
from spyctl.api.rulesets import post_new_ruleset, put_ruleset_update
from spyctl.api.saved_queries import (
    get_saved_queries,
    post_new_saved_query,
    put_saved_query_update,
)

# import spyctl.commands.merge as m

# ----------------------------------------------------------------- #
#                         Apply Subcommand                          #
# ----------------------------------------------------------------- #


@click.command("apply", cls=lib.CustomCommand, epilog=lib.SUB_EPILOG)
@click.help_option("-h", "--help", hidden=True, is_eager=True)
@click.option(
    "-f",
    "--filename",
    # help="Filename containing Spyderbat resource.",
    metavar="",
    type=click.File(),
    required=True,
)
def apply(filename):
    """Apply a configuration to a resource by file name."""
    handle_apply(filename)


# ----------------------------------------------------------------- #
#                          Apply Handlers                           #
# ----------------------------------------------------------------- #

APPLY_PRIORITY = {
    lib.RULESET_KIND: 100,
    lib.POL_KIND: 50,
}


def handle_apply(filename):
    """
    Apply new resources or update existing resources.

    Args:
        filename (str): The path to the resource file.

    Returns:
        None
    """
    resrc_data = lib.load_resource_file(filename)
    if lib.ITEMS_FIELD in resrc_data:
        for resrc in resrc_data[lib.ITEMS_FIELD]:
            # Sort resource items by priority
            resrc_data[lib.ITEMS_FIELD].sort(
                key=__apply_priority, reverse=True
            )
            handle_apply_data(resrc)
    else:
        handle_apply_data(resrc_data)


def handle_apply_data(resrc_data: Dict):
    kind = resrc_data.get(lib.KIND_FIELD)
    if kind == lib.POL_KIND:
        handle_apply_policy(resrc_data)
    elif kind == lib.NOTIFICATION_KIND:
        handle_apply_notification_config(resrc_data)
    elif kind == lib.TARGET_KIND:
        handle_apply_notification_target(resrc_data)
    elif kind == lib.RULESET_KIND:
        handle_apply_ruleset(resrc_data)
    elif kind == lib.SAVED_QUERY_KIND:
        handle_apply_saved_query(resrc_data)
    else:
        cli.err_exit(f"The 'apply' command is not supported for {kind}")


def handle_apply_policy(policy: Dict):
    """
    Apply a policy to the current context.

    Args:
        policy (Dict): The policy to be applied.

    Returns:
        None
    """
    ctx = cfg.get_current_context()
    pol_type = policy[lib.METADATA_FIELD][lib.METADATA_TYPE_FIELD]
    if pol_type == lib.POL_TYPE_TRACE:
        policy = __check_duplicate_sel_hashes(policy)
        if not policy:
            return
    sub_type = _r.policies.get_policy_subtype(pol_type)
    uid = policy[lib.METADATA_FIELD].get(lib.METADATA_UID_FIELD)
    if uid:
        resp = put_policy_update(*ctx.get_api_data(), policy)
        if resp.status_code == 200:
            cli.try_log(f"Successfully updated policy {uid}")
    else:
        resp = post_new_policy(*ctx.get_api_data(), policy)
        if resp and resp.text:
            uid = json.loads(resp.text).get("uid", "")
            cli.try_log(
                f"Successfully applied new {pol_type} {sub_type} policy with uid: {uid}"  # noqa
            )


def __check_duplicate_sel_hashes(policy: Dict):
    sel_hash = _r.suppression_policies.get_selector_hash(policy)
    ctx = cfg.get_current_context()
    matching_policies = get_policies(
        *ctx.get_api_data(),
        params={
            "selector_hash_equals": sel_hash,
            "type": lib.POL_TYPE_TRACE,
        },
    )
    if not matching_policies:
        return policy
    matching_pol = matching_policies[0]
    if cli.query_yes_no(
        "A policy matching this scope already exists. Would you like to merge"
        " this policy into the existing one?"
    ):
        pol, should_update = _r.suppression_policies.merge_allowed_flags(
            matching_pol, policy
        )
        if should_update:
            return pol
        cli.try_log(
            "No changes detected in the policy. Skipping update.",
            is_warning=True,
        )
    return None


def handle_apply_ruleset(ruleset: Dict):
    """
    Apply a ruleset to the current context.

    Args:
        ruleset (Dict): The ruleset to be applied.

    Returns:
        None
    """
    ctx = cfg.get_current_context()
    rs_type = ruleset[lib.METADATA_FIELD][lib.METADATA_TYPE_FIELD]
    uid = ruleset[lib.METADATA_FIELD].get(lib.METADATA_UID_FIELD)
    if uid:
        resp = put_ruleset_update(*ctx.get_api_data(), ruleset)
        if resp.status_code == 200:
            cli.try_log(f"Successfully updated ruleset {uid}")
    else:
        resp = post_new_ruleset(*ctx.get_api_data(), ruleset)
        if resp and resp.json():
            uid = resp.json().get("uid", "")
            cli.try_log(
                f"Successfully applied new {rs_type} ruleset with uid: {uid}"
            )


def handle_apply_notification_target(notif_target: Dict):
    """
    Apply a notification target to the current context.

    Args:
        notif_target (Dict): The notification target to be applied.

    Returns:
        None
    """
    ctx = cfg.get_current_context()
    target = _r.notification_targets.Target(target_resource=notif_target)
    notif_pol = get_notification_policy(*ctx.get_api_data())
    targets: Dict = notif_pol.get(lib.TARGETS_FIELD, {})
    old_tgt = None
    for tgt_name, tgt_data in targets.items():
        tgt_id = tgt_data.get(lib.DATA_FIELD, {}).get(lib.ID_FIELD)
        if not tgt_id:
            continue
        if tgt_id == target.id:
            old_tgt = {tgt_name: tgt_data}
            break
        if tgt_name == target.name:
            cli.err_exit("Target names must be unique!")
    if old_tgt:
        tgt_name = next(iter(old_tgt))
        targets.pop(tgt_name)
    target.set_last_update_time()
    new_tgt = target.as_target()
    targets.update(**new_tgt)
    notif_pol[lib.TARGETS_FIELD] = targets
    put_notification_policy(*ctx.get_api_data(), notif_pol)
    if old_tgt:
        cli.try_log(f"Successfully updated Notification Target '{target.id}'")
    else:
        cli.try_log(f"Successfully applied Notification Target '{target.id}'")


def handle_apply_notification_config(notif_config: Dict):
    """
    Apply a notification configuration to the current context.

    Args:
        notif_config (Dict): The notification configuration to be applied.

    Returns:
        None
    """
    ctx = cfg.get_current_context()
    config = _r.notification_configs.NotificationConfig(
        config_resource=notif_config
    )
    notif_pol = get_notification_policy(*ctx.get_api_data())
    routes: List[Dict] = notif_pol.get(lib.ROUTES_FIELD, [])
    old_route_index = None
    for i, route in enumerate(routes):
        route_id = route.get(lib.DATA_FIELD, {}).get(lib.ID_FIELD)
        if not route_id:
            continue
        if route_id == config.id:
            old_route_index = i
    if old_route_index is not None:
        routes.pop(old_route_index)
    config.set_last_updated()
    new_route = config.route
    routes.append(new_route)
    notif_pol[lib.ROUTES_FIELD] = routes
    put_notification_policy(*ctx.get_api_data(), notif_pol)
    if old_route_index:
        cli.try_log(f"Successfully updated Notification Config '{config.id}'")
    else:
        cli.try_log(f"Successfully applied Notification Config '{config.id}'")


def handle_apply_saved_query(saved_query: Dict):
    """
    Apply a saved query to the current context.

    Args:
        saved_query (Dict): The saved query to be applied.

    Returns:
        None
    """
    ctx = cfg.get_current_context()
    spec = saved_query[lib.SPEC_FIELD]
    schema = spec.get(lib.QUERY_SCHEMA_FIELD)
    query = spec.get(lib.QUERY_FIELD)
    uid = saved_query[lib.METADATA_FIELD].get(lib.METADATA_UID_FIELD)
    if not uid:
        # Check if a saved query with the same schema and query already exists
        matching_queries, _total_pages = get_saved_queries(
            *ctx.get_api_data(),
            **{
                "schema_equals": schema,
                "query_equals": query,
            },
        )
        if matching_queries and not cli.query_yes_no(
            "A Saved Query with this Schema and Query already exists."
            " Do you still want to create this saved query?",
            default="no",
        ):
            cli.try_log("Operation cancelled.")
            sys.exit(0)
        uid = post_saved_query_from_data(saved_query)
        cli.try_log(f"Successfully applied new saved query with uid: {uid}")
    else:
        put_saved_query_from_data(uid, saved_query)
        cli.try_log(f"Successfully updated saved query with uid: {uid}")
    return uid


def post_saved_query_from_data(saved_query: Dict) -> str:
    """
    Post a saved query to the current context.

    Args:
        saved_query (Dict): The saved query to be posted.

    Returns:
        None
    """
    ctx = cfg.get_current_context()
    metadata = saved_query[lib.METADATA_FIELD]
    spec = saved_query[lib.SPEC_FIELD]
    req_body = {
        "name": metadata[lib.METADATA_NAME_FIELD],
        "schema": spec[lib.QUERY_SCHEMA_FIELD],
        "query": spec[lib.QUERY_FIELD],
    }
    description = spec.get(lib.QUERY_DESCRIPTION_FIELD)
    if description:
        req_body["description"] = description
    uid = post_new_saved_query(*ctx.get_api_data(), **req_body)
    return uid


def put_saved_query_from_data(uid: str, saved_query: Dict) -> str:
    """
    Put a saved query to the current context.

    Args:
        saved_query (Dict): The saved query to be put.

    Returns:
        None
    """
    ctx = cfg.get_current_context()
    metadata = saved_query[lib.METADATA_FIELD]
    spec = saved_query[lib.SPEC_FIELD]
    req_body = {"name": metadata[lib.METADATA_NAME_FIELD]}
    description = spec.get(lib.QUERY_DESCRIPTION_FIELD)
    if description:
        req_body["description"] = description
    put_saved_query_update(*ctx.get_api_data(), uid, **req_body)
    return uid


# ----------------------------------------------------------------- #
#                          Helper Functions                         #
# ----------------------------------------------------------------- #


def __apply_priority(resrc: Dict) -> int:
    kind = resrc.get(lib.KIND_FIELD)
    return APPLY_PRIORITY.get(kind, 0)


# def __handle_matching_policies(
#     policy: Dict, matching_policies: Dict[str, Dict]
# ):
#     uid = policy[lib.METADATA_FIELD].get(lib.METADATA_UID_FIELD)
#     if uid:
#         return _r.suppression_policies.TraceSuppressionPolicy(policy)
#     query = (
#         "There already exists a policy matching this scope. Would you like"
#         " to merge this policy into the existing one?"
#     )
#     if not cli.query_yes_no(query):
#         return _r.suppression_policies.TraceSuppressionPolicy(policy)
#     ret_pol = policy
#     for uid, m_policy in matching_policies.items():
#         merged = m.merge_resource(ret_pol, "", m_policy)
#         if merged:
#             ret_pol = merged.get_obj_data()
#     ret_pol[lib.METADATA_FIELD][lib.METADATA_UID_FIELD] = uid
#     return _r.suppression_policies.TraceSuppressionPolicy(ret_pol)
