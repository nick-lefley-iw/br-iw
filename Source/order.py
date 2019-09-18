import os
import time
import curses
import getpass
import random
import sys
from Source.classes import *
from Source.string_helpers import *

any_orders = False
team_name = ""
largest_team_member_id = 0
largest_drink_id = 0
item_type = "drink"
waiter = "brewer"


def login(already_got_team):
    global team_name

    os.system("clear")
    print(ascii_images["login"])
    if not already_got_team:
        team_name = input("  Team Name: ").strip().lower()
        while not team_name.strip() or team_name not in teams.get_team_names():
            if not team_name.strip():
                team_name = input(f"  Sorry, I Did Not Understand That. Team Name: ").strip().lower()
            else:
                team_name = input(f"  Sorry, That Team Does Not Exist. Team Name: ").strip().lower()
    else:
        print(f"  Team Name: {team_name}")
        print(f"  ** Incorrect Password **")

    password = getpass.getpass("  Password: ")
    if password != teams.get_password(team_name):
        login(True)
    else:
        read_data()


def change_password(correct_try):
    os.system("clear")
    print(ascii_images["change_team_details"])

    if not correct_try:
        print(f"  ** Incorrect Password **")
    password = getpass.getpass("  Old Password: ")

    if password != teams.get_password(team_name):
        change_password(False)
    else:
        new_password = getpass.getpass("  New Password: ")
        old_id = None
        lines_to_keep = []

        try:
            with open("data/teams.txt", "r") as order_records:
                for line in order_records.readlines():
                    data = line.split("|")
                    if len(data) > 2 and data[1] != team_name:
                        lines_to_keep.append(line)
                    else:
                        old_id = int(data[0])
        except FileNotFoundError as err:
            print("  Unable To Open Teams File: " + str(err))
            return

        try:
            open('data/teams.txt', 'w').close()
        except FileNotFoundError as err:
            print("  Unable To Open Teams File: " + str(err))
            return

        try:
            with open("data/teams.txt", "w") as order_records:
                for line in lines_to_keep:
                    order_records.write(line)
                order_records.write(f"{old_id}|{team_name}|{new_password}|\n")
        except FileNotFoundError as err:
            print("  Unable To Open Teams File: " + str(err))
            return

        teams.get_team(old_id).update_password(new_password)


def read_team_data():
    try:
        with open("data/teams.txt", "r") as team_records:
            for line in team_records:
                data = line.split("|")
                teams.add_team(Team(data[1].strip(), data[2].strip(), int(data[0].strip())))
    except FileNotFoundError as err:
        print("  Unable To Open Teams File: " + str(err))


def read_data():
    global any_orders
    global largest_team_member_id
    global largest_drink_id

    try:
        with open(f"data/{item_type}s.txt", "r") as drink_records:
            for line in drink_records:
                data = line.split("|")
                largest_drink_id = max(largest_drink_id, int(data[0].strip()))
                if data[2].strip() == team_name:
                    drinks.add_drink(Drink(data[1].strip(), largest_drink_id, int(data[0].strip())))
    except FileNotFoundError as err:
        print(f"  Unable To Open {item_type.capitalize()}s File: " + str(err))

    try:
        with open(f"data/people_{item_type}.txt", "r") as people_records:
            for line in people_records:
                data = line.split("|")
                largest_team_member_id = max(largest_team_member_id, int(data[0].strip()))
                if data[3].strip() == team_name:
                    team_members.add_team_member(
                        TeamMember(data[1].strip(), int(data[2].strip()), largest_team_member_id, int(data[0].strip())))
    except FileNotFoundError as err:
        print("  Unable To Open Team Member File: " + str(err))

    try:
        with open(f"data/{item_type}_order.txt", "r") as order_records:
            lines = order_records.readlines()
            if len(lines) > 0 and len(lines[0].split("\n")) > 0 and lines[0].split("\n")[0].strip():
                any_orders = True
                for line in lines:
                    data = line.split("|")
                    if len(data) > 2 and data[-2].strip() == team_name:
                        for person in data[2:-2]:
                            drinks_round.add_drink(int(data[0].strip()), int(person.strip()))
                        drinks_round.update_brewer(int(data[1].strip()))
    except FileNotFoundError as err:
        print("  Unable To Open Order File: " + str(err))


