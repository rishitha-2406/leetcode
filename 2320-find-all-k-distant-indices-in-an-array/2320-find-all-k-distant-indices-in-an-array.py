class Solution:
  def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
    n = len(nums)
    ans = []

    j = 0
    for i in range(n):
      while j < n and (nums[j] != key or j < i - k):
        j += 1
      if j == n:
        break
      if abs(i - j) <= k:
        ans.append(i)

    return ans