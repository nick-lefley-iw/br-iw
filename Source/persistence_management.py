from Source.classes import *


def update_team_password(team_name, new_password):
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
        return None

    try:
        open('data/teams.txt', 'w').close()
    except FileNotFoundError as err:
        print("  Unable To Open Teams File: " + str(err))
        return None

    try:
        with open("data/teams.txt", "w") as order_records:
            for line in lines_to_keep:
                order_records.write(line)
            order_records.write(f"{old_id}|{team_name}|{new_password}|\n")
    except FileNotFoundError as err:
        print("  Unable To Open Teams File: " + str(err))
        return None

    return old_id


def read_team():
    try:
        with open("data/teams.txt", "r") as team_records:
            for line in team_records:
                data = line.split("|")
                teams.add_team(Team(data[1].strip(), data[2].strip(), int(data[0].strip())))
    except FileNotFoundError as err:
        print("  Unable To Open Teams File: " + str(err))


def read_data(item_type, team_name, any_orders, largest_team_member_id, largest_drink_id):

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

    return any_orders, largest_team_member_id, largest_drink_id


def append_team_member(item_type, team_member, item_name, preference, team_name):
    try:
        with open(f"data/people_{item_type}.txt", "a") as people_records:
            people_records.write(
                f"{team_member.id}|{item_name.lower()}|{preference}|{team_name}|\n")
    except FileNotFoundError as err:
        print("  Unable To Open Team Member File: " + str(err))


def append_drink(item_type, drink, item_name, team_name):
    try:
        with open(f"data/{item_type}s.txt", "a") as drink_records:
            drink_records.write(f"{drink.id}|{item_name.lower()}|{team_name}|\n")
    except FileNotFoundError as err:
        print(f"  Unable To Open {item_type.capitalize()}s File: " + str(err))


def update_team_member_preference(item_type, person, person_name, drink, team_name):
    changes_made = False
    new_lines = []
    try:
        with open(f"data/people_{item_type}.txt", "r+") as people_records:
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

    return changes_made


def update_order_records(item_type, team_name):
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


def clear_order_records(item_type):
    try:
        open(f'data/{item_type}_order.txt', 'w').close()
    except FileNotFoundError as err:
        print("  Unable To Open Order File: " + str(err))
    else:
        print("  The Stored Last Order Has Been Cleared.")
