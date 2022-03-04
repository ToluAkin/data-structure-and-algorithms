def gcd(m, n):
    def divisor(divisor):
        cleanDivisionM = m / divisor
        cleanDivisionN = n / divisor

        if cleanDivisionM.is_integer() and cleanDivisionN.is_integer():
            return divisor
    
    value = 2
    while divisor(value) == None:
        value += 1
    return value
print(gcd(6, 12))