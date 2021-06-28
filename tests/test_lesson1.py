from lesson1.quiz import *


def test_list_quiz():
    assert list_quiz() == 51


def test_dict_quiz():
    assert dict_quiz() == {}


def test_search_cpu_codename():
    assert search_cpu_codename([2015, 2016,
                                2021]) == ['kaby lake', 'ice lake', None]
