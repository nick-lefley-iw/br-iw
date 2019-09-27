import os
import time
import curses
import sys
from Source.string_helpers import distribute, display_order, display_people, display_drinks, update_menu_string, ascii_images
from Source.controllers.persistence_management_controller import read_team
from Source.controllers.team_controller import login, logout, change_password
from Source.controllers.round_controller import no_order, clear_last_order, select_brewer, take_favourite_order, take_order
from Source.controllers.drink_controller import log_drinks
from Source.controllers.team_member_controller import log_team_members, update_preference
from Source.classes.drinks import Drinks
from Source.classes.team_members import TeamMembers
from Source.classes.round import Round
from Source.classes.teams import Teams
from Source.enums import *


def menu_user_input(menu_string, option):
    os.system("clear")
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    screen.addstr(menu_string)
    curses.curs_set(0)

    try:
        while True:
            char = screen.getch()
            if char == curses.KEY_ENTER or char == 10:
                break
            elif char == curses.KEY_UP and option != 0:
                screen.clear()
                menu_string = update_menu_string(menu_string, option, True)
                try:
                    screen.addstr(menu_string)
                except:
                    pass
                option -= 1
            elif char == curses.KEY_DOWN and option != 14:
                screen.clear()
                menu_string = update_menu_string(menu_string, option, False)
                try:
                    screen.addstr(menu_string)
                except:
                    pass
                option += 1
            curses.curs_set(0)
    finally:
        screen.clear()
        screen.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    return menu_string, option


def show_menu(any_orders, item_type, teams, drinks, team_members, drinks_round):
    option = 0
    menu_string = ascii_images[item_types[item_type] + "_menu_string"]

    while True:
        menu_string, option = menu_user_input(menu_string, option)
        os.system("clear")

        # add drinks options
        if option == 0:
            print(ascii_images[f"add_{item_types[item_type]}_options"])
            log_drinks(item_type, drinks, teams)
        # view drink options
        elif option == 1:
            print(ascii_images[f"view_{item_types[item_type]}_options"])
            print(display_drinks(item_type, drinks))
            input("  Press Enter To Return To Menu ")
        # add team members
        elif option == 2:
            print(ascii_images["add_team_members"])
            log_team_members(item_type, drinks, team_members, teams)
        # update favourite drink
        elif option == 3:
            print(ascii_images[f"update_favourite_{item_types[item_type]}"])
            update_preference(item_type, team_members, drinks)
        # view team members
        elif option == 4:
            print(ascii_images["view_team_members"])
            print(display_people(item_type, team_members))
            input("  Press Enter To Return To Menu ")
        # take order
        elif option == 5:
            print(ascii_images[f"select_{waiter_types[item_type]}"])
            old_id = drinks_round.id
            success = select_brewer(item_type, team_members, drinks, drinks_round)
            if success:
                os.system("clear")
                print(ascii_images["take_order"])
                take_order(old_id, item_type, drinks, team_members, drinks_round, teams)
                any_orders = True
        # take favourite order
        elif option == 6:
            print(ascii_images[f"select_{waiter_types[item_type]}"])
            old_id = drinks_round.id
            success = select_brewer(item_type, team_members, drinks, drinks_round)
            if success:
                os.system("clear")
                take_favourite_order(old_id, item_type, team_members, drinks_round, drinks, teams)
                any_orders = True
        # view last order
        elif option == 7:
            print(ascii_images["view_last_order"])
            if any_orders:
                print(display_order(drinks_round, drinks, item_type, team_members))
                input("  Press Enter To Return To Menu ")
            else:
                no_order()
        # distribute last order
        elif option == 8:
            print(ascii_images["distribute_last_order"])
            if any_orders:
                print(distribute(drinks_round, drinks, item_type))
                input("\n  Press Enter To Return To Menu ")
            else:
                no_order()
        # clear last order
        elif option == 9:
            print(ascii_images["clear_last_order"])
            any_orders = clear_last_order(any_orders, drinks_round)
        # change team details
        elif option == 10:
            change_password(True, teams)
        # help
        elif option == 11:
            print(ascii_images["help"])
            print(f"  BR-IW Has Been Designed To Help Record Your {item_types[item_type].capitalize()}s Rounds.\n  If You Have Any Issues, Please Consult The User Manual.")
            input("  Press Enter To Return To Menu ")
        # logout
        elif option == 12:
            print(ascii_images["logout"])
            any_orders = logout(any_orders, item_type, teams, drinks, team_members, drinks_round)
        # exit
        elif option == 13:
            print(ascii_images["exit"])
            end_app()
        # bonus
        elif option == 14:
            print(ascii_images["rick"])
            os.system(ascii_images["lyrics"])
            input("  Press Enter To Return To Menu ")
        else:
            break


def end_app():
    finish_check = input(f"  Are You Sure You Want To Exit? (Y/N) ").strip()
    while finish_check.upper() != "Y" and finish_check.upper() != "N":
        finish_check = input(f"  Sorry, I Did Not Understand That. Are You Sure You Want To Exit? (Y/N) ").strip()
    if finish_check.upper() == "Y":
        print(ascii_images["goodbye"])
        time.sleep(1)
        os.system("clear")
        exit()


def run_app():
    any_orders = False
    item_type = 0
    drinks = Drinks()
    team_members = TeamMembers()
    teams = Teams()
    drinks_round = Round()

    os.system("printf '\e[8;100;200t'")
    arguments = sys.argv
    if len(arguments) == 2 and arguments[1] == "mib":
        item_type = 1
    read_team(teams)
    any_orders = login(False, any_orders, item_type, teams, drinks, team_members, drinks_round)
    show_menu(any_orders, item_type, teams, drinks, team_members, drinks_round)


if __name__ == "__main__":
    run_app()
