from lesson3 import *


def parse_answer(capsys):
    try:
        out, err = capsys.readouterr()
        ans = out[out.find("(") + 1:out.find(")")]
    except:
        pass
    return out, ans


def test_bmi(capsys):
    out, ans = parse_answer(capsys)
    assert out.upper() == "O(1)" or ans.upper() == 1


def test_pi_1(capsys):
    out, ans = parse_answer(capsys)
    out, err = capsys.readouterr()
    assert out.upper() == "O(N^2)" or ans.upper() == "N^2"


def test_pi_2(capsys):
    out, ans = parse_answer(capsys)
    assert out.upper() == "O(N)" or ans.upper() == "N"
