# 78. Subsets

Given an integer array `nums` of unique elements, return all possible subsets _(the power set)_.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**

```python
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
```

**Constraints:**

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are unique.

## Solution Ideation

Firstly, I think we can initialize the output array ahead of time. It isn't explicitly mentioned that the input `nums` will be in ascending order. It could be random.
