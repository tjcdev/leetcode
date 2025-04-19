class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Use a stack
        Iterate through the list 
            if the top of the stack equals the current letter:
                pop the stack and move on
            else:
                add to the stack
        return the stack joined by ""
        """
        stack = []
        for c in s:
            if len(stack) > 0  and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)