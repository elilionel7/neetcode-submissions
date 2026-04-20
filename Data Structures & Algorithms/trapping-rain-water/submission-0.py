class Solution:
    def trap(self, h: List[int]) -> int:
        l,lm,rm,r,=0,0,0,len(h)-1
        w=0
        while l<r:
            if h[l] <= h[r]:
                if h[l] >= lm:
                    lm = h[l]
                else:
                    w += lm - h[l]
                l += 1
            else:
                if h[r] >= rm:
                    rm = h[r]
                else:
                    w += rm - h[r]
                r -= 1
        return w
        