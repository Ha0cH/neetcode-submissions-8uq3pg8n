class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valKey = {}
        for i in range (len(nums)):
            d = target - nums[i]
            if d in valKey:
                return [valKey[d], i]
            valKey[nums[i]] = i
        
        return []