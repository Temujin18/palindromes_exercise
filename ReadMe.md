## Fun with Palindromes

### Level 1

Write a function that takes in a non-empty string and returns a boolean representing whether the string is a palindrome.

#### Approach for Level 1

A simple check for the equality between the text and the inverse of the text. String inverse can be done either by using string slicing or joining the `reversed()` text. I went with string slicing `text[::-1]` since this proved to be faster than the latter, as confirmed by running `timeit`.

### Level 2

Write a function that, given a string, returns its longest palindromic substring. You can assume that there will only be one longest palindromic substring.

#### Approach for Level 2

The first thought that always comes to mind is to not reinvent the wheel and look for existing code, that's probably widely tested. I came across several implementations of Manacher's algorithm. This solution has O(n) time complexity. I also did a naive solution, for the sake of comparison. My own solution has O(n**2) complexity since it involves running 2 for loops to arrive at an answer.

### Level 3

Write a function that returns the minimum number of cuts needed to perform on the string such that each remaining substring is a palindrome.

#### Approach for Level 3

Same with Level 2, I searched for existing solutions. I came across several implementations, but chose one that incorporated memoization. Memoization is just "remembering" answers to previous inputs, so we would not have to recompute and therefore save time. The implementation I found has O(n**2) complexity, and I have not found any better alternative. I have included references for the implementations as code comments.
