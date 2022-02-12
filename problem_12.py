class Problem_12():
    def __init__(self, place_number):
        self.place_number = place_number
        self.t_number = 0

    def triangleNumber(self):
        for i in range(1, self.place_number + 1):
            self.t_number = self.t_number + i

        return self.t_number

    def prime_factors(self):
        prime_flist = []
        factor = 2
        self.number = self.triangleNumber()
        while self.number > 1:
            if self.number % factor == 0:
                prime_flist.append(factor)
                self.number = self.number // factor
            else:
                factor = factor + 1
        return prime_flist
# place = 12375


obj1 = Problem_12(7)
print(obj1.triangleNumber())
print(obj1.prime_factors())
