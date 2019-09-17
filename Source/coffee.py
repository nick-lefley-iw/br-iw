import sys
team_members = []
drinks = []


def log_items(is_people):
    finished = False
    while not finished:
        enter_text = "Enter " + ("Team Member" if is_people else "Drink") + " Name: "
        add_text = "Add Another " + ("Team Member" if is_people else "Drink")
        item_name = input(enter_text)
        while len(item_name) == 0:
            item_name = input("Sorry, I Didn't Understand That." + enter_text)
        if is_people:
            team_members.append(item_name)
        else:
            drinks.append(item_name)
        finish_check = input(add_text + "? (Y/N) ")
        while finish_check != "Y" and finish_check != "N":
            finish_check = input("Sorry, I Didn't Understand That. " + add_text + "? (Y/N) ")
        finished = finish_check == "N"
    if is_people:
        print(team_members)
    else:
        print(drinks)


arguments = sys.argv
if len(arguments) != 2:
    print("Command Not Defined")
elif arguments[1] == "get-people":
    log_items(True)
elif arguments[1] == "get-drinks":
    log_items(False)
else:
    print("Command Not Defined")

