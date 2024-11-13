#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""

from typing import Iterable, List, Tuple, Sequence

def element_length(list: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function element_length that takes a list input_list of strings and returns a list of tuples, each tuple having a string and an integer. """
    return [(i, len(i)) for i in list]