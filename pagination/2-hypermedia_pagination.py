#!/usr/bin/env python3
"""Logic behind pagination"""
import csv
import math
from typing import List, Dict, Any, Tuple

index_range = __import__("0-simple_helper_function").index_range


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
        sliced_dataset = self.dataset()[tuple_value[0]:tuple_value[1]]
        return sliced_dataset

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """A method that takes the same arguments (and defaults)
        as get_page method
        and returns a dictionary containing the following key-value pairs:"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        total_pages = (len(self.dataset()) + page_size - 1) // page_size
        data = self.get_page(page, page_size)
        page_size = page_size if data else 0
        hypermedia = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
        return hypermedia
