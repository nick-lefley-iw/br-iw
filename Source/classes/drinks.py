class Drinks:
    drinks = {}

    def add_drink(self, drink):
        self.drinks[drink.id] = drink

    def get_drinks_names(self):
        names = []
        for drink in self.drinks.values():
            names.append(drink.name)
        return names

    def get_ids(self):
        return self.drinks.keys()

    def get_drink(self, drink_id):
        if drink_id in self.drinks.keys():
            return self.drinks[drink_id]
        raise ValueError("Drink Does Not Exist")

    def clear_drinks(self):
        self.drinks = {}
