

class Solution:
    def shortestPalindrome(self, s):
        right = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == s[right]:
                right += 1
        
        if right == len(s):
            return s

        mid = self.shortestPalindrome(s[:right])
        return s[::-1] + mid + s[:right]


if __name__ == "__main__":
    s = Solution()
    print(s.shortestPalindrome("sdsdlkjsaoio"))