class Team:
    def __init__(self, name, password, team_id):
        self.id = team_id
        self.name = name
        self.password = password

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.id == other.id and self.name == other.name and self.password == other.password
        return False

    def update_password(self, password):
        self.password = password
