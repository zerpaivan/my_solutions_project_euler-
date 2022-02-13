class Problem_12():
    def __init__(self, place_number):
        self.place_number = place_number

    def triangleNumber(self):
        self.t_number = 0
        for i in range(1, self.place_number + 1):
            self.t_number = self.t_number + i

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
            # print(self.number, factor)
        return prime_flist

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
        print(x)
        result = []
        for e, i in enumerate(x[:-1]):
            for j in i:
                for k in x[e + 1:]:
                    for l in k:
                        result.append(j * l)
        return sorted(result)


# place = 12375


obj1 = Problem_12(7)
print(obj1.triangleNumber())
print(obj1.prime_factors())
print(obj1.dividers())
