"""
Uncommon Words from Two Sentences

A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1Words = s1.split(' ')
        s2Words = s2.split(' ')

        words = s1Words + s2Words
        wordsCount = Counter(words)
        uncommon = []
        
        for k, v in wordsCount.items():
            if v == 1:
                uncommon.append(k)

        return uncommon

# optimized Solution
class Solution2:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordsCount = Counter((s1 + " " + s2).split())
        uncommon = []
        
        for k, v in wordsCount.items():
            if v == 1:
                uncommon.append(k)

        return uncommon

# More optimized Solution
class Solution3:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordsCount = Counter((s1 + " " + s2).split())
        return [k for k, v in wordsCount.items() if v == 1]