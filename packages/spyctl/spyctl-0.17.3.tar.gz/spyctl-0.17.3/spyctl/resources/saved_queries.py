"""Contains functions specific to the saved_query resource."""

from typing import Dict, List

from tabulate import tabulate

import spyctl.schemas_v2 as schemas
import spyctl.spyctl_lib as lib


def data_to_yaml(data: Dict) -> Dict:
    """
    Convert data to a YAML representation of a SavedQueryModel.

    Args:
        data (Dict): The data to be converted.

    Returns:
        Dict: The YAML representation of a SavedQueryModel.
    """
    metadata = schemas.SavedQueryMetadataModel(
        name=data["name"],
        creationTimestamp=data.get("valid_from"),
        createdBy=data.get("created_by"),
        lastUsedTimestamp=data.get("last_used"),
        uid=data.get("uid"),
    )
    spec = schemas.SavedQuerySpecModel(
        **{
            "query": data["query"],
            "schema": data["schema"],
            "description": data["description"],
        }
    )
    model = schemas.SavedQueryModel(
        apiVersion=lib.API_VERSION,
        kind=lib.SAVED_QUERY_KIND,
        metadata=metadata,
        spec=spec,
    )
    return model.model_dump(
        exclude_unset=True, exclude_none=True, by_alias=True
    )


SUMMARY_HEADERS = [
    "NAME",
    "UID",
    "SCHEMA",
    "LAST USED",
    "DESCRIPTION",
]


def summary_output(
    queries: List[Dict], total_pages: int, current_page: int = 0
):
    """
    Print a summary of saved queries.

    Args:
        queries (List[Dict]): The saved queries to be summarized.
    """
    data = []
    for query in queries:
        description = limit_line_length(query.get("description", ""))
        data.append(
            [
                query["name"],
                query["uid"],
                query["schema"],
                lib.epoch_to_zulu(query["last_used"]),
                description,
            ]
        )
    if len(queries) == 0:
        current_page = 0
        total_pages = 0
    else:
        current_page = min(current_page + 1, total_pages)
    rv = [f"Page {current_page}/{total_pages}"]
    rv.append(tabulate(data, headers=SUMMARY_HEADERS, tablefmt="plain"))
    return "\n".join(rv)


WIDE_HEADERS = [
    "NAME",
    "UID",
    "SCHEMA",
    "LAST USED",
    "DESCRIPTION",
    "CREATED BY",
    "QUERY",
]


def wide_output(queries: List[Dict], total_pages: int, current_page: int = 0):
    """
    Print a summary of saved queries.

    Args:
        queries (List[Dict]): The saved queries to be summarized.
    """
    data = []
    for query in queries:
        description = limit_line_length(query.get("description", ""))
        data.append(
            [
                query["name"],
                query["uid"],
                query["schema"],
                lib.epoch_to_zulu(query["last_used"]),
                description,
                query["created_by"],
                query["query"],
            ]
        )
    if len(queries) == 0:
        current_page = 0
        total_pages = 0
    else:
        current_page = min(current_page + 1, total_pages)
    rv = [f"Page {current_page}/{total_pages}"]
    rv.append(tabulate(data, headers=WIDE_HEADERS, tablefmt="plain"))
    return "\n".join(rv)


def limit_line_length(s: str, max_length: int = 50) -> str:
    """
    Limits the line length of a given string by splitting it into multiple
    lines.

    Args:
        s (str): The input string.
        max_length (int, optional): The maximum length of each line. Defaults
            to 50.

    Returns:
        str: The modified string with limited line length.
    """
    lines = s.split("\n")
    new_lines = []
    for line in lines:
        while len(line) > max_length:
            new_lines.append(line[:max_length])
            line = line[max_length:]
        new_lines.append(line)
    return "\n".join(new_lines)
