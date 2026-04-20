class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        cntT, win = {},{}

        for c in t:
            cntT[c] = 1 + cntT.get(c,0)
        
        have, need, = 0, len(cntT)
        res, rl = [-1,-1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            win[c] = 1 + win.get(c,0)

            if c in cntT and win[c] == cntT[c]:
                have += 1

            while have == need:
                if (r-l+1) < rl:
                    res = [l,r]
                    rl = r-l+1
                win[s[l]] -= 1
                if s[l] in cntT and win[s[l]] < cntT[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l:r+1] if rl != float('inf') else ""


        