class Employee:

    def __init__(self, fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def greet_person(self):
        print("Hello Welcome to eox " +self.fname)

emp1 = Employee('Prathi','B Raj','prathi@eox.com')
emp2 = Employee('sony', 'kp', 'sony@eox.com')
print(emp1.fname)
emp2.greet_person()


     # def __init__(self, fname, lname, email):
#         self.fname = fname
#         self.lname = lname
#         self.email = email
#
#      def greet_person(self):
#          print("Hello, Welcome to RCV Academy " +self.fname)
#
# emp1 = Employee('Prathiksha','B Raj', "prathikshar@eoxvantage.com")
# emp2 = Employee('Ram','Raj',"raj@eox.com")
# print(emp1.lname)
# print(emp2.fname)
#
# emp1.greet_person()
# emp2.greet_person()


