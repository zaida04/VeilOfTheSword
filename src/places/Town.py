from places.Arena import Arena
from places.Shop import Shop
from util.input import get_option, prompt_option, ChoiceError

class Town():
    def __init__(self):
        self.shops = {}
        self.shops["weapon_shop"] = Shop(self, "Weapons Shop", "Overlord")
        self.shops["armour_shop"] = Shop(self, "Armour Shop", "Oliver")
        self.shops["potion_shop"] = Shop(self, "Potion Shop", "Necron")
        self.arena = Arena(self)
    def intro(self):
        return print("Welcome to the Town! Here are your options: ")
    def wander(self):
        options = {
            1: "Enter the weapons shop",
            2: "Enter the armour shop",
            3: "Enter the potions shop"
        }

        prompt_option(options)
        choice = None
        while choice == None:
            try:
                choice = get_option(1, 3, input("What is your choice?: "))
            except ChoiceError:
                choice = None

        def one():
            return self.shops["weapon_shop"].enter()
        def two():
            return self.shops["armour_shop"].enter()
        def three():
            return self.shops["potion_shop"].enter()

        switcher = {
            1: one,
            2: two,
            3: three
        }

        option_func = switcher.get(choice)
        option_func()
