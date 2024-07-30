"""
1653. Minimum Deletions to Make String Balanced

You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

"""
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        b_left = [0] * n
        a_right = [0] * n

        b_count = 0
        a_count = 0

        for i in range(n):
            b_left[i] = b_count
            if s[i] == 'b':
                b_count += 1

        for i in range(n - 1, -1, -1):
            a_right[i] = a_count
            if s[i] == 'a':
                a_count += 1

        min_del = float('inf')
        for i in range(n):
            min_del = min(min_del, a_right[i] + b_left[i])

        return min_del