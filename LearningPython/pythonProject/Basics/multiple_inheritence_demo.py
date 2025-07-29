# class Movecharacter():
#     def move_fwd(self):
#         print("Move forward 1 step")
#
#     def move_bwd(self):
#         print("Move backward 1 step")
#
# class Jumpcharacter():
#     def Jump_1level(self):
#         print("Jump Character 1 level")
#
#     def Jump_2level(self):
#         print("Jump Character 2 level")
#
# class Pokemon(Movecharacter,Jumpcharacter):
#     def move_bwd(self):
#         print("pokemon moving")
# p = Pokemon()
# p.move_fwd()
# p.Jump_1level()
# print(Pokemon.mro())
#
#
# class Mickey(Movecharacter,Jumpcharacter):
#     pass
# m = Mickey()
# m.move_fwd()
# m.Jump_2level()


class Movecharacter:
    def move_fwd(self):
        print("Character moving forward")

class Jumpcharacter:
    def Jump_1level(self):
        print("Jump Character 1 level")

    def Jump_2level(self):
        print("Jump Character 2 level")

class Pokemon(Movecharacter, Jumpcharacter):
    def move_bwd(self):
        print("pokemon moving")

p = Pokemon()
p.move_bwd()
p.Jump_2level()
print(Pokemon.mro())

# class Mickey(Movecharacter, Jumpcharacter):
#     pass
#
# m = Mickey()
# m.move_fwd()
# m.Jump_2level()
