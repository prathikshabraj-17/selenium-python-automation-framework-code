class RateofInterest:
    interest = 0.06

    def __init__(self,name,loan):
        self.name = name
        self.loan = loan


    def calc_interest(self):
        print("Total interest: ", self.loan * self.interest)

class Student(RateofInterest):
    pass
#
# s = Student("Prathiksha", 200000)
# s.calc_interest()


p1 = RateofInterest("Prathiksha", 50000)
# p1.interest = 0.02
p1.calc_interest()
#
# p2 = RateofInterest("Prathi", 25000)
# p2.calc_interest()