import unittest
from Source.string_helpers import *
from Source.classes import *


class StringHelperIntegrationTests(unittest.TestCase):

    def test_display_people(self):
        team_members.add_team_member(TeamMember("john smith", 1, 0))
        team_members.add_team_member(TeamMember("mary smith", 1, 1))
        team_members.add_team_member(TeamMember("steve smith", 2, 2))
        drinks.add_drink(Drink("coffee", 0))
        drinks.add_drink(Drink("tea", 1))
        drinks.add_drink(Drink("water", 2))
        self.assertMultiLineEqual(display_people("drink", team_members), """  ╔═══════╦══════════════════════════════╦════════════╦══════════════════════════════╗
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
        team_members.add_team_member(TeamMember("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 1, 0))
        team_members.add_team_member(TeamMember("mary smith", 1, 1))
        team_members.add_team_member(TeamMember("steve smith", 1000001, 10000))
        drinks.add_drink(Drink("coffee", 0))
        drinks.add_drink(Drink("teaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 1000000))
        drinks.add_drink(Drink("water", 2))
        self.assertMultiLineEqual(display_people("drink", team_members), """  ╔═════════╦═══════════════════════════════════════════════════════════╦════════════╦═══════════════════════════════════════════════╗
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
        self.assertMultiLineEqual(display_people("drink", team_members), """  ╔═══════╦══════════════════════════════╦════════════╦══════════════════════════════╗
  ║  Id   ║  Team Members                ║  Drink Id  ║  Favourite Drink             ║
  ╠═══════╬══════════════════════════════╬════════════╬══════════════════════════════╣
  ║       ║                              ║            ║                              ║
  ╚═══════╩══════════════════════════════╩════════════╩══════════════════════════════╝

""")

    def test_display_drinks(self):
        drinks.add_drink(Drink("coffee", 0))
        drinks.add_drink(Drink("tea", 1))
        drinks.add_drink(Drink("water", 2))
        self.assertMultiLineEqual(display_drinks("drink", drinks), """  ╔═══════╦══════════════════════════════╗
  ║  Id   ║  Drink Options               ║
  ╠═══════╬══════════════════════════════╣
  ║  1    ║  Coffee                      ║
  ║  2    ║  Tea                         ║
  ║  3    ║  Water                       ║
  ╚═══════╩══════════════════════════════╝

""")
        drinks.clear_drinks()

    def test_display_larger_drinks(self):
        drinks.add_drink(Drink("coffee", 0))
        drinks.add_drink(Drink("teaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 1000000))
        drinks.add_drink(Drink("water", 2))
        self.assertMultiLineEqual(display_drinks("drink", drinks), """  ╔═══════════╦═══════════════════════════════════════════════╗
  ║  Id       ║  Drink Options                                ║
  ╠═══════════╬═══════════════════════════════════════════════╣
  ║  1        ║  Coffee                                       ║
  ║  1000001  ║  Teaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  ║
  ║  3        ║  Water                                        ║
  ╚═══════════╩═══════════════════════════════════════════════╝

""")
        drinks.clear_drinks()

    def test_display_no_drinks(self):
        self.assertMultiLineEqual(display_drinks("drink", drinks), """  ╔═══════╦══════════════════════════════╗
  ║  Id   ║  Drink Options               ║
  ╠═══════╬══════════════════════════════╣
  ║       ║                              ║
  ╚═══════╩══════════════════════════════╝

""")

    def test_display_order(self):
        team_members.add_team_member(TeamMember("john", 1, 0))
        team_members.add_team_member(TeamMember("mary smith", 1, 1))
        team_members.add_team_member(TeamMember("steve smith", 1, 2))
        team_members.add_team_member(TeamMember("bob smith", 1, 3))
        drinks.add_drink(Drink("coffee", 0))
        drinks.add_drink(Drink("tea", 1))
        drinks.add_drink(Drink("water", 2))
        drinks_round.add_drink(1, 1)
        drinks_round.add_drink(1, 2)
        drinks_round.add_drink(2, 3)
        drinks_round.add_drink(3, 4)
        drinks_round.update_brewer(1)
        self.assertMultiLineEqual(display_order(drinks_round, drinks, "brewer"), """
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
        team_members.add_team_member(TeamMember("john", 1, 0))
        team_members.add_team_member(TeamMember("mary smith", 1, 1))
        team_members.add_team_member(TeamMember("steve smith", 1, 2))
        team_members.add_team_member(TeamMember("bob smith", 1, 3))
        drinks.add_drink(Drink("coffee", 0))
        drinks.add_drink(Drink("teaaaaaaaaaaaaaaaaaaaaaaaaaa", 1))
        drinks.add_drink(Drink("water", 2))
        drinks_round.add_drink(1, 1)
        drinks_round.add_drink(1, 2)
        drinks_round.add_drink(2, 3)
        drinks_round.add_drink(3, 4)
        drinks_round.update_brewer(1)
        self.assertMultiLineEqual(display_order(drinks_round, drinks, "brewer"), """
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
        team_members.add_team_member(TeamMember("johnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn", 1, 0))
        team_members.add_team_member(TeamMember("mary smith", 1, 1))
        team_members.add_team_member(TeamMember("steve smith", 1, 2))
        team_members.add_team_member(TeamMember("bob smith", 1, 3))
        drinks.add_drink(Drink("coffee", 0))
        drinks.add_drink(Drink("tea", 1))
        drinks.add_drink(Drink("water", 2))
        drinks_round.add_drink(1, 1)
        drinks_round.add_drink(1, 2)
        drinks_round.add_drink(2, 3)
        drinks_round.add_drink(3, 4)
        drinks_round.update_brewer(1)
        self.assertMultiLineEqual(display_order(drinks_round, drinks, "brewer"), """
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
        team_members.add_team_member(TeamMember("john", 1, 0))
        drinks_round.update_brewer(1)
        self.assertMultiLineEqual(display_order(drinks_round, drinks, "brewer"), """
  ╔══════════════════════════════╗
  ║  John Will Need To Make      ║
  ╠══════════════════════════════╣
  ║                              ║
  ╚══════════════════════════════╝

""")
        team_members.clear_team_members()
        drinks_round.clear_order()


if __name__ == "__main__":
    unittest.main()