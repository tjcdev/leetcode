class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Sorting would O(nlogn)

        Created a set, Sorted it, create a dictionary of val: rank

        Loop over arr, replacing with it's dictionary
        """
        ordered_set = sorted(set(arr)) # O(n log n)
        ranks = {arr_val: i for i, arr_val in enumerate(ordered_set)}
        return [ranks[a]+1 for a in arr]