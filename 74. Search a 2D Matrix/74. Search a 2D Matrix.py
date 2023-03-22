class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We will apply Binary search to get the target array in which we will again apply binary search to check target value present in the list or not.
        def BinarySearch(arr, target):
            l = 0 
            r = len(arr)-1 
            while l<=r:
                mid = l + (r-l)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        s = 0 # start value
        t = len(matrix)-1 # end value
        while s<=t:
            mid_mat = s + (t-s)//2 #mid value
            if BinarySearch(matrix[mid_mat], target):
                return True # returns true if target value found in the mid matrix
            elif matrix[mid_mat][0]<target:
                s = mid_mat + 1
            else:
                t = mid_mat - 1
        return False