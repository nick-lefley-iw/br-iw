class Round:
    def __init__(self):
        self.id = None
        self.drinks = {}
        self.brewer = None

    def to_json(self):
        drinks_round = self
        if drinks_round.brewer:
            brewer = drinks_round.brewer
            brewer.name = brewer.name.title()
            if brewer.preference:
                brewer.preference = brewer.preference.__dict__
            drinks_round.brewer = brewer.__dict__
        drinks = []
        for drink in drinks_round.drinks.values():
            if drink["drink"]:
                drink["drink"].name = drink["drink"].name.title()
                drink["drink"] = drink["drink"].__dict__
                drink["drink"]["quantity"] = len(drink["team_members"])
            team_members = drink["team_members"]
            drink["team_members"] = []
            for team_member in team_members:
                team_member.name = team_member.name.title()
                if team_member.preference:
                    team_member.preference.name = team_member.preference.name.title()
                    team_member.preference = team_member.preference.__dict__
                drink["team_members"] += [team_member.__dict__]
            drinks.append(drink)
        drinks_round.drinks = drinks
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
