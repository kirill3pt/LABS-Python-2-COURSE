class Fraction(object):
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()

    def __str__(self):
        return "%d/%d" % (self.__num, self.__den)

    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num //= g
        self.__den //= g

    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)

    # -frac
    def __neg__(self):
        return Fraction(-self.__num, self.__den)

    # ~frac (переворот дроби)
    def __invert__(self):
        return Fraction(self.__den, self.__num)

    # frac ** n
    def __pow__(self, power):
        return Fraction(self.__num ** power, self.__den ** power)

    # float(frac)
    def __float__(self):
        return self.__num / self.__den

    # int(frac)
    def __int__(self):
        return self.__num // self.__den

def run():
    frac = Fraction(7, 2)

    print(-frac)
    print(~frac)
    print(frac**2)
    print(float(frac))
    print(int(frac))