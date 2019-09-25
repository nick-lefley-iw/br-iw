class Teams:
    teams = {}
    current_team_id = None
    current_team_name = None
    current_team_password = None

    def add_team(self, team):
        self.teams[team.id] = team

    def get_team_names(self):
        names = []
        for team in self.teams.values():
            names.append(team.name)
        return names

    def get_team(self, team_id):
        if team_id in self.teams.keys():
            return self.teams[team_id]
        raise ValueError("Team Does Not Exist")

    def update_current_team(self, team_name):
        for key, team in self.teams.items():
            if team_name.lower() == team.name.lower():
                self.current_team_name = team_name.title()
                self.current_team_id = key
                self.current_team_password = team.password
                return
        raise ValueError("Team Does Not Exist")

    def logout_team(self):
        self.current_team_password = None
        self.current_team_name = None
        self.current_team_id = None

    def clear_teams(self):
        self.logout_team()
        self.teams = {}
