class Round:
    def __init__(self):
        self.id = None
        self.drinks = {}
        self.brewer = None

    def add_drink(self, drink, team_member):
        if drink.id in self.drinks.keys():
            if team_member.id not in self.drinks[drink.id]["team_member_ids"]:
                self.drinks[drink.id]["team_members"] += [team_member]
                self.drinks[drink.id]["team_member_ids"] += [team_member.id]
        else:
            self.drinks[drink.id] = {"drink": drink, "team_members": [team_member], "team_member_ids": [team_member.id]}

    def get_drinks_in_order(self):
        return self.drinks.keys()

    def get_brewer(self):
        return self.brewer.get_name()

    def update_brewer(self, team_member):
        self.brewer = team_member

    def update_id(self, round_id):
        self.id = round_id

    def clear_order(self):
        self.drinks = {}
        self.brewer = None
        self.id = None
