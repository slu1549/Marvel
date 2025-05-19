

# OOPs

class Human:
    superpower = []
    avengers = []
    herocount = 0
    # constructor    
    def __init__(self, name, age, power, homeworld, bodycount):

        # These are the attributes of an object

        self.name = name
        self.age = age
        self.power = power
        self.homeworld = homeworld
        self.bodycount = bodycount

        Human.herocount += 1
        Human.superpower.append(self.power)
        Human.avengers.append(self.name)


    def planet(self):
        print(self.name, f"is from planet {self.homeworld}!")

    def kills(self):
        print(f"This hero has defeated {self.bodycount} enemies!")

    def newadd(self):
        print(f"{self.name} has joined the Avengers!")


class Thunderbolts(Human):
    #re initiate the constructor
    def __init__(self, name, age, superpower, affiliate):
        super().__init__(name, age, power)
        self.affiliate = affiliate

    def friend(self):
        print(f"{name} is friends with {affiliate}")

Bucky = Thunderbolts("Bucky", 80, "SSS", "Steve Rogers")
                     
Bucky.friend()
                    

Thor = Human("Thor", 1500, "flight", "Asgard", 40)
Thor.planet()
Thor.kills()

Ironman = Human("Iron Man", 42, "Repulsor beams", "Earth", 16)



print(Human.superpower)
Ironman.newadd()
print(Human.avengers)