def log_items(is_people):
    global largest_team_member_id
    global largest_drink_id

    if is_people:
        if len(drinks.get_ids()) == 0:
            print(f"  You Must Add {item_type.capitalize()} Options Before You Can Add Team Members.")
            input("\n  Press Enter To Return To Menu ")
            return
        print(display_drinks(item_type, drinks))

    finished = False

    while not finished:
        add_text = f"Add Another {('Team Member' if is_people else f'{item_type.capitalize()} Option')}"
        item_name = input(f"  Enter {('Team Member Name' if is_people else f'{item_type.capitalize()} Option')}: ").strip()
        if not item_name.strip():
            print(f"  Sorry, I Did Not Understand That.")
        elif "|" in item_name or not is_people and item_name.upper() == "X":
            print(f"  Sorry, That Is Not A Valid Entry.")
        elif is_people and item_name.lower() in team_members.get_team_member_names() or not is_people and item_name.lower() in drinks.get_drinks_names():
            print(f"  Sorry, You Have Already Entered That.")
        else:
            if is_people:
                while True:
                    preference = input(f"  Enter Favourite {item_type.capitalize()} Id: ").strip()
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
                        team_member = TeamMember(item_name.lower(), int(preference), largest_team_member_id)
                        largest_team_member_id = max(largest_team_member_id, team_member.id)
                        team_members.add_team_member(team_member)
                        try:
                            with open(f"data/people_{item_type}.txt", "a") as people_records:
                                people_records.write(
                                    f"{team_member.id}|{item_name.lower()}|{preference}|{team_name}|\n")
                        except FileNotFoundError as err:
                            print("  Unable To Open Team Member File: " + str(err))
                        break
            else:
                drink = Drink(item_name.lower(), largest_drink_id)
                largest_drink_id = max(largest_drink_id, drink.id)
                drinks.add_drink(drink)
                try:
                    with open(f"data/{item_type}s.txt", "a") as drink_records:
                        drink_records.write(f"{drink.id}|{item_name.lower()}|{team_name}|\n")
                except FileNotFoundError as err:
                    print(f"  Unable To Open {item_type.capitalize()}s File: " + str(err))

        finish_check = input(f"  {add_text}? (Y/N) ").strip()
        while finish_check.upper() != "Y" and finish_check.upper() != "N":
            finish_check = input(f"  Sorry, I Did Not Understand That. {add_text}? (Y/N) ").strip()
        finished = finish_check.upper() == "N"


def update_preference():
    if len(team_members.get_ids()) == 0 or len(drinks.get_ids()) == 0:
        print(f"  You Must Add Team Members And {item_type.capitalize()} Options Before You Can Update Favourites.")
        input("\n  Press Enter To Return To Menu ")
        return

    print(display_people(item_type, team_members))
    person = ""

    while True:
        person = input("  Enter The Id Of The Person You Would Like To Update: ").strip()
        if not person.strip() or not person.isdigit() or int(person) not in team_members.get_ids():
            response = ""
            if not person.strip():
                response = input(f"  Sorry, I Did Not Understand That. Would You Still Like To Update A Favourite {item_type.capitalize()}? (Y/N) ").strip()
            else:
                response = input(f"  Sorry, That Is Not An Option. Would You Still Like To Update A Favourite {item_type.capitalize()}? (Y/N) ").strip()

            while response.upper() != "Y" and response.upper() != "N":
                response = input(f"  Sorry, I Did Not Understand That. Would You Still Like To Update A Favourite {item_type.capitalize()}? (Y/N) ").strip()
            if response.lower() == "n":
                return
        else:
            break

    print(display_drinks(item_type, drinks))
    person_name = team_members.get_team_member(int(person)).get_name()
    drink = ""

    while True:
        drink = input(f"  Enter The Id Of {person_name}'s Favourite {item_type.capitalize()}: ").strip()
        if not drink.strip() or not drink.isdigit() or int(drink) not in drinks.get_ids():
            response = ""
            if not drink.strip():
                response = input(f"  Sorry, I Did Not Understand That. Would You Still Like To Update A Favourite {item_type.capitalize()}? (Y/N) ").strip()
            else:
                response = input(f"  Sorry, That Is Not An Option. Would You Still Like To Update A Favourite {item_type.capitalize()}? (Y/N) ").strip()

            while response.upper() != "Y" and response.upper() != "N":
                response = input(f"  Sorry, I Did Not Understand That. Would You Still Like To Update A Favourite {item_type.capitalize()}? (Y/N) ").strip()
            if response.lower() == "n":
                return
        else:
            break

    team_members.get_team_member(int(person)).update_preference(int(drink))
    changes_made = False
    new_lines = []
    try:
        with open(f"data/people_{item_type}.txt", "r") as people_records:
            lines = people_records.readlines()
            for line in lines:
                if line.startswith(f"{person}|"):
                    new_lines.append(f"{person}|{person_name}|{drink}|{team_name}|\n")
                    changes_made = True
                else:
                    new_lines.append(line)
            people_records.seek(0)
            for line in new_lines:
                people_records.write(line)
    except FileNotFoundError as err:
        print("  Unable To Open Team Member File: " + str(err))

    if changes_made:
        print("  Preference Updated.")
    else:
        print("  Error: Person Could Not Be Found.")
    input("\n  Press Enter To Return To Menu ")


