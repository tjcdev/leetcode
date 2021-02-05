class Solution:
    def isValid(self, s: str) -> bool:
        # Algorithm
        '''
        Loop over the string
            if it's an opening bracket then add it to the stack
            if it's a closing bracket then pop from the stack and check it matches
                no match return false
            else:
                continue
            
        return true
        '''
        stack = []
        for char in list(s):
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if (char == ')' and top != '(') or \
                   (char == '}' and top != '{') or \
                   (char == ']' and top != '['):
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        return False    