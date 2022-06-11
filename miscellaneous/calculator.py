

class BasicCalculator:
    def calculate(self, s):
        num = 0
        res = 0
        sign = 1
        stack = []

        for i in range(len(s)):
            # if s[i] is digit
            if ord('0') <= ord(s[i]) <= ord('9'):
                num = ord(s[i]) - ord('0') + num * 10
            elif s[i] in ['+', '-']:
                res += sign * num
                sign = 1 if s[i] == '+' else -1
                num = 0
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res, num, sign = 0, 0, 1
            elif s[i] == ')':
                res += sign * num
                prev_sign, prev_res = stack.pop(), stack.pop()
                res = res * prev_sign + prev_res
                num, sign = 0, 1
        
        if num != 0:
            res += sign * num

        return res

if __name__ == "__main__":
    s = "1 + (1 + 2)"
    print(BasicCalculator().calculate(s))