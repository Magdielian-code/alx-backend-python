
#!/usr/bin/env python3
"""" 7. Complex types - string and int/float to tuple """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of a string and a float"""
    return (k, v * v)