def update_order_records():
    lines_to_keep = []
    try:
        with open(f"data/{item_type}_order.txt", "r") as order_records:
            for line in order_records.readlines():
                data = line.split("|")
                if len(data) > 2 and data[-2] != team_name:
                    lines_to_keep.append(line)
    except FileNotFoundError as err:
        print("  Unable To Open Order File: " + str(err))
        return

    try:
        open(f'data/{item_type}_order.txt', 'w').close()
    except FileNotFoundError as err:
        print("  Unable To Open Order File: " + str(err))
        return

    try:
        with open(f"data/{item_type}_order.txt", "w") as order_records:
            for line in lines_to_keep:
                order_records.write(line)

            for drink, people in drinks_round.drinks.items():
                order_records.write(f"{drink}|{drinks_round.brewer}|")
                for person in people:
                    order_records.write(f"{person}|")
                order_records.write(f"{team_name}|\n")
    except FileNotFoundError as err:
        print("  Unable To Open Order File: " + str(err))
        return


def show_order():
    update_order_records()
    os.system("clear")
    print(ascii_images["view_order"])
    print(display_order(drinks_round, drinks, waiter))


def distribute_order():
    input(f"  Press Enter To Distribute {item_type.capitalize()}s ")
    os.system("clear")
    print(ascii_images["distribute_order"])
    print(distribute(drinks_round, drinks, team_members, item_type))
    input("\n  Press Enter To Return To Menu ")


def select_brewer():
    if len(team_members.get_ids()) == 0 or len(drinks.get_ids()) == 0:
        print(f"  You Must Add Team Members And {item_type.capitalize()} Options Before You Can Take An Order.")
        input("\n  Press Enter To Return To Menu ")
        return False

    print(display_people(item_type, team_members))
    print(f"  Type 'X' To Pick The {waiter.capitalize()} At Random\n")

    drinks_round.clear_order()
    finished = False

    while not finished:
        brewer = input(f"  Enter Person Id For {waiter.capitalize()} Of This Round: ").strip()
        if item_type == "doughnut":
            drinks_round.update_brewer(1)
            print(f"\n  The {waiter.capitalize()} Is {drinks_round.get_brewer()}!")
            time.sleep(1)
            return True
        else:
            if not brewer.strip():
                print(f"  Sorry, I Did Not Understand That.")
            elif (not brewer.isdigit() or int(brewer) not in team_members.get_ids()) and brewer.lower() != "x":
                print(f"  Sorry, That Is Not An Option.")
            else:
                if brewer.lower() != "x":
                    drinks_round.update_brewer(int(brewer))
                else:
                    drinks_round.update_brewer(random.choice(list(team_members.get_ids())))
                print(f"\n  The {waiter.capitalize()} Is {drinks_round.get_brewer()}!")
                time.sleep(1)
                return True

        finish_check = input(f"  Do You Still Want To Take An Order? (Y/N) ").strip()
        while finish_check.upper() != "Y" and finish_check.upper() != "N":
            finish_check = input(
                f"  Sorry, I Did Not Understand That. Do You Still Want To Take An Order? (Y/N) ").strip()
        finished = finish_check.upper() == "N"
    return False


def take_order():
    global any_orders

    print(display_drinks(item_type, drinks))
    print(f"  Leave Blank If No {item_type.capitalize()} Required")
    print(f"  Type 'X' To Use Their Favourite {item_type.capitalize()}\n")

    any_orders = True
    all_empty = True
    for key, person in team_members.team_members.items():
        name = person.get_name()
        preference = person.preference

        order = input(
            f"  What Is The Id Of {name}'s Desired {item_type.capitalize()}? Their Favourite {item_type.capitalize()} Is {person.get_preference()} (Id {preference}) ").strip()
        while (not order.isdigit() or int(order) not in drinks.get_ids()) and order.strip() and order.lower() != "x":
            order = input(f"  Sorry, That Is Not An Option. What Is The Id Of {name}'s Desired {item_type.capitalize()}? ").strip()
        if order.strip():
            drinks_round.add_drink(preference if order.lower() == "x" else int(order), key)
            all_empty = False

    show_order()
    if all_empty:
        input("  Press Enter To Return To Menu ")
    else:
        distribute_order()


def take_favourite_order():
    global any_orders

    any_orders = True
    for key, person in team_members.team_members.items():
        drinks_round.add_drink(person.preference, key)

    show_order()
    distribute_order()


