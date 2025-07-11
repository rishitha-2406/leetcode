class Solution:
  def minimizeMax(self, nums: list[int], p: int) -> int:
    nums.sort()

    def numPairs(maxDiff: int) -> int:
      pairs = 0
      i = 1
      while i < len(nums):
        if nums[i] - nums[i - 1] <= maxDiff:
          pairs += 1
          i += 2
        else:
          i += 1
      return pairs

    return bisect.bisect_left(range(nums[-1] - nums[0]), p, key=numPairs)