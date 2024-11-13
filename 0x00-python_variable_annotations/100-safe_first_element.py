#!/usr/bin/env python3
""" 100. Safe first element! """

from typing import Sequence, Union, Any

def safe_first_element(ist: Sequence[Any]) -> Union[Any, None]:
    """ function safe_first_element that takes a sequence ist of any type and returns its first element. """
    if ist:
        return ist[0]
    else:
        return None