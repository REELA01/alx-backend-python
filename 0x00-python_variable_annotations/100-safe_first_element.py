#!/usr/bin/env python3
"""Task 10 module"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieve the first element of a sequence if it exist"""
    if lst:
        return lst[0]
    else:
        return None
