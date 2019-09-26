import getpass
import os
from Source.string_helpers import ascii_images
from Source.controllers.persistence_management_controller import read_drink, read_team_member, read_round, update_team_password


def login(already_got_team, any_orders, item_type, teams, drinks, team_members, drinks_round):
    os.system("clear")
    print(ascii_images["login"])
    if not already_got_team:
        team_name = input("  Team Name: ").strip().lower()
        while not team_name.strip() or team_name not in teams.get_team_names():
            os.system("clear")
            print(ascii_images["login"])
            if not team_name.strip():
                print(f"  ** Invalid Input **")
            else:
                print(f"  ** Invalid Team Name **")
            team_name = input(f"  Team Name: ").strip().lower()
        teams.update_current_team(team_name)
        os.system("clear")
        print(ascii_images["login"])
        print(f"  Team Name: {team_name}")
    else:
        print(f"  Team Name: {teams.current_team_name}")
        print(f"  ** Incorrect Password **")

    password = getpass.getpass("  Password: ")
    if password != teams.current_team_password:
        any_orders = login(True, any_orders, item_type, teams, drinks, team_members, drinks_round)
    else:
        read_drink(teams.current_team_id, drinks, item_type)
        read_team_member(teams.current_team_id, team_members, item_type)
        any_orders = read_round(item_type, any_orders, teams.current_team_id, drinks_round)

    return any_orders


def logout(any_orders, item_type, teams, drinks, team_members, drinks_round):
    finish_check = input(f"  Are You Sure You Want To Logout? (Y/N) ").strip()
    while finish_check.upper() != "Y" and finish_check.upper() != "N":
        finish_check = input(f"  Sorry, I Did Not Understand That. Are You Sure You Want To Logout? (Y/N) ").strip()
    if finish_check.upper() == "Y":
        os.system("clear")
        teams.logout_team()
        drinks.clear_drinks()
        team_members.clear_team_members()
        drinks_round.clear_order()
        any_orders = login(False, any_orders, item_type, teams, drinks, team_members, drinks_round)

    return any_orders


def change_password(correct_try, teams):
    os.system("clear")
    print(ascii_images["change_team_details"])

    if not correct_try:
        print(f"  ** Incorrect Password **")
    password = getpass.getpass("  Old Password: ")

    if password != teams.current_team_password:
        change_password(False, teams)
    else:
        new_password = getpass.getpass("  New Password: ")
        update_team_password(new_password, teams.current_team_id)
        teams.get_team(teams.current_team_id).update_password(new_password)
