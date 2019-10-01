import os
from Source.string_helpers import display_drinks, ascii_images, display_people
from Source.controllers.persistence_management_controller import append_team_member, update_team_member
from Source.classes.team_member import TeamMember
from Source.enums import *


def log_team_members(item_type, drinks, team_members, teams):
    if len(drinks.get_ids()) == 0:
        print(f"  You Must Add {item_types[item_type].capitalize()} Options Before You Can Add Team Members.")
        input("\n  Press Enter To Return To Menu ")
        return
    print(display_drinks(item_type, drinks))

    finished = False

    while not finished:
        add_text = f"Add Another Team Member"
        item_name = input(f"  Enter Team Member Name: ").strip()
        if not item_name.strip():
            print(f"  Sorry, I Did Not Understand That.")
        elif "|" in item_name:
            print(f"  Sorry, That Is Not A Valid Entry.")
        elif item_name.lower() in team_members.get_team_member_names():
            print(f"  Sorry, You Have Already Entered That.")
        else:
            while True:
                preference = input(f"  Enter Favourite {item_types[item_type].capitalize()} Id: ").strip()
                if not preference.strip() or not preference.isdigit() or int(preference) not in drinks.get_ids():
                    response = ""
                    if not preference.strip():
                        response = input(f"  Sorry, I Did Not Understand That. Do You Still Want To Add {item_name.capitalize()}? (Y/N) ").strip()
                    else:
                        response = input(f"  Sorry, That Is Not An Option. Do You Still Want To Add {item_name.capitalize()}? (Y/N) ").strip()

                    while response.upper() != "Y" and response.upper() != "N":
                        response = input(f"  Sorry, I Did Not Understand That. Do You Still Want To Add {item_name.capitalize()}? (Y/N) ").strip()
                    if response.lower() == "n":
                        break
                else:
                    team_member_id = append_team_member(item_type, item_name, preference, teams.current_team_id)
                    team_member = TeamMember(item_name.lower(), drinks.get_drink(int(preference)), team_member_id)
                    team_members.add_team_member(team_member)
                    break

        finish_check = input(f"  {add_text}? (Y/N) ").strip()
        while finish_check.upper() != "Y" and finish_check.upper() != "N":
            finish_check = input(f"  Sorry, I Did Not Understand That. {add_text}? (Y/N) ").strip()
        finished = finish_check.upper() == "N"
        if not finished:
            os.system("clear")
            print(ascii_images["add_team_members"])
            print(display_drinks(item_type, drinks))


def update_preference(item_type, team_members, drinks):
    if len(team_members.get_ids()) == 0 or len(drinks.get_ids()) == 0:
        print(f"  You Must Add Team Members And {item_types[item_type].capitalize()} Options Before You Can Update Favourites.")
        input("\n  Press Enter To Return To Menu ")
        return

    print(display_people(item_type, team_members))
    person = ""

    while True:
        person = input("  Enter The Id Of The Person You Would Like To Update: ").strip()
        if not person.strip() or not person.isdigit() or int(person) not in team_members.get_ids():
            response = ""
            if not person.strip():
                response = input(f"  Sorry, I Did Not Understand That. Would You Still Like To Update A Favourite {item_types[item_type].capitalize()}? (Y/N) ").strip()
            else:
                response = input(f"  Sorry, That Is Not An Option. Would You Still Like To Update A Favourite {item_types[item_type].capitalize()}? (Y/N) ").strip()

            while response.upper() != "Y" and response.upper() != "N":
                response = input(f"  Sorry, I Did Not Understand That. Would You Still Like To Update A Favourite {item_types[item_type].capitalize()}? (Y/N) ").strip()
            if response.lower() == "n":
                return
        else:
            break

    print(display_drinks(item_type, drinks))
    person_name = team_members.get_team_member(int(person)).get_name()
    drink = ""

    while True:
        drink = input(f"  Enter The Id Of {person_name}'s Favourite {item_types[item_type].capitalize()}: ").strip()
        if not drink.strip() or not drink.isdigit() or int(drink) not in drinks.get_ids():
            response = ""
            if not drink.strip():
                response = input(f"  Sorry, I Did Not Understand That. Would You Still Like To Update A Favourite {item_types[item_type].capitalize()}? (Y/N) ").strip()
            else:
                response = input(f"  Sorry, That Is Not An Option. Would You Still Like To Update A Favourite {item_types[item_type].capitalize()}? (Y/N) ").strip()

            while response.upper() != "Y" and response.upper() != "N":
                response = input(f"  Sorry, I Did Not Understand That. Would You Still Like To Update A Favourite {item_types[item_type].capitalize()}? (Y/N) ").strip()
            if response.lower() == "n":
                return
        else:
            break

    team_members.get_team_member(int(person)).update_preference(int(drink))
    update_team_member(person, None, drink)
    print("  Preference Updated.")
    input("\n  Press Enter To Return To Menu ")
