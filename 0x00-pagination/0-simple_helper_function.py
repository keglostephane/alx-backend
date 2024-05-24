#!/usr/bin/env python3
"""pagination_helper
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple a start index and end index to paginate
    a given page.
    """
    return (page - 1) * page_size, page * page_size
