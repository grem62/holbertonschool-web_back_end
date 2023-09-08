#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index=None, page_size=10):
        # Check if index is within a valid range
        assert index is None or (0 <= index < len(self.dataset()))

        # Calculate the current index, next index, and the actual page of data
        current_index = index if index is not None else 0
        dataset = self.dataset()
        next_index = min(current_index + page_size, len(dataset))
        data = dataset[current_index:next_index]

        # Return the dictionary with the required information
        return {
            "index": current_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
