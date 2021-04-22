
class Dice():
    def __init__(self, color, sides):
        self.color = color
        self.sides = sides
        self.current_side = 1               #kezdőoldal (1től indul minden kocka)
        self.__rolled_values = []           #itt pl gyűjthetjük a már dobott számokat, és csekkolhatja h már volt-e


    def roll(self):                         #metódus, ahogy használni akarjuk pl. a kockát
        import random                       #lokálisan importálom, hogy ne akadjon össze esetleg mással
        self.current_side = random.randint(1,self.sides)


    def __str__(self):                                          #akkor kell, ha kiprintelem az osztályt
        return f"Color: {self.color}\t\tSides: {self.sides}"    #igy: print(d6)

d6 = Dice("white", 6)
d20 = Dice("blue", 20)

import time
for _ in range(20):
    d20.roll()
    print(d20.current_side)
    time.sleep(1)