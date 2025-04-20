from collections import defaultdict
import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
         unique = defaultdict(int)  
         for a in answers:
            unique[a] += 1
         tot = 0
         for sim, count in unique.items():
            base_num = sim + 1 
            tot += math.ceil(count / base_num) * base_num 
         return tot
