# 131. Palindrome Partitioning

> Level: Medium

## Details

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return *all possible palindrome partitioning of `s`*.

```python
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]
```

## Constraints

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

## Solution Ideation

Keeping in mind that all substrings in a partition must be palindrome, this will be the output:

```python
Input: s = "aabc"
Output: [["a","a","b","c"],["aa","b","c"]]
```

Obvious output: each of the individual letters.

We can also check if the full string is a palindrome easily.

Now, the substrings. My first idea is to do a nested for loop that checks if a palindrome exists from a starting point and if there exists one, we can check if there are any other palindromes within that partition. If not, we can just output each individual letter. We need to also recheck from where the first palindrome left of in case there is a longer palindrome.
