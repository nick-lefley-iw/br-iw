class TeamMember:
    def __init__(self, name, preference, team_member_id):
        self.id = team_member_id
        self.name = name
        self.preference = preference

    def get_preference(self, drinks):
        return drinks.get_drink(self.preference).get_name()

    def get_name(self):
        return self.name.title()

    def update_preference(self, preference):
        self.preference = preference
