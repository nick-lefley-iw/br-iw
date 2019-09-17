import unittest
from Source.classes import *


class ClassTests(unittest.TestCase):

    # team
    def test_update_team_password(self):
        team = Team("test", "password", 1)
        team.update_password("new_password")
        self.assertEqual(team.password, "new_password")

    # drink
    def test_get_drink_name(self):
        drink = Drink("coffee", 0)
        self.assertEqual(drink.get_name(), "Coffee")

    def test_create_first_drink_id(self):
        drink = Drink("coffee", 0)
        self.assertEqual(drink.id, 1)

    def test_create_new_drink_id(self):
        drink = Drink("coffee", 0)
        drinks.add_drink(drink)
        new_drink = Drink("tea", 1)
        self.assertEqual(new_drink.id, 2)
        drinks.clear_drinks()

    # team member
    def test_get_team_member_name(self):
        team_member = TeamMember("john smith", 1, 0)
        self.assertEqual(team_member.get_name(), "John Smith")

    def test_get_team_member_preference(self):
        drink = Drink("coffee", 0)
        drinks.add_drink(drink)
        team_member = TeamMember("john smith", 1, 0)
        self.assertEqual(team_member.get_preference(), "Coffee")
        drinks.clear_drinks()

    def test_update_team_member_preference(self):
        team_member = TeamMember("john smith", 1, 0)
        team_member.update_preference(2)
        self.assertEqual(team_member.preference, 2)

    def test_create_first_team_member_id(self):
        team_member = TeamMember("john smith", 1, 0)
        self.assertEqual(team_member.id, 1)

    def test_create_new_team_member_id(self):
        team_member = TeamMember("john smith", 1, 0)
        team_members.add_team_member(team_member)
        new_team_member = TeamMember("mary smith", 1, 1)
        self.assertEqual(new_team_member.id, 2)
        team_members.clear_team_members()

    # teams
    def test_add_team(self):
        team = Team("test", "password", 1)
        teams.add_team(team)
        self.assertDictEqual(teams.teams, {1: team})
        teams.clear_teams()

    def test_get_team_names(self):
        teams.add_team(Team("test1", "password1", 1))
        teams.add_team(Team("test2", "password2", 2))
        teams.add_team(Team("test3", "password3", 3))
        self.assertListEqual(teams.get_team_names(), ["test1", "test2", "test3"])
        teams.clear_teams()

    def test_get_team_password(self):
        teams.add_team(Team("test1", "password1", 1))
        teams.add_team(Team("test2", "password2", 2))
        teams.add_team(Team("test3", "password3", 3))
        self.assertEqual(teams.get_password("test2"), "password2")
        teams.clear_teams()

    def test_cannot_get_team_password(self):
        teams.add_team(Team("test1", "password1", 1))
        teams.add_team(Team("test2", "password2", 2))
        teams.add_team(Team("test3", "password3", 3))
        with self.assertRaises(ValueError):
            teams.get_password("test4")
        teams.clear_teams()

    def test_get_team(self):
        team = Team("test2", "password2", 2)
        teams.add_team(Team("test1", "password1", 1))
        teams.add_team(team)
        teams.add_team(Team("test3", "password3", 3))
        self.assertEqual(teams.get_team(2), team)
        teams.clear_teams()

    def test_cannot_get_team(self):
        teams.add_team(Team("test1", "password1", 1))
        teams.add_team(Team("test2", "password2", 2))
        teams.add_team(Team("test3", "password3", 3))
        with self.assertRaises(ValueError):
            teams.get_team(4)
        teams.clear_teams()

    def test_clear_teams(self):
        teams.add_team(Team("test1", "password1", 1))
        teams.add_team(Team("test2", "password2", 2))
        teams.add_team(Team("test3", "password3", 3))
        teams.clear_teams()
        self.assertDictEqual(teams.teams, {})

    # drinks
    def test_add_drink(self):
        drink = Drink("coffee", 0)
        drinks.add_drink(drink)
        self.assertDictEqual(drinks.drinks, {1: drink})
        drinks.clear_drinks()

    def test_get_drink_names(self):
        drinks.add_drink(Drink("coffee", 0))
        drinks.add_drink(Drink("tea", 1))
        drinks.add_drink(Drink("water", 2))
        self.assertListEqual(drinks.get_drinks_names(), ["coffee", "tea", "water"])
        drinks.clear_drinks()

    def test_get_drink_ids(self):
        drinks.add_drink(Drink("coffee", 0))
        drinks.add_drink(Drink("tea", 1))
        drinks.add_drink(Drink("water", 2))
        self.assertListEqual(list(drinks.get_ids()), [1, 2, 3])
        drinks.clear_drinks()

    def test_get_drink(self):
        drinks.add_drink(Drink("coffee", 0))
        drink = Drink("tea", 1)
        drinks.add_drink(drink)
        drinks.add_drink(Drink("water", 2))
        self.assertEqual(drinks.get_drink(2), drink)
        drinks.clear_drinks()

    def test_cannot_get_drink(self):
        drinks.add_drink(Drink("coffee", 0))
        drinks.add_drink(Drink("tea", 1))
        drinks.add_drink(Drink("water", 2))
        with self.assertRaises(ValueError):
            drinks.get_drink(4)
        drinks.clear_drinks()

    def test_clear_drinks(self):
        drinks.add_drink(Drink("coffee", 0))
        drinks.add_drink(Drink("tea", 1))
        drinks.add_drink(Drink("water", 2))
        drinks.clear_drinks()
        self.assertDictEqual(drinks.drinks, {})

    # team members
    def test_add_team_member(self):
        team_member = TeamMember("john smith", 1, 0)
        team_members.add_team_member(team_member)
        self.assertDictEqual(team_members.team_members, {1: team_member})
        team_members.clear_team_members()

    def test_get_team_member_names(self):
        team_members.add_team_member(TeamMember("john smith", 1, 0))
        team_members.add_team_member(TeamMember("mary smith", 1, 1))
        team_members.add_team_member(TeamMember("steve smith", 1, 2))
        self.assertListEqual(team_members.get_team_member_names(), ["john smith", "mary smith", "steve smith"])
        team_members.clear_team_members()

    def test_get_team_member_ids(self):
        team_members.add_team_member(TeamMember("john smith", 1, 0))
        team_members.add_team_member(TeamMember("mary smith", 1, 1))
        team_members.add_team_member(TeamMember("steve smith", 1, 2))
        self.assertListEqual(list(team_members.get_ids()), [1, 2, 3])
        team_members.clear_team_members()

    def test_get_team_member(self):
        team_members.add_team_member(TeamMember("john smith", 1, 0))
        team_member = TeamMember("mary smith", 1, 1)
        team_members.add_team_member(team_member)
        team_members.add_team_member(TeamMember("steve smith", 1, 2))
        self.assertEqual(team_members.get_team_member(2), team_member)
        team_members.clear_team_members()

    def test_cannot_get_team_member(self):
        team_members.add_team_member(TeamMember("john smith", 1, 0))
        team_members.add_team_member(TeamMember("mary smith", 1, 1))
        team_members.add_team_member(TeamMember("steve smith", 1, 2))
        with self.assertRaises(ValueError):
            team_members.get_team_member(4)
        team_members.clear_team_members()

    def test_clear_team_members(self):
        team_members.add_team_member(TeamMember("john smith", 1, 0))
        team_members.add_team_member(TeamMember("mary smith", 1, 1))
        team_members.add_team_member(TeamMember("steve smith", 1, 2))
        team_members.clear_team_members()
        self.assertDictEqual(team_members.team_members, {})

    # round
    def test_add_new_drink_to_round(self):
        drinks_round.add_drink(1, 1)
        self.assertDictEqual(drinks_round.drinks, {1: [1]})
        drinks_round.clear_order()

    def test_add_drink_to_round(self):
        drinks_round.add_drink(1, 1)
        self.assertDictEqual(drinks_round.drinks, {1: [1]})
        drinks_round.add_drink(1, 2)
        self.assertDictEqual(drinks_round.drinks, {1: [1, 2]})
        drinks_round.clear_order()

    def test_does_not_add_drink_to_round(self):
        drinks_round.add_drink(1, 1)
        self.assertDictEqual(drinks_round.drinks, {1: [1]})
        drinks_round.add_drink(1, 1)
        self.assertDictEqual(drinks_round.drinks, {1: [1]})
        drinks_round.clear_order()

    def test_get_drinks_in_order(self):
        drinks_round.add_drink(1, 1)
        drinks_round.add_drink(1, 2)
        drinks_round.add_drink(2, 3)
        self.assertListEqual(list(drinks_round.get_drinks_in_order()), [1, 2])
        drinks_round.clear_order()

    def test_get_brewer(self):
        team_members.add_team_member(TeamMember("john smith", 1, 0))
        drinks_round.update_brewer(1)
        self.assertEqual(drinks_round.get_brewer(), "John Smith")
        team_members.clear_team_members()
        drinks_round.clear_order()

    def update_brewer(self):
        drinks_round.update_brewer(1)
        self.assertEqual(drinks_round.brewer, 1)
        drinks_round.clear_order()

    def test_clear_order(self):
        drinks_round.add_drink(1, 1)
        drinks_round.add_drink(1, 2)
        drinks_round.update_brewer(1)
        drinks_round.clear_order()
        self.assertDictEqual(drinks_round.drinks, {})


if __name__ == "__main__":
    unittest.main()
