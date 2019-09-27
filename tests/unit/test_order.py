import unittest
from unittest.mock import patch
from unittest.mock import call
from Source.app import *
from Source.classes.team_member import *
from Source.classes.teams import *
from Source.classes.team_members import *
from Source.classes.drinks import *
from Source.classes.round import *


drinks = Drinks()
team_members = TeamMembers()
teams = Teams()
drinks_round = Round()


def return_multiple(a, b):
    return a, b


class TestOrder(unittest.TestCase):

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 0), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.log_drinks', return_value='')
    def test_show_menu_select_option_0(self, operation, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation.assert_called_once_with(0, drinks, teams)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 0)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"add_drink_options"])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 1), return_multiple("", 15)])
    def test_show_menu_select_option_1(self, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 1)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_has_calls([call(ascii_images[f"view_drink_options"]), call(display_drinks(0, drinks))])
        hide_input.assert_called_once_with("  Press Enter To Return To Menu ")

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 2), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.log_team_members', return_value='')
    def test_show_menu_select_option_2(self, operation, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation.assert_called_once_with(0, drinks, team_members, teams)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 2)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"add_team_members"])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 3), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.update_preference', return_value='')
    def test_show_menu_select_option_3(self, operation, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation.assert_called_once_with(0, team_members, drinks)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 3)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"update_favourite_drink"])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 4), return_multiple("", 15)])
    def test_show_menu_select_option_4(self, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 4)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_has_calls([call(ascii_images[f"view_team_members"]), call(display_people(0, team_members))])
        hide_input.assert_called_once_with("  Press Enter To Return To Menu ")

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 5), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.select_brewer', return_value=False)
    def test_show_menu_select_option_5_without_success(self, operation, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation.assert_called_once_with(0, team_members, drinks, drinks_round)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 5)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"select_brewer"])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 5), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.take_order', return_value='')
    @unittest.mock.patch('Source.app.select_brewer', return_value=True)
    def test_show_menu_select_option_5_with_success(self, operation1, operation2, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation1.assert_called_once_with(0, team_members, drinks, drinks_round)
        operation2.assert_called_once_with(None, 0, drinks, team_members, drinks_round, teams)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 5)])
        hide_system.assert_has_calls([call("clear"), call("clear"), call("clear")])
        hide_print.assert_has_calls([call(ascii_images[f"select_brewer"]), call(ascii_images[f"take_order"])])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 6), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.select_brewer', return_value=False)
    def test_show_menu_select_option_6_without_success(self, operation, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation.assert_called_once_with(0, team_members, drinks, drinks_round)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 6)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"select_brewer"])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 6), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.take_favourite_order', return_value='')
    @unittest.mock.patch('Source.app.select_brewer', return_value=True)
    def test_show_menu_select_option_6_with_success(self, operation1, operation2, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation1.assert_called_once_with(0, team_members, drinks, drinks_round)
        operation2.assert_called_once_with(None, 0, team_members, drinks_round, drinks, teams)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 6)])
        hide_system.assert_has_calls([call("clear"), call("clear"), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"select_brewer"])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 7), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.no_order', return_value='')
    def test_show_menu_select_option_7_with_no_order(self, operation, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation.assert_called_once_with()
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 7)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"view_last_order"])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 7), return_multiple("", 15)])
    def test_show_menu_select_option_7_with_order(self, menu_input, hide_system, hide_input, hide_print):
        team_members.add_team_member(TeamMember("john", 1, 1))
        drinks_round.update_brewer(team_members.team_members[1])
        show_menu(True, 0, teams, drinks, team_members, drinks_round)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 7)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_has_calls([call(ascii_images[f"view_last_order"]), call(display_order(drinks_round, drinks, 0, team_members))])
        hide_input.assert_called_once_with("  Press Enter To Return To Menu ")
        team_members.clear_team_members()

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 8), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.no_order', return_value='')
    def test_show_menu_select_option_8_with_no_order(self, operation, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation.assert_called_once_with()
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 8)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"distribute_last_order"])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 8), return_multiple("", 15)])
    def test_show_menu_select_option_8_with_order(self, menu_input, hide_system, hide_input, hide_print):
        show_menu(True, 0, teams, drinks, team_members, drinks_round)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 8)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_has_calls([call(ascii_images[f"distribute_last_order"]), call(distribute(drinks_round, drinks, 0))])
        hide_input.assert_called_once_with("\n  Press Enter To Return To Menu ")

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 9), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.clear_last_order', return_value='')
    def test_show_menu_select_option_9(self, operation, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation.assert_called_once_with(False, drinks_round)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 9)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"clear_last_order"])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 10), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.change_password', return_value='')
    def test_show_menu_select_option_10(self, operation, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation.assert_called_once_with(True, teams)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 10)])
        hide_system.assert_has_calls([call("clear"), call("clear")])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 11), return_multiple("", 15)])
    def test_show_menu_select_option_11(self, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 11)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_has_calls([call(ascii_images[f"help"]), call(f"  BR-IW Has Been Designed To Help Record Your Drinks Rounds.\n  If You Have Any Issues, Please Consult The User Manual.")])
        hide_input.assert_called_once_with("  Press Enter To Return To Menu ")

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 12), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.logout', return_value='')
    def test_show_menu_select_option_12(self, operation, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation.assert_called_once_with(False, 0, teams, drinks, team_members, drinks_round)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 12)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"logout"])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 13), return_multiple("", 15)])
    @unittest.mock.patch('Source.app.end_app', return_value='')
    def test_show_menu_select_option_13(self, operation, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        operation.assert_called_once_with()
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 13)])
        hide_system.assert_has_calls([call("clear"), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"exit"])

    @unittest.mock.patch('builtins.print', return_value='')
    @unittest.mock.patch('builtins.input', return_value='')
    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', side_effect=[return_multiple("", 14), return_multiple("", 15)])
    def test_show_menu_select_option_14(self, menu_input, hide_system, hide_input, hide_print):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        menu_input.assert_has_calls([call(ascii_images["drink_menu_string"], 0), call("", 14)])
        hide_system.assert_has_calls([call("clear"), call(ascii_images["lyrics"]), call("clear")])
        hide_print.assert_called_once_with(ascii_images[f"rick"])
        hide_input.assert_called_once_with("  Press Enter To Return To Menu ")

    @unittest.mock.patch('os.system', return_value='')
    @unittest.mock.patch('Source.app.menu_user_input', return_value=return_multiple("", 15))
    def test_show_menu_select_option_15(self, menu_input, hide_system):
        show_menu(False, 0, teams, drinks, team_members, drinks_round)
        menu_input.assert_called_once_with(ascii_images["drink_menu_string"], 0)
        hide_system.assert_called_once_with("clear")


if __name__ == "__main__":
    unittest.main()
