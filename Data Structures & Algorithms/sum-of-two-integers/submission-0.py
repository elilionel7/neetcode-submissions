class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            aXorb = (a ^ b) & mask

            aAndb =  ((a & b) << 1) & mask

            a,b  = aXorb , aAndb   

        return a if a <= max_int else ~(a ^ mask)