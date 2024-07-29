"""
 1395. Count Number of Teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
 
"""

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        left_smaller = [0] * n
        left_larger = [0] * n
        right_smaller = [0] * n
        right_larger = [0] * n

        # first lets fill the arrays above
        # fill left_*
        for j in range(n):
            for i in range(j): # starts at 0 to the current j (left rating)
                if rating[i] > rating[j]:
                    left_larger[j] += 1 # will contain number of large numbers in the left of j
                if rating[i] < rating[j]:
                    left_smaller[j] += 1 # will contain number of small number in the left of j

        # fill right_*
        for j in range(n):
            for i in range(j, n):
                if rating[i] > rating[j]:
                    right_larger[j] += 1
                if rating[i] < rating[j]:
                    right_smaller[j] += 1

        count = 0
        for j in range(n):
            count += left_smaller[j] * right_larger[j]
            count += left_larger[j] * right_smaller[j]

        return count
