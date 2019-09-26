import pymysql
from os import environ
from Source.classes.team import Team
from Source.classes.drink import Drink
from Source.classes.team_member import TeamMember


def return_connection_string():
    return pymysql.connect(environ.get("DB_HOST"), environ.get("DB_USER"), environ.get("DB_PASSWORD"), environ.get("DB_NAME"))


def select_sql(sql_string):
    connection = return_connection_string()
    rows = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_string)
            rows = cursor.fetchall()
    except:
        print("  Unable To Retrieve Data")
    finally:
        connection.close()
        return rows


def update_sql(sql_string):
    connection = return_connection_string()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_string)
        connection.commit()
    except:
        print("  Unable To Retrieve Data")
    finally:
        connection.close()


def append_team(item_name, password):
    update_sql(f"INSERT INTO team(name, password) VALUES ('{item_name.lower()}', '{password}')")
    new_id = select_sql(f"SELECT MAX(id) from team")[0][0]

    return new_id


def update_team_password(new_password, current_team_id):
    update_sql(f"UPDATE team SET password = '{new_password}' WHERE id = {current_team_id}")


def read_team(teams):
    for row in select_sql("SELECT * FROM team"):
        teams.add_team(Team(row[1], row[2], row[0]))


def read_drink(current_team_id, drinks, item_type):
    for row in select_sql(f"SELECT * FROM drink WHERE team_id = {current_team_id} AND item_type = {item_type}"):
        drinks.add_drink(Drink(row[1], row[0]))


def read_team_member(current_team_id, team_members, item_type):
    for row in select_sql(f"SELECT * FROM team_member WHERE team_id = {current_team_id} AND item_type = {item_type}"):
        team_members.add_team_member(TeamMember(row[1], row[2], row[0]))


def read_round(item_type, any_orders, current_team_id, drinks_round):
    for row in select_sql(f"SELECT r.id, r.brewer_id, d.drink_id, d.team_member_id FROM round r LEFT JOIN drink_order d on r.id = d.round_id WHERE r.team_id = {current_team_id} and r.item_type = {item_type}"):
        drinks_round.update_id(row[0])
        drinks_round.update_brewer(row[1])
        if row[2]:
            any_orders = True
            drinks_round.add_drink(row[2], row[3])

    return any_orders


def append_team_member(item_type, item_name, preference, current_team_id):
    update_sql(f"INSERT INTO team_member(name, preference_id, team_id, item_type) VALUES ('{item_name.lower()}', {preference}, {current_team_id}, {item_type})")
    new_id = select_sql(f"SELECT MAX(id) from team_member")[0][0]

    return new_id


def append_drink(item_type, item_name, current_team_id):
    update_sql(f"INSERT INTO drink(name, team_id, item_type) VALUES ('{item_name.lower()}', {current_team_id}, {item_type})")
    new_id = select_sql(f"SELECT MAX(id) from drink")[0][0]

    return new_id


def update_team_member_preference(person, drink):
    update_sql(f"UPDATE team_member SET preference_id = {drink} WHERE id = {person}")


def create_round(old_id, brewer, current_team_id, item_type):
    if old_id:
        clear_order_records(old_id)

    update_sql(f"INSERT INTO round(brewer_id, team_id, item_type) VALUES ({brewer}, {current_team_id}, {item_type})")
    new_id = select_sql(f"SELECT MAX(id) from round")[0][0]
    return new_id


def update_order_records(drinks_round, round_id):
    insert_sql = "INSERT INTO drink_order(drink_id, team_member_id, round_id) VALUES "
    for drink, people in drinks_round.drinks.items():
        for person in people:
            insert_sql += f"({drink}, {person}, {round_id}), "
    update_sql(insert_sql[:-2])


def clear_order_records(old_id):
    update_sql(f"DELETE FROM drink_order WHERE round_id = {old_id}")
    update_sql(f"DELETE FROM round WHERE id = {old_id}")
