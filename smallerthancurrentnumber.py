class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count= []

        for i in range(0, len(nums)):
            small=0
            for j in range(0, len(nums)):
                if (nums[j]<nums[i]):
                    small=small+1
            count.append(small)
        return count
