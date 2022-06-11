class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        res = [''] * numRows
        index, step = 0, 1
        
        for c in s:
            res[index] += c
            
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.convert('PAYPALISHIRING', 3))