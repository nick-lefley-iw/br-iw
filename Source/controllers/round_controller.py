import os
import random
import time
from Source.string_helpers import ascii_images, display_order, display_people, distribute, display_drinks
from Source.controllers.persistence_management_controller import update_order_records, create_round, clear_order_records
from Source.enums import *


def show_order(old_id, item_type, drinks_round, drinks, teams, team_members):
    new_id = create_round(old_id, drinks_round.brewer, teams.current_team_id, item_type)
    update_order_records(drinks_round, new_id)
    drinks_round.update_id(new_id)
    os.system("clear")
    print(ascii_images["view_order"])
    print(display_order(drinks_round, drinks, item_type, team_members))


def distribute_order(item_type, drinks_round, drinks, team_members):
    input(f"  Press Enter To Distribute {item_types[item_type].capitalize()}s ")
    os.system("clear")
    print(ascii_images["distribute_order"])
    print(distribute(drinks_round, drinks, team_members, item_type))
    input("\n  Press Enter To Return To Menu ")


def select_brewer(item_type, team_members, drinks, drinks_round):
    if len(team_members.get_ids()) == 0 or len(drinks.get_ids()) == 0:
        print(f"  You Must Add Team Members And {item_types[item_type].capitalize()} Options Before You Can Take An Order.")
        input("\n  Press Enter To Return To Menu ")
        return False

    print(display_people(item_type, team_members, drinks))
    print(f"  Type 'X' To Pick The {waiter_types[item_type].capitalize()} At Random\n")

    drinks_round.clear_order()
    finished = False

    while not finished:
        brewer = input(f"  Enter Person Id For {waiter_types[item_type].capitalize()} Of This Round: ").strip()
        if not brewer.strip():
            print(f"  Sorry, I Did Not Understand That.")
        elif (not brewer.isdigit() or int(brewer) not in team_members.get_ids()) and brewer.lower() != "x":
            print(f"  Sorry, That Is Not An Option.")
        else:
            if brewer.lower() != "x":
                drinks_round.update_brewer(int(brewer))
            else:
                drinks_round.update_brewer(random.choice(list(team_members.get_ids())))
            print(f"\n  The {waiter_types[item_type].capitalize()} Is {drinks_round.get_brewer(team_members)}!")
            time.sleep(1)
            return True

        finish_check = input(f"  Do You Still Want To Take An Order? (Y/N) ").strip()
        while finish_check.upper() != "Y" and finish_check.upper() != "N":
            finish_check = input(
                f"  Sorry, I Did Not Understand That. Do You Still Want To Take An Order? (Y/N) ").strip()
        finished = finish_check.upper() == "N"
    return False


def take_order(old_id, item_type, drinks, team_members, drinks_round, teams):
    print(display_drinks(item_type, drinks))
    print(f"  Leave Blank If No {item_types[item_type].capitalize()} Required")
    print(f"  Type 'X' To Use Their Favourite {item_types[item_type].capitalize()}\n")

    all_empty = True
    for key, person in team_members.team_members.items():
        name = person.get_name()
        preference = person.preference

        order = input(
            f"  What Is The Id Of {name}'s Desired {item_types[item_type].capitalize()}? Their Favourite {item_types[item_type].capitalize()} Is {person.get_preference(drinks)} (Id {preference}) ").strip()
        while (not order.isdigit() or int(order) not in drinks.get_ids()) and order.strip() and order.lower() != "x":
            order = input(f"  Sorry, That Is Not An Option. What Is The Id Of {name}'s Desired {item_types[item_type].capitalize()}? ").strip()
        if order.strip():
            drinks_round.add_drink(preference if order.lower() == "x" else int(order), key)
            all_empty = False

    show_order(old_id, item_type, drinks_round, drinks, teams, team_members)
    if all_empty:
        input("  Press Enter To Return To Menu ")
    else:
        distribute_order(item_type, drinks_round, drinks, team_members)


def take_favourite_order(old_id, item_type, team_members, drinks_round, drinks, teams):
    for key, person in team_members.team_members.items():
        drinks_round.add_drink(person.preference, key)

    show_order(old_id, item_type, drinks_round, drinks, teams, team_members)
    distribute_order(item_type, drinks_round, drinks, team_members)


def no_order():
    print("  No Orders Are Currently Stored.")
    input("\n  Press Enter To Return To Menu ")


def clear_last_order(any_orders, drinks_round):
    if any_orders:
        finish_check = input(f"  Are You Sure You Want To Clear The Last Order? (Y/N) ").strip()
        while finish_check.upper() != "Y" and finish_check.upper() != "N":
            finish_check = input(
                f"  Sorry, I Did Not Understand That. Are You Sure You Want To Clear The Last Order? (Y/N) ").strip()
        if finish_check.upper() == "Y":
            any_orders = False
            clear_order_records(drinks_round.id)
            print("  The Stored Last Order Has Been Cleared.")
            input("\n  Press Enter To Return To Menu ")
    else:
        no_order()

    return any_orders
