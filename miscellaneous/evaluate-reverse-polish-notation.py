class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ['+', '-', '*', '/']
        
        for token in tokens:
            if token not in operators:
                stack.append(self.str2int(token))
            else:
                y, x = stack.pop(), stack.pop()
                stack.append(self.compute(x, y, token))
        
        return stack.pop()
    
    def str2int(self, token):
        sign, num, idx = 1, 0, 0

        if token[idx] in ['+', '-']:
            idx += 1
        
        if token[0] == '-':
            sign = -1

        for i in range(idx, len(token)):
            num = num * 10 + ord(token[i]) - ord('0')
        
        return num * sign
    
    def compute(self, x, y, token):
        if token == '+':
            return x + y
        if token == '-':
            return x - y
        if token == '/':
            return int(float(x) / y)
        if token == '*':
            return x * y

if __name__ == "__main__":
    # tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    tokens = ["3","-4","+"]
    print(Solution().evalRPN(tokens))