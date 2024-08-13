"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, curr_comb, curr_sum):
            if curr_sum == target:
                result.append(curr_comb[:])
                return
            if curr_sum > target:
                return

            for i in range(start, len(candidates)):
                curr_comb.append(candidates[i])
                backtrack(i, curr_comb, curr_sum + candidates[i])
                curr_comb.pop()

        result = []
        backtrack(0, [], 0)
        return result