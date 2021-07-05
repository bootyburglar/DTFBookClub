from lesson3 import *


def parse_answer(capsys):
    try:
        out, err = capsys.readouterr()
        out = out.strip().upper()
        ans = out[out.find("(") + 1:out.find(")")]
        ans = ans.upper()
    except:
        pass
    return out, ans


def test_bmi(capsys):
    bmi(100, 100)
    out, ans = parse_answer(capsys)
    assert out == "O(1)" or ans == 1


def test_pi_1(capsys):
    pi_1(10)
    out, ans = parse_answer(capsys)
    assert out == "O(N^2)" or ans == "N^2"


def test_pi_2(capsys):
    pi_2(10)
    out, ans = parse_answer(capsys)
    assert out == "O(N)" or ans == "N"
