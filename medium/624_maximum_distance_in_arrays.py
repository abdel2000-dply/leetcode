'''624. Maximum Distance in Arrays

You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.
'''
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_v = arrays[0][0]
        max_v = arrays[0][-1]
        
        max_dist = 0
        
        for i in range(1, len(arrays)):
            max_dist = max(max_dist, abs(arrays[i][-1] - min_v), abs(max_v - arrays[i][0]))
            
            min_v = min(min_v, arrays[i][0])
            max_v = max(max_v, arrays[i][-1])
        
        return max_dist