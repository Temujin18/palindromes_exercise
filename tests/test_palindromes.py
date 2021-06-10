import timeit
from palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome("abcdcba") == True
