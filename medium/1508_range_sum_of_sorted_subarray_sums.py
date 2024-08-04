"""
1508. Range Sum of Sorted Subarray Sums

You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.
"""

lass Solution:
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