class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        c1, c2, c = 0, 0, 0
        if dividend < 0:
            c1 = -1
        else:
            c1 = 1
        if divisor < 0:
            c2 = -1
        else:
            c2 = 1
        c = c1 * c2
        dividend *= c1
        divisor *= c2
        q = dividend//divisor
        
        if c == 1 and q > 2**31 -1:
            return 2**31 -1
        elif c == -1 and q > 2**31:
            return 2**31
        return c*q