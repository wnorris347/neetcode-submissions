class Solution:
    def isPalindrome(self, s: str) -> bool:
        an = "1234567890qwertyuiopasdfghjklzxcvbnm"
        front = 0
        back = len(s)-1
        while back > front:
            if s[front].lower() not in an:
                front += 1
                continue
            if s[back].lower() not in an:
                back -= 1
                continue
            if not s[front].lower() == s[back].lower():
                return False
            front += 1
            back -= 1
        return True