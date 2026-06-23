class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        j= 1
        if len(nums)%2 == 0:
            while j <= len(nums)-1 and i <= len(nums)-1:
                if nums[i]!=nums[j]:
                    return nums[i]
                i+=2
                j+=2
        else:
            while j <= len(nums)-1 and i <= len(nums)-1:
                if nums[i]!=nums[j]:
                    return nums[i]
                i+=2
                j+=2
            return nums[i]
