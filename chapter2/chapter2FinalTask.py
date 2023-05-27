# 2.5

class Animal:
    """
    Represents an animal in the zoo.
    """
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """
        Initializes an instance of the Animal class.
        :param name: The name of the animal.
        :type name: str
        :param hunger: The hunger level of the animal (default is 0).
        :type hunger: int
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        Returns the name of the animal.
        :return: The name of the animal.
        :rtype: str
        """
        return self._name

    def is_hungry(self):
        """
        Checks if the animal is hungry.
        :return: True if the animal is hungry, False otherwise.
        :rtype: bool
        """
        return self._hunger > 0

    def feed(self):
        """
        Reduces the hunger level of the animal by 1.
        """
        self._hunger -= 1

    def talk(self):
        """
        Represents the sound of the animal.
        This method needs to be implemented in the subclasses.
        """
        pass


class Dog(Animal):
    """
    Represents a dog, a subclass of Animal.
    """
    def talk(self):
        """
        Prints the sound of a dog ("woof woof").
        """
        print("woof woof")

    def fetch_stick(self):
        """
        Prints "There you go, sir!" representing the action of a dog fetching a stick.
        """
        print("There you go, sir!")


class Cat(Animal):
    """
    Represents a cat, a subclass of Animal.
    """
    def talk(self):
        """
        Prints the sound of a cat ("meow").
        """
        print("meow")

    def chase_laser(self):
        """
        Prints "Meeeeow" representing the action of a cat chasing a laser.
        """
        print("Meeeeow")


class Skunk(Animal):
    """
    Represents a skunk, a subclass of Animal.
    """
    def __init__(self, name, hunger=0, stink_count=6):
        """
        Initializes an instance of the Skunk class.
        :param name: The name of the skunk.
        :type name: str
        :param hunger: The hunger level of the skunk (default is 0).
        :type hunger: int
        :param stink_count: The stink count of the skunk (default is 6).
        :type stink_count: int
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """
        Prints the sound of a skunk ("tsssss").
        """
        print("tsssss")

    def stink(self):
        """
        Prints "Dear lord" representing the action of a skunk releasing a strong smell (stink).
        """
        print("Dear lord")


class Unicorn(Animal):
    """
    Represents a unicorn, a subclass of Animal.
    """
    def talk(self):
        """
        Prints the sound of a unicorn ("Good day, darling").
        """
        print("Good day, darling")

    def sing(self):
        """
        Prints "I’m not your toy..." representing the action of a unicorn singing
        (should be the power of a unicorn in my opinion).
        """
        print("I’m not your toy...")


class Dragon(Animal):
    """
    Represents a dragon, a subclass of Animal.
    """
    def __init__(self, name, hunger=0, color="Green"):
        """
        Initializes an instance of the Dragon class.
        :param name: The name of the dragon.
        :type name: str
        :param hunger: The hunger level of the dragon (default is 0).
        :type hunger: int
        :param color: The color of the dragon (default is "Green").
        :type color: str
        """
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """
        Prints the sound of a dragon ("Raaaawr").
        """
        print("Raaaawr")

    def breath_fire(self):
        """
        Prints "$@#$#@$" representing the action of a dragon breathing fire.
        """
        print("$@#$#@$")


def main():
    # Creating animals
    dog1 = Dog("Brownie", 10)
    cat1 = Cat("Zelda", 3)
    skunk1 = Skunk("Stinky")
    unicorn1 = Unicorn("Keith", 7)
    dragon1 = Dragon("Lizzy", 1450)
    dog2 = Dog("Doggo", 80)
    cat2 = Cat("Kitty", 80)
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn2 = Unicorn("Clair", 80)
    dragon2 = Dragon("McFly", 80)
    # Putting the animals in a list
    zoo_lst = [dog1, cat1, skunk1, unicorn1, dragon1, dog2, cat2, skunk2, unicorn2, dragon2]
    for animal in zoo_lst:
        # If the animal is hungry, printing the type, name and feeding until not hungry anymore
        if animal.is_hungry():
            print(type(animal).__name__, animal.get_name())
            while animal.is_hungry():
                animal.feed()
        # Each animal talks (differently)
        animal.talk()
        # Doing a specific thing for each animal type
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
    # Printing the zoo name
    print(Animal.zoo_name)


if __name__ == '__main__':
    main()
