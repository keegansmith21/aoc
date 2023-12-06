from typing import Union, Iterable, Literal, Tuple


def n_in_range(
    n: Union[int, float], r: Iterable[Union[int, bool]], inclusive: Tuple[bool, bool] = (True, True)
) -> Union[int, float, Literal[False]]:
    """Checks if a int/float is within a range of ints/floats

    :param n: number
    :param r: range
    :param inclusive: (low_inclusive, high_inclusive)
    :return: if in range - the offset from lowest value in range, else False
    """
    low = min(r)
    high = max(r)

    if inclusive[0]:
        if n <= low:
            return False
    else:
        if n < low:
            return False

    if inclusive[1]:
        if n >= high:
            return False
        else:
            if n > high:
                return False

    return n - low
