#!/usr/bin/env python3
"""paginate_database
"""
import csv
from typing import List, Tuple, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple a start index and end index to paginate
    a given page.
    """
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializer"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: Optional[int] = 1,
                 page_size: Optional[int] = 10) -> List[List]:
        """return a list of items in the page"""
        assert type(page) is int and page > 0, "not a valid page"
        assert type(page_size) is int and page_size > 0, \
            "not a valid page size"
        data = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(data):
            return []
        if (end - start) > len(data):
            return data[start:]
        return data[start:end]
