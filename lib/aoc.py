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


def most_common_item(lst):
    # Finds the most common item in a list and how many there are
    count_dict = {}

    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1

    common_item = max(count_dict, key=count_dict.get)
    count = count_dict[common_item]

    return common_item, count


def transpose_list_of_lists(lst):
    # Transposes a list like it's a matrix
    return list(map(list, zip(*lst)))
