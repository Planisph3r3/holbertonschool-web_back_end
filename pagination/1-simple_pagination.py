#!/usr/bin/env python3
"""Logic behind simple pagination"""

import csv
import math
from typing import Tuple, List

class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A method that checks the upcoming parameters and uses them for
        making the proper slicing of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        tuple_value = index_range(page, page_size)
        return self.dataset()[tuple_value[0]:tuple_value[1]]


def index_range(page: int, page_size: int) -> Tuple:
    """The function should return a tuple of size two
    containing a start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters"""

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)