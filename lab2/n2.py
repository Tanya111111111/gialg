#150 Evaluate Reverse Polish Notation
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b) if a * b >= 0 else -(-a // b))
            else:
                stack.append(int(t))
        return stack[0]