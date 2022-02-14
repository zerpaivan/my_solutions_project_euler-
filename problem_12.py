class Problem_12():

    def triangleNumber(self, place_number):
        self.place_number = place_number
        self.t_number = sum(range(1, self.place_number + 1))
        return self.t_number

    def prime_factors(self, number):
        prime_flist = []
        factor = 2
        self.number = number

        while self.number >= factor:
            if self.number % factor == 0:
                prime_flist.append(factor)
                self.number = self.number // factor
            else:
                factor = factor + 1

        return prime_flist

    # def numbers_of_dividers(self):
    #     p_factors = self.prime_factors()
    #     primes_base = list(set(p_factors))
    #     ns = []
    #     for prime in primes_base:  # without repeated elements
    #         ns.append(p_factors.count(prime))
    #     nod = 1
    #     for i in ns:
    #         nod = nod * (1+i)
    #     return nod

    def dividers(self, number):
        p_factors = self.prime_factors(number)
        primes_base = list(set(p_factors))
        ns = []
        monomials = []
        for prime in primes_base:  # without repeated elements
            ns.append(p_factors.count(prime))

        for i in range(len(primes_base)):
            m = []
            for n in range(ns[i] + 1):
                m.append((primes_base[i] ** n))
            monomials.append(m)

        if monomials == []:
            monomials = [[]]
# --------------------------------------------------------------------------
        temp_list = []
        list_i = monomials[0]
        for e, list_j in enumerate(monomials[1:]):
            for i in list_i:
                for j in list_j:
                    temp_list.append(i * j)
            list_i = temp_list[:]
            temp_list = []
        return sorted(list_i)


def main():
    place_num = 0
    num_div = 0
    sol = Problem_12()
    while num_div < 500:
        tn = sol.triangleNumber(place_num)
        num_div = len(sol.dividers(tn))
        place_num = place_num + 1
    return num_div, place_num - 1, tn


print(main())
