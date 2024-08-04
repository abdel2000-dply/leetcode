class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray = []
        mod = 10**9 + 7

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                # we add to curr_sum and append it to the subarray
                curr_sum += nums[j]
                subarray.append(curr_sum)

        subarray.sort()

        res = sum(subarray[left-1:right]) % mod

        return res        