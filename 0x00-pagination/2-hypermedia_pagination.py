#!/usr/bin/env python3
"""hypermedia_paginate_database
"""
import csv
import math
from typing import List, Tuple, Dict


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns a list of items in the page"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start, end = index_range(page, page_size)

        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dict description of items in the page."""
        dataset_length = len(self.dataset())
        data = self.get_page(page, page_size)

        return {
            'page_size': len(data) if data != [] else 0,
            'page': page,
            'data': data,
            'next_page': page + 1 if self.get_page(page + 1, page_size)
            else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': math.ceil(dataset_length / page_size)
        }
