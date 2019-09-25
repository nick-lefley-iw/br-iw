class Round:
    def __init__(self):
        self.id = None
        self.drinks = {}
        self.brewer = None

    def add_drink(self, drink_id, team_member_id):
        if drink_id in self.drinks.keys():
            if team_member_id not in self.drinks[drink_id]:
                self.drinks[drink_id] += [team_member_id]
        else:
            self.drinks[drink_id] = [team_member_id]

    def get_drinks_in_order(self):
        return self.drinks.keys()

    def get_brewer(self, team_members):
        return team_members.get_team_member(self.brewer).get_name()

    def update_brewer(self, team_member_id):
        self.brewer = team_member_id

    def update_id(self, round_id):
        self.id = round_id

    def clear_order(self):
        self.drinks = {}
        self.brewer = None
        self.id = None
