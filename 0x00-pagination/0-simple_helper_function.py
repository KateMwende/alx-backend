#!/usr/bin/env python3
"""
index_range function returns a tuple
"""


def index_range(page: int, page_size: int) -> float:
    """Return tuple of start and end idx of a list"""
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
