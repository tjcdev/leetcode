def validMountainArray(self, arr: List[int]) -> bool:
    if len(arr) < 3:
        return False
    
    i = 1
    # Find the index where it stops increasing
    while(i < len(arr) and arr[i] > arr[i-1]):
        i+=1
    
    # If it never increased OR increased the whole way
    if (i == 1 or i == len(arr)):
        return False
    
    # Find where it stops decreasing (after i)
    while(i < len(arr) and arr[i] < arr[i-1]):
        i+=1
    
    # If we reached the end of the arr then it is a mountain
    return i==len(arr)