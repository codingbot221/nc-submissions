class Solution:
    def twoSum(self, nums: List[int], tar: int) -> List[int]:
      seen={}
      for i in range(len(nums)):
        c=tar-nums[i]
        if c in seen:
          return [seen[c],i]
        seen[nums[i]]=i