class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res, self.target = [], target
        
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(
                    num[i:], num[:i], int(num[:i]), int(num[:i]), res
                )
        
        return res
    
    
    def dfs(self, num, temp, cur_num, last, res):
        if not num:
            if cur_num == self.target:
                res.append(temp)
            return
        
        for i in range(1, len(num) + 1):
            val = num[:i]
            
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], temp + '+' + val, cur_num + int(val), int(val), res)
                self.dfs(num[i:], temp + '-' + val, cur_num - int(val), -int(val), res)
                self.dfs(num[i:], temp + '*' + val, cur_num - last + last * int(val), last * int(val), res)


if __name__ == "__main__":
    num = "123"
    target = 6
    print(Solution().addOperators(num, target))