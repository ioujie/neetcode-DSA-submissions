class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        for char in s:
            if char.isalnum():
                ans.append(char.lower())
        
        return ans == ans[::-1]
