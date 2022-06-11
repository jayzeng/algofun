import collections


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        char_map = {}
        
        for c in chars:
            char_map[c] = char_map.get(c, 0) + 1
        
        res = 0
        
        for word in words:
            if self.check(word, chars, char_map):
                res += len(word)
        
        return res
    
    def check(self, word, chars, char_map):
        if len(word) > len(chars):
            return False
        
        word_counter = collections.Counter()
        
        for c in word:
            word_counter[c] += 1
            if c not in char_map or char_map[c] < word_counter[c]:
                return False
        
        return True

if __name__ == "__main__":
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    print(Solution().countCharacters(words, chars))