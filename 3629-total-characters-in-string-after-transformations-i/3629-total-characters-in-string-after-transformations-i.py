class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        from collections import Counter

        
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        for _ in range(t):
            new_cnt = [0] * 26
            for i in range(25):  
                new_cnt[i + 1] = (new_cnt[i + 1] + cnt[i]) % MOD
            
            new_cnt[0] = (new_cnt[0] + cnt[25]) % MOD  
            new_cnt[1] = (new_cnt[1] + cnt[25]) % MOD  
            cnt = new_cnt

        return sum(cnt) % MOD
