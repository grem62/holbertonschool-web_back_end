#!/usr/bin/env python3_summary_
"""
task 0
"""

from typing import Tuple
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        azert = []
        dataset = self.dataset()
        jerome_, matheo = index_range(page, page_size)
        if matheo >= len(dataset):
            return azert
        else:
            return dataset[jerome_:matheo]
