import os
from Source.string_helpers import ascii_images
from Source.controllers.persistence_management_controller import append_drink
from Source.classes.drink import Drink
from Source.enums import *


def log_drinks(item_type, drinks, teams):
    finished = False

    while not finished:
        add_text = f"Add Another {item_types[item_type].capitalize()} Option"
        item_name = input(f"  Enter {item_types[item_type].capitalize()} Option: ").strip()
        if not item_name.strip():
            print(f"  Sorry, I Did Not Understand That.")
        elif "|" in item_name or item_name.upper() == "X":
            print(f"  Sorry, That Is Not A Valid Entry.")
        elif item_name.lower() in drinks.get_drinks_names():
            print(f"  Sorry, You Have Already Entered That.")
        else:
            drink_id = append_drink(item_type, item_name, teams.current_team_id)
            drink = Drink(item_name.lower(), drink_id)
            drinks.add_drink(drink)

        finish_check = input(f"  {add_text}? (Y/N) ").strip()
        while finish_check.upper() != "Y" and finish_check.upper() != "N":
            finish_check = input(f"  Sorry, I Did Not Understand That. {add_text}? (Y/N) ").strip()
        finished = finish_check.upper() == "N"
        if not finished:
            os.system("clear")
            print(ascii_images[f"add_{item_types[item_type]}_options"])
