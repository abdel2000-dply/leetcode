"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, curr_comb, curr_sum):
            if curr_sum == target:
                result.append(curr_comb[:])
                return
            if curr_sum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                curr_comb.append(candidates[i])
                backtrack(i+1, curr_comb, curr_sum + candidates[i])
                curr_comb.pop()

        result = []
        candidates.sort()
        backtrack(0, [], 0)
        return result