class TeamMember:
    def __init__(self, name, preference, team_member_id):
        self.id = team_member_id
        self.name = name
        self.preference = preference

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.id == other.id and self.name == other.name and self.preference == other.preference
        return False

    def get_preference(self):
        return self.preference.get_name()

    def get_name(self):
        return self.name.title()

    def update_preference(self, preference):
        self.preference = preference
