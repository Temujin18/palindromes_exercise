## Fun with Palindromes

### Level 1

Write a function that takes in a non-empty string and returns a boolean representing whether the string is a palindrome.

#### Approach for Level 1

A simple check for the equality between the text and the inverse of the text. String inverse can be done either by using string slicing or joining the `reversed()` text. I went with string slicing `text[::-1]` since this proved to be faster than the latter, as confirmed by running `timeit`.

### Level 2

Write a function that, given a string, returns its longest palindromic substring. You can assume that there will only be one longest palindromic substring.

#### Approach for Level 2

The first thought that always comes to mind is to not reinvent the wheel and look for existing code, that's probably widely tested. I came across several implementations of Manacher's algorithm. This solution has O(n) time complexity. I also did a naive solution, for the sake of comparison. My own solution has O(n**2) complexity since it involves running 2 for loops to arrive at an answer.


Note: I used numba to JIT compile the naive_lps function. Original runtime for 10,000 cycles is 0.4 seconds. With numba, it takes 2 seconds to first compile and run the function, and for the next cached run, runtime is down to 0.2 seconds. But Manacher's algorithm still is faster, with runtimes between 0.15 to 0.2 for 10,000 cycles.
### Level 3

Write a function that returns the minimum number of cuts needed to perform on the string such that each remaining substring is a palindrome.

#### Approach for Level 3

Same with Level 2, I searched for existing solutions. I came across several implementations, but chose one that incorporated memoization. Memoization is just "remembering" answers to previous inputs, so we would not have to recompute and therefore save time. The implementation I found has O(n**2) complexity, and I have not found any better alternative. I have included references for the implementations as code comments.

### To Run Project

1. Clone repository
2. Create virtual environment and install dependencies from requirements.txt. Main dependencies are pytest and numba.
3. To run tests, open terminal in project directory and run `python -m pytest`

Notes: Used Python 3.7 for this project as requirement for numba. No dice in using JIT to other functions, will have to go through numba docs to make it work.
