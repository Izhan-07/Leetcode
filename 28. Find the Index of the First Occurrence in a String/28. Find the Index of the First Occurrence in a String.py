class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # A brute force approach-> traverse through all the element in haystack from index
        # 0 to (n-len(needle)+1 , where n is the len of haystack)
        for i in range(len(haystack)-len(needle)+1):
            # this check index starting from 0 to 0+len(needle)
            # this will check like this: 
            # sad == sad, adb==sad, dbu==sad, but==sad.... so on
            if haystack[i:i+len(needle)] == needle:
                return i # to return the index of first occurence
        return -1 # if not part of haystack