

class Movecharacter():
    def move_fwd(self):
        print("Move forward 1 step")

    def move_bwd(self):
        print("Move backward 1 step")

class Pokemon(Movecharacter):
     def move_bwd(self):
        print("pokemon moving")

p = Pokemon()
p.move_fwd()
# p.Jump_1level()
# print(Pokemon.mro())


