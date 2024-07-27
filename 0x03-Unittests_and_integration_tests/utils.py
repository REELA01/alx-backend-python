#!/usr/bin/env python3
"""utilities for github org clients"""
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """access nested map with key path"""
    for ky in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(ky)
        nested_map = nested_map[ky]
    return nested_map


def get_json(url: str) -> Dict:
    """get JSON from remote URL"""
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """decorator to memoize a method"""
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return property(memoized)
