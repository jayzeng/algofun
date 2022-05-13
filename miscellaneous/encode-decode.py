import unittest

# An interesting problem from:
# https://leetcode.com/problems/encode-and-decode-strings/

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode
# Example1

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"
# Example2

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

class Encoder:
    def encode(self, strs):
        # encode the list of strings to a string
        # len(word1) + # + len(word2) + # + ...
        res = []

        for s in strs:
            res.append(str(len(s)) + '#' + s)
        
        return ''.join(res)

    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            
            word_len = int(str[i:j])
            res.append(str[j+1:j+word_len+1])
            i = j + word_len + 1
        
        return res

class TestSort(unittest.TestCase):
    def test_encode_decode(self):
        all_words = [
            ['hello', '5world:#', 'beautiful', 'world'],
            ['5 can   h', 'I', 'encod#?s ', 't h i .      s'],
        ]

        for words in all_words:
            encoder = Encoder()
            encoded_str = encoder.encode(words)
            decoded_words = encoder.decode(encoded_str)
            print(f'words {words}, encoded: {encoded_str}, decoded: {decoded_words}')
            self.assertEqual(words, decoded_words)

if __name__ == "__main__":
    unittest.main()