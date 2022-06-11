import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        counter = {}
        words = re.findall(r'\w+', paragraph.lower())
        banned = set(banned)
        res = ''
        
        for word in words:
            if word in banned:
                continue
                
            counter[word] = counter.get(word, 0) + 1
            
            if counter[word] > counter.get(res, 0):
                res = word
        
        return res


if __name__ == "__main__":
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]
    # paragraph = "Bob. hIt, baLl"
    # banned = ["bob", "hit"]
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]

    s = Solution()
    print(s.mostCommonWord(paragraph, banned))