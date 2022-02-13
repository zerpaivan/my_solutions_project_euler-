class Problem_12():
    def __init__(self, place_number):
        self.place_number = place_number

    def triangleNumber(self):
        # self.t_number = 0
        self.t_number = sum(range(1, self.place_number + 1))
        return self.t_number

    def prime_factors(self):
        prime_flist = []
        factor = 2
        self.number = self.triangleNumber()
        while self.number >= factor:
            if self.number % factor == 0:
                # print(self.number, factor)
                prime_flist.append(factor)
                self.number = self.number // factor
            else:
                factor = factor + 1

        return prime_flist

    def numbers_of_dividers(self):
        p_factors = self.prime_factors()
        primes = list(set(p_factors))
        ns = []
        for prime in primes:  # without repeated elements
            ns.append(p_factors.count(prime))
        nod = 1
        for i in ns:
            nod = nod * (1+i)
        return nod

    def dividers(self):
        p_factors = self.prime_factors()
        primes = list(set(p_factors))
        ns = []
        x = []
        for prime in primes:  # without repeated elements
            ns.append(p_factors.count(prime))
        for e, p in enumerate(primes):
            m = []
            for n in range(ns[e] + 1):
                m.append((p ** n))
                # print(m)
            x.append(m)
        # print(x)
        result = []
        for e, i in enumerate(x[:-1]):
            for j in i:
                for k in x[e + 1:]:
                    for l in k:
                        result.append(j * l)
        return sorted(result)


def main():
    place_num = 1
    num_div = 0
    while True:
        sol = Problem_12(place_num)
        num_div = len(sol.dividers())
        if num_div < 150:
            place_num = place_num + 1
        else:
            tn = sol.t_number
            break
    return num_div, place_num, tn

print(main())
# obj1 = Problem_12(7)
# print(obj1.triangleNumber())
# print(obj1.prime_factors())
# print(obj1.numbers_of_dividers())
