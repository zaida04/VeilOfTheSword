from util.input import get_option, prompt_option, ChoiceError

class Shop():
    def __init__(self, parent_town, shop_name, shop_keeper_name):
        self.town = parent_town
        self.shop_name = shop_name
        self.shopkeeper = shop_keeper_name
        self.inventory = {}
    def generate_item(self):
        pass
    def get_inventory(self):
        return self.inventory
    def exit(self):
        return self.town.wander()
    def enter(self):
        print(f"\nWelcome to the {self.shop_name}! The shopkeeper's name is {self.shopkeeper}")
        options = {
            1: "Buy an Item",
            2: "Exit"
        }

        prompt_option(options)
        choice = None
        while choice == None:
            try:
                choice = get_option(1, 2, input("What is your choice?: "))
            except ChoiceError:
                choice = None

        def one():
            pass
        def two():
            self.exit()

        switcher = {
            1: one,
            2: two
        }

        option_func = switcher.get(choice)
        option_func()
        self.exit()
