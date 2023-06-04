class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        l1 = len(word1)
        l2 = len(word2)
        i,j = 0,0
        while i<l1 and j<l2:
            merged += word1[i]
            merged += word2[j]
            i+=1
            j+=1
        merged += word1[i:]
        merged += word2[j:]
        return merged
