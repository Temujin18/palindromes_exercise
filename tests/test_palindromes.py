from palindrome import is_simple_palindrome, longest_palindromic_substring, minimum_cuts_for_palindrome_substrings


def test_is_palindrome():
    assert is_simple_palindrome("abcdcba")


def test_lps():
    assert longest_palindromic_substring("abaxyzzyxf") == "xyzzyx"


def test_min_cuts():
    assert minimum_cuts_for_palindrome_substrings("noonabbad") == 2

