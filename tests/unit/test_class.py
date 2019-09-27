import unittest
from Source.classes.drink import *
from Source.classes.team_member import *
from Source.classes.team import *
from Source.classes.teams import *
from Source.classes.team_members import *
from Source.classes.drinks import *
from Source.classes.round import *


drinks = Drinks()
team_members = TeamMembers()
teams = Teams()
drinks_round = Round()


class TestClass(unittest.TestCase):

    # team
    def test_update_team_password(self):
        team = Team("test", "password", 1)
        team.update_password("new_password")
        self.assertEqual(team.password, "new_password")

    # drink
    def test_get_drink_name(self):
        drink = Drink("coffee", 1)
        self.assertEqual(drink.get_name(), "Coffee")

    # team member
    def test_get_team_member_name(self):
        team_member = TeamMember("john smith", 1, 1)
        self.assertEqual(team_member.get_name(), "John Smith")

    def test_get_team_member_preference(self):
        drink = Drink("coffee", 1)
        drinks.add_drink(drink)
        team_member = TeamMember("john smith", drink, 1)
        self.assertEqual(team_member.get_preference(), "Coffee")
        drinks.clear_drinks()

    def test_update_team_member_preference(self):
        team_member = TeamMember("john smith", 1, 1)
        drink = Drink("coffee", 1)
        team_member.update_preference(drink)
        self.assertEqual(team_member.preference, drink)

    # teams
    def test_add_team(self):
        teams.clear_teams()
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

    def test_update_current_team(self):
        teams.add_team(Team("test1", "password1", 1))
        teams.add_team(Team("test2", "password2", 2))
        teams.add_team(Team("test3", "password3", 3))
        teams.update_current_team("test2")
        self.assertEqual(teams.current_team_id, 2)
        self.assertEqual(teams.current_team_name, "Test2")
        self.assertEqual(teams.current_team_password, "password2")
        teams.clear_teams()

    def test_cannot_update_current_team(self):
        teams.add_team(Team("test1", "password1", 1))
        teams.add_team(Team("test2", "password2", 2))
        teams.add_team(Team("test3", "password3", 3))
        with self.assertRaises(ValueError):
            teams.update_current_team("test4")
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

    def test_logout_team(self):
        teams.add_team(Team("test1", "password1", 1))
        teams.add_team(Team("test2", "password2", 2))
        teams.add_team(Team("test3", "password3", 3))
        teams.update_current_team("test2")
        teams.logout_team()
        self.assertEqual(teams.current_team_name, None)
        self.assertEqual(teams.current_team_password, None)
        self.assertEqual(teams.current_team_id, None)
        teams.clear_teams()

    def test_clear_teams(self):
        teams.add_team(Team("test1", "password1", 1))
        teams.add_team(Team("test2", "password2", 2))
        teams.add_team(Team("test3", "password3", 3))
        teams.clear_teams()
        self.assertDictEqual(teams.teams, {})

    # drinks
    def test_add_drink(self):
        drink = Drink("coffee", 1)
        drinks.add_drink(drink)
        self.assertDictEqual(drinks.drinks, {1: drink})
        drinks.clear_drinks()

    def test_get_drink_names(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("tea", 2))
        drinks.add_drink(Drink("water", 3))
        self.assertListEqual(drinks.get_drinks_names(), ["coffee", "tea", "water"])
        drinks.clear_drinks()

    def test_get_drink_ids(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("tea", 2))
        drinks.add_drink(Drink("water", 3))
        self.assertListEqual(list(drinks.get_ids()), [1, 2, 3])
        drinks.clear_drinks()

    def test_get_drink(self):
        drinks.add_drink(Drink("coffee", 1))
        drink = Drink("tea", 2)
        drinks.add_drink(drink)
        drinks.add_drink(Drink("water", 3))
        self.assertEqual(drinks.get_drink(2), drink)
        drinks.clear_drinks()

    def test_cannot_get_drink(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("tea", 2))
        drinks.add_drink(Drink("water", 3))
        with self.assertRaises(ValueError):
            drinks.get_drink(4)
        drinks.clear_drinks()

    def test_clear_drinks(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("tea", 2))
        drinks.add_drink(Drink("water", 3))
        drinks.clear_drinks()
        self.assertDictEqual(drinks.drinks, {})

    # team members
    def test_add_team_member(self):
        team_members.clear_team_members()
        team_member = TeamMember("john smith", 1, 1)
        team_members.add_team_member(team_member)
        self.assertDictEqual(team_members.team_members, {1: team_member})
        team_members.clear_team_members()

    def test_get_team_member_names(self):
        team_members.add_team_member(TeamMember("john smith", 1, 1))
        team_members.add_team_member(TeamMember("mary smith", 1, 2))
        team_members.add_team_member(TeamMember("steve smith", 1, 3))
        self.assertListEqual(team_members.get_team_member_names(), ["john smith", "mary smith", "steve smith"])
        team_members.clear_team_members()

    def test_get_team_member_ids(self):
        team_members.add_team_member(TeamMember("john smith", 1, 1))
        team_members.add_team_member(TeamMember("mary smith", 1, 2))
        team_members.add_team_member(TeamMember("steve smith", 1, 3))
        self.assertListEqual(list(team_members.get_ids()), [1, 2, 3])
        team_members.clear_team_members()

    def test_get_team_member(self):
        team_members.add_team_member(TeamMember("john smith", 1, 1))
        team_member = TeamMember("mary smith", 1, 2)
        team_members.add_team_member(team_member)
        team_members.add_team_member(TeamMember("steve smith", 1, 3))
        self.assertEqual(team_members.get_team_member(2), team_member)
        team_members.clear_team_members()

    def test_cannot_get_team_member(self):
        team_members.add_team_member(TeamMember("john smith", 1, 1))
        team_members.add_team_member(TeamMember("mary smith", 1, 2))
        team_members.add_team_member(TeamMember("steve smith", 1, 3))
        with self.assertRaises(ValueError):
            team_members.get_team_member(4)
        team_members.clear_team_members()

    def test_clear_team_members(self):
        team_members.add_team_member(TeamMember("john smith", 1, 1))
        team_members.add_team_member(TeamMember("mary smith", 1, 2))
        team_members.add_team_member(TeamMember("steve smith", 1, 3))
        team_members.clear_team_members()
        self.assertDictEqual(team_members.team_members, {})

    # round
    def test_add_new_drink_to_round(self):
        drink = Drink("test", 1)
        team_member = TeamMember("test", drink, 1)
        drinks_round.add_drink(drink, team_member)
        self.assertDictEqual(drinks_round.drinks, {1: {"team_member_ids": [1], "team_members": [team_member], "drink": drink}})
        drinks_round.clear_order()

    def test_add_drink_to_round(self):
        drink = Drink("test", 1)
        team_member1 = TeamMember("test1", drink, 1)
        team_member2 = TeamMember("test2", drink, 2)
        drinks_round.add_drink(drink, team_member1)
        self.assertDictEqual(drinks_round.drinks, {1: {"team_member_ids": [1], "team_members": [team_member1], "drink": drink}})
        drinks_round.add_drink(drink, team_member2)
        self.assertDictEqual(drinks_round.drinks, {1: {"team_member_ids": [1, 2], "team_members": [team_member1, team_member2], "drink": drink}})
        drinks_round.clear_order()

    def test_does_not_add_drink_to_round(self):
        drink = Drink("test", 1)
        team_member = TeamMember("test1", drink, 1)
        drinks_round.add_drink(drink, team_member)
        self.assertDictEqual(drinks_round.drinks, {1: {"team_member_ids": [1], "team_members": [team_member], "drink": drink}})
        drinks_round.add_drink(drink, team_member)
        self.assertDictEqual(drinks_round.drinks, {1: {"team_member_ids": [1], "team_members": [team_member], "drink": drink}})
        drinks_round.clear_order()

    def test_get_drinks_in_order(self):
        drink1 = Drink("test1", 1)
        drink2 = Drink("test2", 2)
        team_member1 = TeamMember("test1", drink1, 1)
        team_member2 = TeamMember("test2", drink1, 2)
        team_member3 = TeamMember("test3", drink1, 3)
        drinks_round.add_drink(drink1, team_member1)
        drinks_round.add_drink(drink1, team_member2)
        drinks_round.add_drink(drink2, team_member3)
        self.assertListEqual(list(drinks_round.get_drinks_in_order()), [1, 2])
        drinks_round.clear_order()

    def test_get_brewer(self):
        team_member = TeamMember("john smith", 1, 1)
        team_members.add_team_member(team_member)
        drinks_round.update_brewer(team_member)
        self.assertEqual(drinks_round.get_brewer(), "John Smith")
        team_members.clear_team_members()
        drinks_round.clear_order()

    def test_update_brewer(self):
        team_member = TeamMember("john smith", 1, 1)
        drinks_round.update_brewer(team_member)
        self.assertEqual(drinks_round.brewer, team_member)
        drinks_round.clear_order()

    def test_update_id(self):
        drinks_round.update_id(1)
        self.assertEqual(drinks_round.id, 1)
        drinks_round.clear_order()

    def test_clear_order(self):
        drink = Drink("test", 1)
        team_member1 = TeamMember("test1", drink, 1)
        team_member2 = TeamMember("test2", drink, 2)
        drinks_round.add_drink(drink, team_member1)
        drinks_round.add_drink(drink, team_member2)
        drinks_round.update_brewer(team_member1)
        drinks_round.update_id(1)
        drinks_round.clear_order()
        self.assertDictEqual(drinks_round.drinks, {})
        self.assertEqual(drinks_round.brewer, None)
        self.assertEqual(drinks_round.id, None)


if __name__ == "__main__":
    unittest.main()
