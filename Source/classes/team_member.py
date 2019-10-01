class TeamMember:
    def __init__(self, name, preference, team_member_id):
        self.id = team_member_id
        self.name = name
        self.preference = preference

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.id == other.id and self.name == other.name and self.preference == other.preference
        return False

    def to_json(self):
        team_member = self
        if team_member.preference:
            team_member.preference.name = team_member.preference.name.title()
            team_member.preference = team_member.preference.__dict__
        team_member.name = team_member.name.title()
        return team_member.__dict__

    def get_preference(self):
        return self.preference.get_name()

    def get_name(self):
        return self.name.title()

    def update_preference(self, preference):
        self.preference = preference
