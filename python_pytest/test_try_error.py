import pytest
from try_error import calc_days

def test_valid_integer(capsys):
    calc_days(10)
    captured = capsys.readouterr()
    assert captured.out == "Total days: 3650\n"

def test_non_integer_string(capsys):
    calc_days("ten")
    captured = capsys.readouterr()
    assert "Bad Input: invalid literal for int()" in captured.out

def test_negative_integer(capsys):
    calc_days(-1)
    captured = capsys.readouterr()
    assert captured.out == "Total days: -365\n"

def test_float_string(capsys):
    calc_days("3.14")
    captured = capsys.readouterr()
    assert "Bad Input: invalid literal for int()" in captured.out

def test_none_type(capsys):
    calc_days(None)
    captured = capsys.readouterr()
    assert "Bad Input: Input must be an integer." in captured.out

def test_list_type(capsys):
    calc_days([1, 2, 3])
    captured = capsys.readouterr()
    assert "Bad Input: Input must be an integer." in captured.out