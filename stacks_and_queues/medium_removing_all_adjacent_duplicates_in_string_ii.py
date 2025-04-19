class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Use a stack
        We should be able to do this in O(N)
        We need to know how long the string of duplicate characters is, each time we pick up a character.
        Maintain two stacks, one is the character, and one is the number of times the character has appeared
        """
        chars = []
        counters = []
        for c in s:
            if len(chars) == 0:
                chars.append(c)
                counters.append(1)
                continue
            if c == chars[-1]:
                counter = counters.pop() + 1
                if counter == k:
                   chars.pop()
                else:
                    counters.append(counter)
            else:
                chars.append(c)
                counters.append(1)
        # reconstruct the string
        ans = []
        for i in range(len(chars)):
            for _ in range(counters[i]):
                ans.append(chars[i])
        return "".join(ans)