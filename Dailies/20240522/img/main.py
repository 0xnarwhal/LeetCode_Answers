from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub_s):
            return sub_s == sub_s[::-1]
        
        def backtrack(start, path, ans):
            if start == len(s):
                ans.append(list(path))
                return
            
            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    path.append(s[start:i+1])
                    backtrack(i+1, path, ans)
                    path.pop()
        
        ans = []
        backtrack(0, [], ans)
        return ans