class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fr = self.firstoccurence(nums, target)
        la = self.lastoccurence(nums, target)
        return [fr, la]
    
    def firstoccurence(self, arr1, target):
        l = 0
        r = len(arr1)-1
        while l<=r:
            mid = l + (r-l)//2
            # We will start with the middle element of the array and check if it is equal to the target value. If it is, then we check if the element before it is less than the target value or not. If it is less than the target value or if the middle element is the first element of the array, then we have found the first occurrence of the target value.
            
            if  (mid == 0 or arr1[mid-1] < target) and arr1[mid] == target:
                return mid

            elif arr1[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        return -1
        
    def lastoccurence(self, arr2, target):
        l = 0
        r = len(arr2)-1
        while l<=r:
            mid = l + (r-l)//2
            # We will start with the middle element of the array and check if it is equal to the target value. If it is, then we check if the element after it is greater than the target value or not. If it is greater than the target value or if the middle element is the last element of the array, then we have found the last occurrence of the target value.
            
            if (mid == r or arr2[mid+1] > target) and arr2[mid] == target:
                return mid
            elif target < arr2[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
