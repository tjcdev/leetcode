class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        
        boats = 0
        
        if len(people) == 1:
            return 1
        
        left = 0
        right = len(people) - 1
        
        while(left <= right):
            if left == right:
                boats += 1
                break
                
            if (people[left] + people[right] <= limit):
                left += 1
                right -= 1
                boats += 1
            else:
                left += 1
                boats += 1
        
        return boats
        