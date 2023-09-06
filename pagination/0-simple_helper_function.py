#!/usr/bin/env python3_summary_
"""
task 0
"""

from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """_summary_

    Args:
        page (_type_): _description_
        page_size (_type_): _description_

    Returns:
        tuple[int, int]: _description_
    """
    start_page = (page - 1) * page_size
    end_page = (start_page + page_size)
    return (start_page, end_page)
