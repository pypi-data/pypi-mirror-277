"""Contains click options shared by multiple get commands."""

import time

import click

import spyctl.config.configs as cfg
import spyctl.spyctl_lib as lib


def context_options(f):
    """Add context options to a click command."""
    f = click.option(
        f"--{cfg.MACHINES_FIELD}",
        help="Only show resources to these nodes."
        " Overrides value current context if it exists.",
        type=lib.ListParam(),
        metavar="",
    )(f)
    f = click.option(
        f"--{cfg.CLUSTER_FIELD}",
        help="Only show resources tied to this cluster."
        " Overrides value current context if it exists.",
        type=lib.ListParam(),
        metavar="",
    )(f)
    f = click.option(
        f"--{cfg.NAMESPACE_FIELD}",
        help="Only show resources tied to this namespace."
        " Overrides value current context if it exists.",
        type=lib.ListParam(),
        metavar="",
    )(f)
    f = click.option(
        "--pod",
        cfg.POD_FIELD,
        help="Only show resources tied to this pod uid."
        " Overrides value current context if it exists.",
        type=lib.ListParam(),
        metavar="",
    )(f)
    return f


def container_context_options(f):
    """Add container context options to a click command."""
    f = click.option(
        "--image",
        cfg.IMG_FIELD,
        help="Only show resources tied to this container image."
        " Overrides value current context if it exists.",
        type=lib.ListParam(),
        metavar="",
    )(f)
    f = click.option(
        "--image-id",
        cfg.IMGID_FIELD,
        help="Only show resources tied to containers running with this"
        " image id. Overrides value current context if it exists.",
        type=lib.ListParam(),
        metavar="",
    )(f)
    f = click.option(
        "--container-name",
        cfg.CONTAINER_NAME_FIELD,
        help="Only show resources tied to containers running with this"
        " container name. Overrides value current context if it exists.",
        type=lib.ListParam(),
        metavar="",
    )(f)
    f = click.option(
        "--container-id",
        cfg.CONT_ID_FIELD,
        help="Only show resources tied to containers running with this"
        " container id. Overrides value current context if it exists.",
        type=lib.ListParam(),
        metavar="",
    )(f)
    return f


def l_svc_context_options(f):
    """Add Linux service context options to a click command."""
    f = cgroup_option(f)
    return f


def time_options(f):
    """Add time options to a click command."""
    f = click.option(
        "-t",
        "--start-time",
        "st",
        help="Start time of the query. Default is 24 hours ago.",
        default="24h",
        type=lib.time_inp,
    )(f)
    f = click.option(
        "-e",
        "--end-time",
        "et",
        help="End time of the query. Default is now.",
        default=time.time(),
        type=lib.time_inp,
    )(f)
    return f


def source_query_options(f):
    """Add source query options to a click command."""
    time_options(f)
    context_options(f)
    f = exact_match_option(f)
    f = help_option(f)
    f = output_option(f)
    f = name_or_id_arg(f)
    return f


help_option = click.help_option("-h", "--help", hidden=True)

exact_match_option = click.option(
    "-E",
    "--exact",
    "--exact-match",
    is_flag=True,
    help="Exact match for NAME_OR_ID. This command's default behavior"
    "displays any resource that contains the NAME_OR_ID.",
)

cgroup_option = click.option(
    "--cgroup",
    cfg.CGROUP_FIELD,
    help="Only show resources tied to machines running Linux services with"
    " this cgroup. Overrides value current context if it exists.",
    type=lib.ListParam(),
    metavar="",
)

output_option = click.option(
    "-o",
    "--output",
    default=lib.OUTPUT_DEFAULT,
    type=click.Choice(
        lib.OUTPUT_CHOICES + [lib.OUTPUT_WIDE], case_sensitive=False
    ),
)

page_option = click.option(
    "--page",
    help="Page number of resources to display.",
    type=click.IntRange(1, clamp=True),
    default=1,
    metavar="",
)

page_size_option = click.option(
    "--page-size",
    help="Number of resources to display per page.",
    type=click.IntRange(-1),
    metavar="",
)

# Arguments

name_or_id_arg = click.argument("name_or_id", required=False)
