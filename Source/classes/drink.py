class Drink:
    def __init__(self, name, drink_id):
        self.id = drink_id
        self.name = name

    def get_name(self):
        return self.name.title()
