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
