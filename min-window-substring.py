
import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        counter = collections.Counter(t)
        missing = len(t)
        
        left, min_start, min_end = 0, 0, 0
        
        for right, char in enumerate(s, 1):
            missing -= (counter[char] > 0)
            counter[char] -= 1
            
            if not missing:
                while left < right and counter[s[left]] < 0:
                    counter[s[left]] += 1
                    left += 1
                
                if not min_end or right - left <= min_end - min_start:
                    min_start, min_end = left, right
                    
        return s[min_start:min_end]


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))