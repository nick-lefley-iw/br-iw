class Teams:
    teams = {}

    def add_team(self, team):
        self.teams[team.id] = team

    def get_team_names(self):
        names = []
        for team in self.teams.values():
            names.append(team.name)
        return names

    def get_password(self, name):
        for team in self.teams.values():
            if name == team.name:
                return team.password
        raise ValueError("Team Does Not Exist")

    def get_team(self, team_id):
        if team_id in self.teams.keys():
            return self.teams[team_id]
        raise ValueError("Team Does Not Exist")

    def clear_teams(self):
        self.teams = {}


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


class TeamMembers:
    team_members = {}

    def add_team_member(self, team_member):
        self.team_members[team_member.id] = team_member

    def get_team_member_names(self):
        names = []
        for person in self.team_members.values():
            names.append(person.name)
        return names

    def get_ids(self):
        return self.team_members.keys()

    def get_team_member(self, team_member_id):
        if team_member_id in self.team_members.keys():
            return self.team_members[team_member_id]
        raise ValueError("Team Member Does Not Exist")

    def clear_team_members(self):
        self.team_members = {}


drinks = Drinks()
team_members = TeamMembers()
teams = Teams()


class Round:
    def __init__(self):
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

    def get_brewer(self):
        return team_members.get_team_member(self.brewer).get_name()

    def update_brewer(self, team_member_id):
        self.brewer = team_member_id

    def clear_order(self):
        self.drinks = {}
        self.brewer = None


drinks_round = Round()


class Team:
    def __init__(self, name, password, team_id):
        self.id = team_id
        self.name = name
        self.password = password

    def update_password(self, password):
        self.password = password


class Drink:
    def __init__(self, name, largest_drink_id, drink_id=None):
        self.id = drink_id if drink_id else (1 if len(drinks.get_ids()) == 0 else largest_drink_id + 1)
        self.name = name

    def get_name(self):
        return self.name.title()


class TeamMember:
    def __init__(self, name, preference, team_members, largest_team_member_id, team_member_id=None):
        self.id = team_member_id if team_member_id else (
            1 if len(team_members.get_ids()) == 0 else largest_team_member_id + 1)
        self.name = name
        self.preference = preference

    def get_preference(self):
        return drinks.get_drink(self.preference).get_name()

    def get_name(self):
        return self.name.title()

    def update_preference(self, preference):
        self.preference = preference
