class Arearect:

    def __init__(self,l,b):
        self.l = l
        self.b = b

    def calculate_area(self):
        return self.l * self.b

area1 = Arearect(14,8)
area2 = Arearect(88,55)
print(area1.calculate_area())
print(area2.calculate_area())

