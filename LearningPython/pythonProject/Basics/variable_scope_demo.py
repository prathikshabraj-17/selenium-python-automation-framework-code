# Variables scope in python - boundary of variable within a program
# Local scope
# Global scope
# Global Keyword
# LEGB Rule - Local -> Enclosing -> Gloabl -> Built-in ->

# Local scope
def var_scope_demo():
    x = 20
    print(x)


#Global scope
# x = 30
# def var_scope_demo():
#     print(x)
#
# def var_scope_demo1():
#     print(x)

# var_scope_demo()
# var_scope_demo1()

#global keyword
# x = 30
# def var_scope_demo():
#     global x
#     x = 60
#     print(x)
#
# def var_scope_demo1():
#     print(x)
#
#

# LEGB Rule

x = 100
def var_scope_demo():
    x = 20
    print(x)
    def var_scope_demo1():
        x = 50
        print(x)
        def var_scope_demo2():
          print(x)
        def grand_child():
           x = 70
           print(x)
        grand_child()
    var_scope_demo1()
#
var_scope_demo()