"""
Given a list of 24-hour clock time points in "HH:MM" format, 
return the minimum minutes difference between any two time-points in the list.

"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeinmin = []
        for time in timePoints:
            [h, m] = time.split(':')
            minutes = int(h) * 60 + int(m)
            timeinmin.append(minutes)
        timeinmin.sort()
        print(timeinmin)
        diff = min(timeinmin[i + 1] - timeinmin[i] for i in range(len(timeinmin) - 1))
        # consider difference between last and first element
        return min(diff, 24 * 60 - timeinmin[-1] + timeinmin[0])
        