class Problem_12():
    def __init__(self, place_number):
        self.place_number = place_number

    def triangleNumber(self):  # by resursion
        if self.place_number == 1:
            return 1
        else:
            return self.place_number +\
                   Problem_12(self.place_number - 1).triangleNumber()


obj1 = Problem_12(7)
print(obj1.triangleNumber())
