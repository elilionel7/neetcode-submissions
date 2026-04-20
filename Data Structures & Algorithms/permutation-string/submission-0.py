class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1cnt, s2cnt = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1cnt[ord(s1[i]) - ord('a')] += 1
            s2cnt[ord(s2[i]) - ord('a')] += 1
        
        same = 0

        for i in range(26):
            same += (1 if s1cnt[i] == s2cnt[i] else 0)

        l = 0

        for r in range(len(s1), len(s2)):
            if same == 26: 
                return True

            idx = ord(s2[r]) - ord('a')
            s2cnt[idx] += 1
            if s1cnt[idx] == s2cnt[idx]:
                same += 1
            elif s1cnt[idx] + 1 == s2cnt[idx]:
                same -= 1
            
            idx = ord(s2[l]) - ord('a')
            if s1cnt[idx] == s2cnt[idx]:
                same -= 1
            s2cnt[idx] -= 1
            if s1cnt[idx] == s2cnt[idx]:
                same += 1

            l += 1
        return same == 26

        