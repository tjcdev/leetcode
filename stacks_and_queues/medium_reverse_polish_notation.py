# https://leetcode.com/problems/evaluate-reverse-polish-notation/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        - Intuition is to use a stack
        - when we encounter a symbol token, we pop the last two items from the stack, apply the token, and push the answer onto the stack
        """
        stack = []
        for token in tokens:
            if token == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a+b)
            elif token == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a-b)
            elif token == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a*b)
            elif token == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a/b)
            else:
                stack.append(token)

        return int(stack[0])