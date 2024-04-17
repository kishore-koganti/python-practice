
anb = 12

anb = anb + 12.5

print((anb))

class person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def printName(self):
        print(self.firstName, self.lastName)

x = person("kish", "kkk")
x.printName()
