import unittest
import sys
sys.path.append("..")
from Source.classes import *


class ClassTests(unittest.TestCase):

    def test_update_team_password(self):
        team = Team("test", "password", 1)
        team.update_password("new_password")
        self.assertEqual(team.password, "new_password")


if __name__ == "__main__":
    unittest.main()