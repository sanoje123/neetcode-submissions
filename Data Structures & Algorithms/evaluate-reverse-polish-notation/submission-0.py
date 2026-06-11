class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []
        set_op = {'+', '-', '*', '/'}
        for t in tokens:
            if t in set_op:
                if t == '+':
                    number_stack.append(number_stack.pop() + number_stack.pop())
                if t == '*':
                    number_stack.append(number_stack.pop() * number_stack.pop())
                if t == '-':
                    a, b = number_stack.pop(), number_stack.pop()
                    number_stack.append(b - a)
                if t == '/':
                    a, b = number_stack.pop(), number_stack.pop()
                    number_stack.append(int(float(b) / a))
            else:
                number_stack.append(int(t))

        return number_stack[0]

        