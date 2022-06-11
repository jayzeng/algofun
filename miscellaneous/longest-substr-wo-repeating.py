class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # "abcabcbb"
        # use a dictionary to keep track of each char's left most position
        # {a -> 0, b -> 1, c -> 2...}
        # {a -> 3, b -> 1, c -> 2...} -> update res
        res, left, char_map = 0, 0, {}
        
        for idx, c in enumerate(s):
            if c in char_map:
                left = max(left, char_map[c] + 1)
            res = max(res, idx - left + 1)
            char_map[c] = idx
        
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))