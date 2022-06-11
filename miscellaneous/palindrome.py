
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1

        return True

    def isPalindrome(self, s: str) -> bool:
        mid = len(s) // 2
        left, right = mid, mid

        if len(s) % 2 == 0:
            left -= 1
            return self.check(s, left, right)
        else:
            left -=1
            right += 1
            return self.check(s, left, right)
    
    def check(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return False
            left, right = left - 1, right + 1
        return True

if __name__ == '__main__':
    s = Solution()
    # print(s.isPalindrome('abba'))
    # print(s.isPalindrome('abbb'))
    print(s.isPalindrome('abc'))
    print(s.isPalindrome('aba'))
    print(s.isPalindrome('aab'))
    print(s.isPalindrome('aabaa'))