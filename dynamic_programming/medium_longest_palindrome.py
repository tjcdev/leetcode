def longestPalindrome(self, s: str) -> str:
    n = len(s)
    if(n<2):
        return s
    left = 0
    right = 0

    palindrome = [[0]*n for _ in range(n)]

    for j in range(1, n):
        for i in range(0, i):
            innerIsPalindrome = palindrome[i+1][j-1] or j-i<=2
            if (s[j] == s[i] and innerIsPalindrome):
                palindrome[i][j] = True
                if (j-i) > right-left:
                    right = j
                    left = i

    return s[left:right+1]