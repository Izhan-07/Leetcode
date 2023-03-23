class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        a = 0
        l = len(nums)
        if l == 1:
            return 0
        while a<=l:
            mid = a + (l-1-a)//2
            if mid==0:
                if nums[mid]>nums[mid+1]:
                    return mid
                else:
                    return mid+1

            elif mid==l-1:
                if nums[mid]>nums[mid-1]:
                    return mid
                else:
                    return mid-1
            
            else:
                if (nums[mid]>nums[mid+1]) and (nums[mid]>nums[mid-1]):
                    return mid
                elif (nums[mid+1]>nums[mid]):
                    a = mid + 1
                else:
                    l = mid
                
            