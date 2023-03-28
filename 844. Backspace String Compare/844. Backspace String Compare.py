class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        Stack1 = ""
        Stack2 = ""

        for i in s:
            if i == "#":
                Stack1 = Stack1[:-1]
            else:
                Stack1 = Stack1 + i
        
        for j in t:
            if j == "#":
                Stack2 = Stack2[:-1]
            else:
                Stack2 = Stack2 + j
        
        if len(Stack1)==len(Stack2):
            if Stack1 == Stack2:
                return True
            else:
                return False
        else:
            return False