from flask import Flask, jsonify, redirect, request, render_template, session
from Source.classes.teams import Teams
from Source.classes.team_members import TeamMembers
from Source.classes.drinks import Drinks
from Source.classes.round import Round
from Source.controllers.persistence_management_controller import *

app = Flask(__name__)
teams = Teams()
app.secret_key = 'any random string'


@app.route("/teams", methods=["GET", "POST", "PATCH"])
def team_handler():
    if request.method == "GET":
        return jsonify([team.__dict__ for team in teams.teams.values()])
    elif request.method == "POST":
        append_team(request.form["name"], request.form["password"])
        return request.args
    elif request.method == "PATCH":
        if "password" in request.form.keys():
            update_team_password(request.form["password"], int(request.form["id"]))
        if "name" in request.form.keys():
            update_team_name(request.form["name"], int(request.form["id"]))
        return request.args


@app.route("/team-members", methods=["GET", "POST"])
def team_member_handler():
    if 'username' in session:
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
            team_members = TeamMembers()
            read_team_member(int(request.args["team_id"]), team_members, 0)
            return redirect("/team-members?team_id=" + str(request.args["team_id"]))
    else:
        return redirect("/login")


@app.route("/drinks", methods=["GET", "POST"])
def drink_handler():
    if 'username' in session:
        if request.method == "GET":
            drinks = Drinks()
            read_drink(int(request.args["team_id"]), drinks, 0)
            return render_template("drinks.html", drink_page="active", data=[drink.to_json() for drink in drinks.drinks.values()], team_id=request.args["team_id"])
        elif request.method == "POST":
            append_drink(0, request.form["drinkName"], int(request.args["team_id"]))
            return redirect("/drinks?team_id=" + str(request.args["team_id"]))
    else:
        return redirect("/login")


@app.route("/drinks-round", methods=["GET", "POST", "DELETE"])
def drink_round_handler():
    if request.method == "GET":
        drinks_round = Round()
        read_round(0, False, int(request.args["team_id"]), drinks_round)
        return jsonify(drinks_round.to_json())
    elif request.method == "POST":
        create_round(None, int(request.form["brewer"]), int(request.args["team_id"]), request.form["item_type"])
        return request.args
    elif request.method == "DELETE":
        clear_order_records(int(request.form["id"]))
        return request.args


@app.route("/drinks-order", methods=["GET", "POST"])
def drink_order_handler():
    if request.method == "POST":
        drinks_round = Round()
        drinks_round.add_drink(Drink("", int(request.form["drink_id"])), TeamMember("", 0, int(request.form["team_member_id"])))
        update_order_records(drinks_round, int(request.args["team_id"]))
        return request.args


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
    if 'username' in session:
        if request.method == "GET":
            return render_template('home.html', title="Create Form", team_id=request.args["team_id"])
    else:
        return redirect("/login")


@app.route("/logout", methods=["GET"])
def logout_handler():
    if 'username' in session:
        if request.method == "GET":
            session.pop('username', None)
            return redirect("/login")
    else:
        return redirect("/login")


if __name__ == "__main__":
    read_team(teams)
    app.run(host="localhost", port=8080)
