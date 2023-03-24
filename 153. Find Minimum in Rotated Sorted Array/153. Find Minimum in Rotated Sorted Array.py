class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if (r+1)==1:
            return nums[0]
        elif (r+2)==2:
            if nums[0]<nums[1]:
                return nums[0]
            else:
                return nums[1]
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[r]>nums[mid]:
                r = mid - 1
            else:
                l = mid