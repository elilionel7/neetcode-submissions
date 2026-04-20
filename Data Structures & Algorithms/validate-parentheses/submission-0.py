class Solution:
    def isValid(self, s: str) -> bool:
        ocp = {")":"(", "}":"{", "]":"["}
        stk = []

        for p in s:
            
            if stk and p in ocp and stk[-1] == ocp[p]:
                stk.pop()
            else:
                stk.append(p)
        return False if stk else True


        