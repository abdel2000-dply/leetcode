"""2053. Kth Distinct String in an Array

"""
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dist = []
        n = len(arr)
        l = 0

        for i in range(n):
            if l == k:
                return dist[k - 1]

            curr = arr[i]
            new = arr[:i] + arr[i + 1:]
            if curr not in new:
                l += 1
                dist.append(curr)
        if k > l:
            return ""
        return dist[l - 1]

