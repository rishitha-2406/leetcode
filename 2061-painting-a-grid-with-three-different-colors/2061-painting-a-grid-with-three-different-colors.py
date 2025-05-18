class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from itertools import product
        MOD = 10**9 + 7
        colors = [0, 1, 2]  # 0: Red, 1: Green, 2: Blue

        # Generate all valid columns
        def is_valid(col):
            return all(col[i] != col[i+1] for i in range(len(col) - 1))

        all_cols = [col for col in product(colors, repeat=m) if is_valid(col)]

        # Precompute which columns are compatible
        transitions = {}
        for c1 in all_cols:
            transitions[c1] = []
            for c2 in all_cols:
                if all(x != y for x, y in zip(c1, c2)):
                    transitions[c1].append(c2)

        # DP
        dp = {col: 1 for col in all_cols}
        for _ in range(n - 1):
            new_dp = {}
            for col in all_cols:
                new_dp[col] = sum(dp[prev] for prev in transitions[col]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD
  