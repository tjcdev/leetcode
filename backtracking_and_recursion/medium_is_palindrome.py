class Solution:
    def ispalindrome(self, string):
        return string[::-1] == string
    
    def solution(self, s, ans, cur):
        if len(s) == 0:
            ans.append(cur[:])
        
        n = len(list(s))
        for i in range(1, n+1):
            temp_s = s[:i]
            if self.ispalindrome(temp_s):
                cur.append(temp_s)
                self.solution(s[i:], ans, cur)
                cur.pop()
        return
            
    
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cur = []
        self.solution(s, ans, cur)
        return ans