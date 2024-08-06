
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        
        sorted_freq = sorted(freq.values(), reverse=True)
        
        min_push = 0
        mult = 1
        
        for i, count in enumerate(sorted_freq):
            min_push += count * mult
            
            if (i + 1) % 8 == 0:
                mult += 1
                
        return min_push      