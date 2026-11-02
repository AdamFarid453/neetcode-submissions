class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in '-+*/':
                second = stack.pop()
                first = stack.pop()
                if tok == '+':
                    res = first+second
                if tok == '-':
                    res = first-second
                if tok == '*':
                    res = first*second
                if tok == '/':
                    res = int(first/second)
                stack.append(res)
            else:
                stack.append(int(tok))
        return stack[0]

