import unittest
from Source.string_helpers import *
from Source.classes.drink import *
from Source.classes.team_member import *
from Source.classes.teams import *
from Source.classes.team_members import *
from Source.classes.drinks import *
from Source.classes.round import *


drinks = Drinks()
team_members = TeamMembers()
teams = Teams()
drinks_round = Round()


class TestStringHelperIntegration(unittest.TestCase):

    def test_display_people(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("tea", 2))
        drinks.add_drink(Drink("water", 3))
        team_members.add_team_member(TeamMember("john smith", drinks.drinks[1], 1))
        team_members.add_team_member(TeamMember("mary smith", drinks.drinks[1], 2))
        team_members.add_team_member(TeamMember("steve smith", drinks.drinks[2], 3))
        self.assertMultiLineEqual(display_people(0, team_members), """  ╔═══════╦══════════════════════════════╦════════════╦══════════════════════════════╗
  ║  Id   ║  Team Members                ║  Drink Id  ║  Favourite Drink             ║
  ╠═══════╬══════════════════════════════╬════════════╬══════════════════════════════╣
  ║  1    ║  John Smith                  ║  1         ║  Coffee                      ║
  ║  2    ║  Mary Smith                  ║  1         ║  Coffee                      ║
  ║  3    ║  Steve Smith                 ║  2         ║  Tea                         ║
  ╚═══════╩══════════════════════════════╩════════════╩══════════════════════════════╝

""")
        team_members.clear_team_members()
        drinks.clear_drinks()

    def test_display_larger_people_with_large_drinks(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("teaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 1000001))
        drinks.add_drink(Drink("water", 3))
        team_members.add_team_member(TeamMember("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", drinks.drinks[1], 1))
        team_members.add_team_member(TeamMember("mary smith", drinks.drinks[1], 2))
        team_members.add_team_member(TeamMember("steve smith", drinks.drinks[1000001], 10001))
        self.assertMultiLineEqual(display_people(0, team_members), """  ╔═════════╦═══════════════════════════════════════════════════════════╦════════════╦═══════════════════════════════════════════════╗
  ║  Id     ║  Team Members                                             ║  Drink Id  ║  Favourite Drink                              ║
  ╠═════════╬═══════════════════════════════════════════════════════════╬════════════╬═══════════════════════════════════════════════╣
  ║  1      ║  Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  ║  1         ║  Coffee                                       ║
  ║  2      ║  Mary Smith                                               ║  1         ║  Coffee                                       ║
  ║  10001  ║  Steve Smith                                              ║  1000001   ║  Teaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  ║
  ╚═════════╩═══════════════════════════════════════════════════════════╩════════════╩═══════════════════════════════════════════════╝

""")
        team_members.clear_team_members()
        drinks.clear_drinks()

    def test_display_no_people(self):
        self.assertMultiLineEqual(display_people(0, team_members), """  ╔═══════╦══════════════════════════════╦════════════╦══════════════════════════════╗
  ║  Id   ║  Team Members                ║  Drink Id  ║  Favourite Drink             ║
  ╠═══════╬══════════════════════════════╬════════════╬══════════════════════════════╣
  ║       ║                              ║            ║                              ║
  ╚═══════╩══════════════════════════════╩════════════╩══════════════════════════════╝

""")

    def test_display_drinks(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("tea", 2))
        drinks.add_drink(Drink("water", 3))
        self.assertMultiLineEqual(display_drinks(0, drinks), """  ╔═══════╦══════════════════════════════╗
  ║  Id   ║  Drink Options               ║
  ╠═══════╬══════════════════════════════╣
  ║  1    ║  Coffee                      ║
  ║  2    ║  Tea                         ║
  ║  3    ║  Water                       ║
  ╚═══════╩══════════════════════════════╝

""")
        drinks.clear_drinks()

    def test_display_larger_drinks(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("teaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 1000001))
        drinks.add_drink(Drink("water", 3))
        self.assertMultiLineEqual(display_drinks(0, drinks), """  ╔═══════════╦═══════════════════════════════════════════════╗
  ║  Id       ║  Drink Options                                ║
  ╠═══════════╬═══════════════════════════════════════════════╣
  ║  1        ║  Coffee                                       ║
  ║  1000001  ║  Teaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  ║
  ║  3        ║  Water                                        ║
  ╚═══════════╩═══════════════════════════════════════════════╝

""")
        drinks.clear_drinks()

    def test_display_no_drinks(self):
        self.assertMultiLineEqual(display_drinks(0, drinks), """  ╔═══════╦══════════════════════════════╗
  ║  Id   ║  Drink Options               ║
  ╠═══════╬══════════════════════════════╣
  ║       ║                              ║
  ╚═══════╩══════════════════════════════╝

""")

    def test_display_order(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("tea", 2))
        drinks.add_drink(Drink("water", 3))
        team_members.add_team_member(TeamMember("john", drinks.drinks[1], 1))
        team_members.add_team_member(TeamMember("mary smith", drinks.drinks[1], 2))
        team_members.add_team_member(TeamMember("steve smith", drinks.drinks[1], 3))
        team_members.add_team_member(TeamMember("bob smith", drinks.drinks[1], 4))
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[1])
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[2])
        drinks_round.add_drink(drinks.drinks[2], team_members.team_members[3])
        drinks_round.add_drink(drinks.drinks[3], team_members.team_members[4])
        drinks_round.update_brewer(team_members.team_members[1])
        self.assertMultiLineEqual(display_order(drinks_round, drinks, 0, team_members), """
  ╔══════════════════════════════╗
  ║  John Will Need To Make      ║
  ╠══════════════════════════════╣
  ║  2 Coffees                   ║
  ║  1 Tea                       ║
  ║  1 Water                     ║
  ╚══════════════════════════════╝

""")
        drinks.clear_drinks()
        team_members.clear_team_members()
        drinks_round.clear_order()

    def test_display_larger_order(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("teaaaaaaaaaaaaaaaaaaaaaaaaaa", 2))
        drinks.add_drink(Drink("water", 3))
        team_members.add_team_member(TeamMember("john", drinks.drinks[1], 1))
        team_members.add_team_member(TeamMember("mary smith", drinks.drinks[1], 2))
        team_members.add_team_member(TeamMember("steve smith", drinks.drinks[1], 3))
        team_members.add_team_member(TeamMember("bob smith", drinks.drinks[1], 4))
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[1])
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[2])
        drinks_round.add_drink(drinks.drinks[2], team_members.team_members[3])
        drinks_round.add_drink(drinks.drinks[3], team_members.team_members[4])
        drinks_round.update_brewer(team_members.team_members[1])
        self.assertMultiLineEqual(display_order(drinks_round, drinks, 0, team_members), """
  ╔══════════════════════════════════╗
  ║  John Will Need To Make          ║
  ╠══════════════════════════════════╣
  ║  2 Coffees                       ║
  ║  1 Teaaaaaaaaaaaaaaaaaaaaaaaaaa  ║
  ║  1 Water                         ║
  ╚══════════════════════════════════╝

""")
        drinks.clear_drinks()
        team_members.clear_team_members()
        drinks_round.clear_order()

    def test_display_order_with_larger_brewer(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("tea", 2))
        drinks.add_drink(Drink("water", 3))
        team_members.add_team_member(TeamMember("johnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn", drinks.drinks[1], 1))
        team_members.add_team_member(TeamMember("mary smith", drinks.drinks[1], 2))
        team_members.add_team_member(TeamMember("steve smith", drinks.drinks[1], 3))
        team_members.add_team_member(TeamMember("bob smith", drinks.drinks[1], 4))
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[1])
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[2])
        drinks_round.add_drink(drinks.drinks[2], team_members.team_members[3])
        drinks_round.add_drink(drinks.drinks[3], team_members.team_members[4])
        drinks_round.update_brewer(team_members.team_members[1])
        self.assertMultiLineEqual(display_order(drinks_round, drinks, 0, team_members), """
  ╔══════════════════════════════════════════════════════════╗
  ║  Johnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn Will Need To Make  ║
  ╠══════════════════════════════════════════════════════════╣
  ║  2 Coffees                                               ║
  ║  1 Tea                                                   ║
  ║  1 Water                                                 ║
  ╚══════════════════════════════════════════════════════════╝

""")
        drinks.clear_drinks()
        team_members.clear_team_members()
        drinks_round.clear_order()

    def test_display_no_order(self):
        drinks.add_drink(Drink("coffee", 1))
        team_members.add_team_member(TeamMember("john", drinks.drinks[1], 1))
        drinks_round.update_brewer(team_members.team_members[1])
        self.assertMultiLineEqual(display_order(drinks_round, drinks, 0, team_members), """
  ╔══════════════════════════════╗
  ║  John Will Need To Make      ║
  ╠══════════════════════════════╣
  ║                              ║
  ╚══════════════════════════════╝

""")
        team_members.clear_team_members()
        drinks.clear_drinks()
        drinks_round.clear_order()

    def test_display_no_distribute(self):
        self.assertEqual(distribute(drinks_round, drinks, 0), "  There Were No Drinks To Distribute In The Last Order.")

    def test_display_distribute(self):
        drinks.add_drink(Drink("coffee", 1))
        team_members.add_team_member(TeamMember("john", drinks.drinks[1], 1))
        team_members.add_team_member(TeamMember("mary", drinks.drinks[1], 2))
        team_members.add_team_member(TeamMember("steve", drinks.drinks[1], 3))
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[1])
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[2])
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[3])
        drinks_round.update_brewer(team_members.team_members[1])
        self.assertMultiLineEqual(distribute(drinks_round, drinks, 0), """
  ╔══════════════════════════════╗
  ║  Coffee                      ║
  ╠══════════════════════════════╣
  ║  John                        ║
  ║  Mary                        ║
  ║  Steve                       ║
  ╚══════════════════════════════╝
""")
        team_members.clear_team_members()
        drinks_round.clear_order()
        drinks.clear_drinks()

    def test_display_distribute_multiple_drinks(self):
        drinks.add_drink(Drink("coffee", 1))
        drinks.add_drink(Drink("tea", 2))
        team_members.add_team_member(TeamMember("john", drinks.drinks[1], 1))
        team_members.add_team_member(TeamMember("mary", drinks.drinks[1], 2))
        team_members.add_team_member(TeamMember("steve", drinks.drinks[1], 3))
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[1])
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[2])
        drinks_round.add_drink(drinks.drinks[2], team_members.team_members[3])
        drinks_round.update_brewer(team_members.team_members[1])
        self.assertMultiLineEqual(distribute(drinks_round, drinks, 0), """
  ╔══════════════════════════════╗
  ║  Coffee                      ║
  ╠══════════════════════════════╣
  ║  John                        ║
  ║  Mary                        ║
  ╚══════════════════════════════╝

  ╔══════════════════════════════╗
  ║  Tea                         ║
  ╠══════════════════════════════╣
  ║  Steve                       ║
  ╚══════════════════════════════╝
""")
        team_members.clear_team_members()
        drinks_round.clear_order()
        drinks.clear_drinks()

    def test_display_distribute_large_drinks(self):
        drinks.add_drink(Drink("coffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", 1))
        team_members.add_team_member(TeamMember("john", drinks.drinks[1], 1))
        team_members.add_team_member(TeamMember("mary", drinks.drinks[1], 2))
        team_members.add_team_member(TeamMember("steve", drinks.drinks[1], 3))
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[1])
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[2])
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[3])
        drinks_round.update_brewer(team_members.team_members[1])
        self.assertMultiLineEqual(distribute(drinks_round, drinks, 0), """
  ╔════════════════════════════════════════════════╗
  ║  Coffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee  ║
  ╠════════════════════════════════════════════════╣
  ║  John                                          ║
  ║  Mary                                          ║
  ║  Steve                                         ║
  ╚════════════════════════════════════════════════╝
""")
        team_members.clear_team_members()
        drinks_round.clear_order()
        drinks.clear_drinks()

    def test_display_distribute_to_large_people(self):
        drinks.add_drink(Drink("coffee", 1))
        team_members.add_team_member(TeamMember("johnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn", drinks.drinks[1], 1))
        team_members.add_team_member(TeamMember("mary", drinks.drinks[1], 2))
        team_members.add_team_member(TeamMember("steve", drinks.drinks[1], 3))
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[1])
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[2])
        drinks_round.add_drink(drinks.drinks[1], team_members.team_members[3])
        drinks_round.update_brewer(team_members.team_members[1])
        self.assertMultiLineEqual(distribute(drinks_round, drinks, 0), """
  ╔═══════════════════════════════════════════════╗
  ║  Coffee                                       ║
  ╠═══════════════════════════════════════════════╣
  ║  Johnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn  ║
  ║  Mary                                         ║
  ║  Steve                                        ║
  ╚═══════════════════════════════════════════════╝
""")
        team_members.clear_team_members()
        drinks_round.clear_order()
        drinks.clear_drinks()


if __name__ == "__main__":
    unittest.main()
