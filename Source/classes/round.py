class Round:
    def __init__(self):
        self.id = None
        self.drinks = {}
        self.brewer = None

    def to_json(self):
        drinks_round = self
        if drinks_round.brewer:
            brewer = drinks_round.brewer
            if brewer.preference:
                brewer.preference = brewer.preference.__dict__
            drinks_round.brewer = brewer.__dict__
        for drink in drinks_round.drinks.values():
            if drink["drink"]:
                drink["drink"] = drink["drink"].__dict__
            team_members = drink["team_members"]
            drink["team_members"] = []
            for team_member in team_members:
                if team_member.preference:
                    team_member.preference = team_member.preference.__dict__
                drink["team_members"] += [team_member.__dict__]
        return drinks_round.__dict__

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
