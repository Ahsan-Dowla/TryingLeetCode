class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        place = 1
        s = 0

        while n:
            digit = n % 10
            s += digit
            if digit:
                x += digit * place
                place *= 10
            n //= 10

        return x * s