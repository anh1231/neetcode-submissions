class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'*': lambda x, y: x * y,\
        '+': lambda x, y: x + y,\
        '/': lambda x, y: int(y / x), \
        '-': lambda x, y: y - x}


        for i in tokens:
            if i in op:
                stack.append(op[i](stack.pop(), stack.pop()))
            else:
                stack.append(int(i))
        return stack[0]