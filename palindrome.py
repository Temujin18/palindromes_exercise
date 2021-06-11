import timeit
from numba import jit


def is_simple_palindrome(text: str) -> bool:
    return text == text[::-1]


@jit(nopython=True)
def naive_lps(text: str) -> str:
    text_length = len(text)

    max_length = 1
    start = 0

    for i in range(text_length):
        for j in range(i, text_length):
            # string of length 1 is considered a palindrome at start
            is_substring_palindrome = True

            for k in range(0, ((j - i) // 2) + 1):
                if text[i + k] != text[j - k]:
                    is_substring_palindrome = False

            if is_substring_palindrome and (j - i + 1) > max_length:
                start = i
                max_length = j - i + 1

    return text[start:(start + max_length)]


def longest_palindromic_substring(text: str) -> str:
    # Reference: https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/Manacher-algorithm-in-Python-O(n)
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = "#".join(f"^{text}$")
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range(1, n - 1):
        P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P.
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return text[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


def minimum_cuts_for_palindrome_substrings(text: str) -> int:
    # Reference: https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/

    # Function to check if input string is palindrome or not
    def is_palindrome(input: str, start: int, end: int) -> bool:
        # Using two pointer technique to check palindrome
        while start < end:
            if input[start] != input[end]:
                return False
            start += 1
            end -= 1
        return True

    # Function to find keys for the Hashmap
    def convert(a: int, b: int) -> str:
        return str(a) + str(b)

    # Returns the minimum number of cuts needed to partition a string
    # such that every part is a palindrome
    def minpalparti_memo(input: str, i: int, j: int, memo: dict):
        if i > j:
            return 0

        # Key for the Input String
        ij = convert(i, j)

        # If the no of partitions for string "ij" is already calculated
        # then return the calculated value using the Hashmap
        if ij in memo:
            return memo[ij]

        # Every String of length 1 is a palindrome
        if i == j:
            memo[ij] = 0
            return 0
        if is_palindrome(input, i, j):
            memo[ij] = 0
            return 0
        minimum = 1000000000

        # Make a cut at every possible location starting from i to j
        for k in range(i, j):
            left_min = 1000000000
            right_min = 1000000000
            left = convert(i, k)
            right = convert(k + 1, j)

            # If left cut is found already
            if left in memo:
                left_min = memo[left]

            # If right cut is found already
            if right in memo:
                right_min = memo[right]

            # Recursively calculating for left and right strings
            if left_min == 1000000000:
                left_min = minpalparti_memo(input, i, k, memo)
            if right_min == 1000000000:
                right_min = minpalparti_memo(input, k + 1, j, memo)

            # Taking minimum of all k possible cuts
            minimum = min(minimum, left_min + 1 + right_min)
        memo[ij] = minimum

        # Return the min cut value for complete string.
        return memo[ij]

    return minpalparti_memo(text, 0, len(text) - 1, {})


if __name__ == '__main__':
    funcs = {
        is_simple_palindrome: "abcdcba",
        longest_palindromic_substring: "abaxyzzyxf",
        naive_lps: "abaxyzzyxf",
        minimum_cuts_for_palindrome_substrings: "noonabbad",
    }
    # Loop twice, Numba would compile during first loop and will take time
    # On second loop, numba would use cached function and would run faster
    for _ in range(2):
        for func, val in funcs.items():
            t = timeit.Timer(lambda: func(val))
            print(f"{func.__name__}: {t.timeit(10_000)}")
