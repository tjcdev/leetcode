# Time Complexity: O(N*M*Log(M)) (M*Log(M) comes from sorting the string), N len(strs), M len of longest string
# Space Complexity: O(N)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        ans_dict = defaultdict(list)
        
        for i in range(0, len(strs)):
            word = strs[i]
            sorted_word = ''.join(sorted(word))
            ans_dict[sorted_word].append(word)
            
        ans = []
        for word, words in ans_dict.items():
            ans.append(words)
            
        return ans
        