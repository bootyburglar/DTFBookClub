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
    pass


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
    pass


#region Define a data tree
class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.val = val

    def insert_left(self, val):
        if not self.left:
            self.left = TreeNode(val)
        else:
            self.insert_left(val)

    def insert_right(self, val):
        if not self.right:
            self.right = TreeNode(val)
        else:
            self.insert_right(val)


def createTree():
    tree = TreeNode(0)
    tree.insert_left(1)
    tree.insert_right(2)
    tree.left.insert_left(3)
    tree.left.insert_right(4)
    tree.right.insert_left(5)
    tree.right.insert_right(6)
    tree.left.left.insert_left(7)
    tree.left.left.insert_right(8)
    tree.left.right.insert_left(9)
    tree.left.right.insert_right(10)
    tree.right.left.insert_left(11)
    tree.right.left.insert_right(12)
    tree.right.right.insert_left(13)
    tree.right.right.insert_right(14)
    return tree


#endregion
tree = createTree()


def breadth_search():
    # 用上面的 tree 來做
    pass


def depth_search():
    # 用上面的 tree 來做
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
