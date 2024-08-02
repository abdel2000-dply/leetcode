""""
2134. Minimum Swaps to Group All 1's Together II

A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.
"""
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count_of1 = sum(nums)
        n = len(nums)
        
        # Extend the array to handle the circular nature
        mocknums = nums + nums
        
        current_ones = sum(mocknums[:count_of1])
        max_ones_in_window = current_ones
        
        # Slide the window across the extended array
        for i in range(1, n):
            current_ones += mocknums[i + count_of1 - 1] - mocknums[i - 1]
            max_ones_in_window = max(max_ones_in_window, current_ones)
        
        min_swaps = count_of1 - max_ones_in_window
        
        return min_swaps