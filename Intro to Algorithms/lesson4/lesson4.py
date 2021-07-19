from typing import List


def linear_search(data: List, value: int) -> int:
    """
    線性搜尋
    輸入list的data找出指定value的在list中的位置

    Args:
        data (list):輸入的資料
        value (int):要找的值

    Returns:
        int value在data中的位置

    Example:
        linear_search([1,2,3,4,5],3)
        > 2
    """
    for index, val in enumerate(data):
        if val == value:
            return index
    return -1


def binery_search(data: List, value: int) -> int:
    """
    二元搜尋
    輸入list的data找出指定value的在list中的位置

    Args:
        data (list):輸入的資料
        value (int):要找的值

    Returns:
        int value在data中的位置

    Example:
        linear_search([1,2,3,4,5],3)
        > 2
    """
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        elif data[mid] > value:
            right = mid - 1
    return -1


def breadth_search():
    # 課本上的舉例會讓人家看不懂 直接用sentinel_breadth_search?
    pass


def depth_search():
    # 課本上的舉例會讓人家看不懂 直接用sentinel_depth_search?
    pass


def sentinel_breadth_search():
    pass


def sentinel_depth_search():
    pass


def sentinel_right_hand_rule():
    pass


def queen():
    pass


def hanoi():
    pass


def search_file_breadth_search():
    pass


def search_file_depth_search():
    pass


def marubastu1():
    pass


def marubastu2():
    pass


def marubastu3():
    pass