def no_order():
    print("  No Orders Are Currently Stored.")
    input("\n  Press Enter To Return To Menu ")


def show_menu():
    global any_orders

    while True:
        os.system("clear")
        screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        screen.keypad(True)

        menu_string = ascii_images[item_type + "_menu_string"]
        screen.addstr(menu_string)
        curses.curs_set(0)
        option = 0
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

        os.system("clear")

        # add drinks options
        if option == 0:
            print(ascii_images[f"add_{item_type}_options"])
            log_items(False)
        # view drink options
        elif option == 1:
            print(ascii_images[f"view_{item_type}_options"])
            print(display_drinks(item_type, drinks))
            input("  Press Enter To Return To Menu ")
        # add team members
        elif option == 2:
            print(ascii_images["add_team_members"])
            log_items(True)
        # update favourite drink
        elif option == 3:
            print(ascii_images[f"update_favourite_{item_type}"])
            update_preference()
        # view team members
        elif option == 4:
            print(ascii_images["view_team_members"])
            print(display_people(item_type, team_members))
            input("  Press Enter To Return To Menu ")
        # take order
        elif option == 5:
            print(ascii_images[f"select_{waiter}"])
            success = select_brewer()
            if success:
                os.system("clear")
                print(ascii_images["take_order"])
                take_order()
        # take favourite order
        elif option == 6:
            print(ascii_images[f"select_{waiter}"])
            success = select_brewer()
            if success:
                os.system("clear")
                take_favourite_order()
        # view last order
        elif option == 7:
            print(ascii_images["view_last_order"])
            if any_orders:
                print(display_order(drinks_round, drinks, waiter))
                input("  Press Enter To Return To Menu ")
            else:
                no_order()
        # distribute last order
        elif option == 8:
            print(ascii_images["distribute_last_order"])
            if any_orders:
                print(distribute(drinks_round, drinks, team_members, item_type))
                input("\n  Press Enter To Return To Menu ")
            else:
                no_order()
        # clear last order
        elif option == 9:
            print(ascii_images["clear_last_order"])
            if any_orders:
                finish_check = input(f"  Are You Sure You Want To Clear The Last Order? (Y/N) ").strip()
                while finish_check.upper() != "Y" and finish_check.upper() != "N":
                    finish_check = input(
                        f"  Sorry, I Did Not Understand That. Are You Sure You Want To Clear The Last Order? (Y/N) ").strip()
                if finish_check.upper() == "Y":
                    any_orders = False
                    try:
                        open(f'data/{item_type}_order.txt', 'w').close()
                    except FileNotFoundError as err:
                        print("  Unable To Open Order File: " + str(err))
                    else:
                        print("  The Stored Last Order Has Been Cleared.")
                    input("\n  Press Enter To Return To Menu ")
            else:
                no_order()
        # change team details
        elif option == 10:
            change_password(True)
        # help
        elif option == 11:
            print(ascii_images["help"])
            print(f"  BR-IW Has Been Designed To Help Record Your {item_type.capitalize()}s Rounds.\n  If You Have Any Issues, Please Consult The User Manual.")
            input("  Press Enter To Return To Menu ")
        # logout
        elif option == 12:
            print(ascii_images["logout"])
            finish_check = input(f"  Are You Sure You Want To Logout? (Y/N) ").strip()
            while finish_check.upper() != "Y" and finish_check.upper() != "N":
                finish_check = input(f"  Sorry, I Did Not Understand That. Are You Sure You Want To Logout? (Y/N) ").strip()
            if finish_check.upper() == "Y":
                global team_name
                os.system("clear")
                team_name = ""
                drinks.clear_drinks()
                team_members.clear_team_members()
                drinks_round.clear_order()
                login(False)
        # exit
        elif option == 13:
            print(ascii_images["exit"])
            finish_check = input(f"  Are You Sure You Want To Exit? (Y/N) ").strip()
            while finish_check.upper() != "Y" and finish_check.upper() != "N":
                finish_check = input(f"  Sorry, I Did Not Understand That. Are You Sure You Want To Exit? (Y/N) ").strip()
            if finish_check.upper() == "Y":
                print(ascii_images["goodbye"])
                time.sleep(1)
                os.system("clear")
                exit()
        # bonus
        else:
            print(ascii_images["rick"])
            os.system(ascii_images["lyrics"])
            input("Press Enter To Return To Menu ")


def run_app():
    global item_type
    global waiter

    arguments = sys.argv
    if len(arguments) == 2 and arguments[1] == "mib":
        item_type = "doughnut"
        waiter = "buyer"
    read_team_data()
    login(False)
    show_menu()


if __name__ == "__main__":
    run_app()
