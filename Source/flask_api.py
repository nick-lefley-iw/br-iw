from flask import Flask, redirect, request, render_template, session
from Source.classes.teams import Teams
from Source.classes.team_members import TeamMembers
from Source.classes.drinks import Drinks
from Source.classes.round import Round
from Source.controllers.persistence_management_controller import *

app = Flask(__name__)
teams = Teams()
app.secret_key = 'any random string'


@app.route("/settings", methods=["GET", "POST"])
def settings_handler():
    if 'username' in session and teams.current_team_id:
        if request.method == "GET":
            return render_template("settings.html", settings_page="active", data=teams.current_team_name.title(), team_id=request.args["team_id"], is_hidden="none")
        elif request.method == "POST":
            team_name = teams.current_team_name
            if "newPassword" in request.form.keys():
                if request.form["oldPassword"] != teams.current_team_password:
                    return render_template("settings.html", settings_page="active", data=teams.current_team_name.title(), team_id=request.args["team_id"], open_modal="open-modal")
                update_team_password(request.form["newPassword"], int(request.args["team_id"]))
            if "teamName" in request.form.keys():
                update_team_name(request.form["teamName"], int(request.args["team_id"]))
                team_name = request.form["teamName"]
            read_team(teams)
            teams.update_current_team(team_name)
            return render_template("settings.html", settings_page="active", data=teams.current_team_name.title(), team_id=request.args["team_id"], is_hidden="none")
    else:
        return redirect("/login")


@app.route("/team-members", methods=["GET", "POST"])
def team_member_handler():
    if 'username' in session and teams.current_team_id:
        if request.method == "GET":
            team_members = TeamMembers()
            read_team_member(int(request.args["team_id"]), team_members, 0)
            drinks = Drinks()
            read_drink(int(request.args["team_id"]), drinks, 0)
            drink_options = [drink.to_json() for drink in drinks.drinks.values()]
            return render_template("team_members.html", team_member_page="active", data=[team_member.to_json() for team_member in team_members.team_members.values()], team_id=request.args["team_id"], drink_options=drink_options)
        elif request.method == "POST":
            if int(request.form["id"]) == 0:
                append_team_member(0, request.form["teamMemberName"], int(request.form["teamMemberPreference"]), int(request.args["team_id"]))
            else:
                update_team_member(int(request.form["id"]), request.form["teamMemberName"], int(request.form["teamMemberPreference"]))
            return redirect("/team-members?team_id=" + str(request.args["team_id"]))
    else:
        return redirect("/login")


@app.route("/drinks", methods=["GET", "POST"])
def drink_handler():
    if 'username' in session and teams.current_team_id:
        if request.method == "GET":
            drinks = Drinks()
            read_drink(int(request.args["team_id"]), drinks, 0)
            return render_template("drinks.html", drink_page="active", data=[drink.to_json() for drink in drinks.drinks.values()], team_id=request.args["team_id"])
        elif request.method == "POST":
            if int(request.form["id"]) == 0:
                append_drink(0, request.form["drinkName"], int(request.args["team_id"]))
            else:
                update_drink(int(request.form["id"]), request.form["drinkName"])
            return redirect("/drinks?team_id=" + str(request.args["team_id"]))
    else:
        return redirect("/login")


@app.route("/drinks-round", methods=["GET", "POST", "DELETE"])
def drink_round_handler():
    if 'username' in session and teams.current_team_id:
        if request.method == "GET":
            drinks_round = Round()
            read_round(0, False, int(request.args["team_id"]), drinks_round)
            team_members = TeamMembers()
            read_team_member(int(request.args["team_id"]), team_members, 0)
            brewer_options = [team_member.to_json() for team_member in team_members.team_members.values()]
            drinks = Drinks()
            read_drink(int(request.args["team_id"]), drinks, 0)
            drink_options = [drink.to_json() for drink in drinks.drinks.values()]
            return render_template("drinks_round.html", round_page="active", data=drinks_round.to_json(), team_id=request.args["team_id"], round_id=drinks_round.id, show_if_round=("" if drinks_round.id else "none"), brewer_options=brewer_options, drink_options=drink_options, open_order_modal=("open-modal" if "add_order" in request.args else ""), open_round_modal=("open-modal" if "start_round" in request.args else ""))
        elif request.method == "POST":
            round_id = None if request.form["id"] == "None" or int(request.form["id"]) == 0 else int(request.form["id"])
            if request.form["clear-order"] == "true":
                new_id = create_round(round_id, int(request.form["roundBrewer"]), int(request.args["team_id"]), 0)
                if request.form["prepopulate"] == "true":
                    drinks_round = Round()
                    team_members = TeamMembers()
                    read_team_member(int(request.args["team_id"]), team_members, 0)
                    for person in team_members.team_members.values():
                        drinks_round.add_drink(person.preference, person)
                    update_order_records(drinks_round, new_id)
            else:
                update_brewer(round_id, int(request.form["roundBrewer"]))
            return redirect("/drinks-round?team_id=" + str(request.args["team_id"]))
        elif request.method == "DELETE":
            clear_order_records(int(request.args["id"]))
            return request.args
    else:
        return redirect("/login")


@app.route("/drinks-order", methods=["POST", "DELETE"])
def drink_order_handler():
    if 'username' in session and teams.current_team_id:
        if request.method == "POST":
            add_order(int(request.args["drink_id"]), int(request.args["round_id"]), int(request.args["team_member_id"]))
            return request.args
        if request.method == "DELETE":
            if "drink_id" in request.args:
                delete_orders_for_drink(int(request.args["round_id"]), int(request.args["drink_id"]))
            elif "team_member_id" in request.args:
                delete_order_for_team_member(int(request.args["round_id"]), int(request.args["team_member_id"]))
            return request.args
    else:
        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login_handler():
    if request.method == "GET":
        return render_template('login.html', title="Create Form", is_hidden="none")
    elif request.method == "POST":
        if request.form["teamName"].lower() not in teams.get_team_names():
            return render_template('login.html', title="Create Form", teamName=request.form["teamName"])
        teams.update_current_team(request.form["teamName"])
        if teams.current_team_password != request.form["teamPassword"]:
            return render_template('login.html', title="Create Form", teamName=request.form["teamName"])
        else:
            session['username'] = "test"
            return redirect('/home?team_id=' + str(teams.current_team_id))


@app.route("/home", methods=["GET"])
def home_handler():
    if 'username' in session and teams.current_team_id:
        if request.method == "GET":
            return render_template('home.html', title="Create Form", team_id=request.args["team_id"])
    else:
        return redirect("/login")


@app.route("/logout", methods=["GET"])
def logout_handler():
    if 'username' in session and teams.current_team_id:
        if request.method == "GET":
            session.pop('username', None)
            return redirect("/login")
    else:
        return redirect("/login")


if __name__ == "__main__":
    read_team(teams)
    app.run(host="0.0.0.0", port=8080, debug=True)
