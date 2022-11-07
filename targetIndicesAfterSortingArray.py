class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        #sort
        n=len(nums)
        for i in range (0,n-1):
            for j in range(i+1,n):
                if(nums[j]<nums[i]):
                    nums[j],nums[i]=nums[i],nums[j]
        #find target indices
        output=[]
        for x in range (0,n):
            if(nums[x]==target):
                output.append(x)
        return output
