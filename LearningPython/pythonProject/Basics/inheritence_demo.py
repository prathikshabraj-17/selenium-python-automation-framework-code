class ParentClass:
    def __init__(self):
        print("Parent Class instance")

    def parent_method(self):
        print("Parents money")

class Childclass(ParentClass):
    pass

p = ParentClass()
p.parent_method()