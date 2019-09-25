class Team:
    def __init__(self, name, password, team_id):
        self.id = team_id
        self.name = name
        self.password = password

    def update_password(self, password):
        self.password = password
