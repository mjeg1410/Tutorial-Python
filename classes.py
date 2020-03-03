class Bird:
    fly = True

    def noise(self):
        print("Birdnoise")

    babies = 0

    def reproduce(self):
        self.babies += 1

    def eat(self):
        pass

    extinct = False
class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self):
        print("Peck Peck")
Mort = Owl()
Mort.eat()
Mort.reproduce()
print (Mort.babies)