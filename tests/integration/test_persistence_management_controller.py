import unittest
from Source.classes.teams import *
from Source.classes.team_members import *
from Source.classes.drinks import *
from Source.classes.round import *
from unittest.mock import patch
from Source.controllers.persistence_management_controller import *


drinks = Drinks()
team_members = TeamMembers()
teams = Teams()
drinks_round = Round()


class TestStringHelperIntegration(unittest.TestCase):
        @unittest.mock.patch('Source.controllers.persistence_management_controller.select_sql', side_effect=[[(1, "test", "password"), (2, "test_2", "red")]])
        def test_read_team(self, operation):
            read_team(teams)
            operation.assert_called_once_with("SELECT * FROM team", ())
            self.assertDictEqual(teams.teams, {1: Team("test", "password", 1), 2: Team("test_2", "red", 2)})


if __name__ == "__main__":
    unittest.main()
