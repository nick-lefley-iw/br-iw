class Drink:
    def __init__(self, name, drink_id):
        self.id = drink_id
        self.name = name

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.id == other.id and self.name == other.name
        return False

    def get_name(self):
        return self.name.title()
