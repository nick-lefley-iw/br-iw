from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from Source.controllers.persistence_management_controller import *
from Source.classes.team_members import TeamMembers
from Source.classes.drinks import Drinks
from Source.classes.round import Round
from Source.classes.teams import Teams


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class DataHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        path_elements = self.path.split("/")

        jd = None
        if len(path_elements) == 2 and path_elements[1] == "teams":
            teams = Teams()
            read_team(teams)
            jd = json.dumps(teams.teams, cls=MyEncoder)
        elif len(path_elements) == 3 and path_elements[2].isdigit():
            if path_elements[1] == "team-members":
                team_members = TeamMembers()
                read_team_member(int(path_elements[2]), team_members, 0)
                jd = json.dumps(team_members.team_members, cls=MyEncoder)
            elif path_elements[1] == "drinks":
                drinks = Drinks()
                read_drink(int(path_elements[2]), drinks, 0)
                jd = json.dumps(drinks.drinks, cls=MyEncoder)
            elif path_elements[1] == "drinks-round":
                drinks_round = Round()
                read_round(0, False, int(path_elements[2]), drinks_round)
                jd = json.dumps(drinks_round, cls=MyEncoder)

        if jd:
            self.wfile.write(jd.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
        path_elements = self.path.split("/")

        if len(path_elements) == 2 and path_elements[1] == "teams":
            append_team(data["name"], data["password"])
            self.send_response(200)
        elif len(path_elements) == 3 and path_elements[2].isdigit():
            if path_elements[1] == "team-members":
                append_team_member(data["item_type"], data["name"], int(data["preference"]), int(path_elements[2]))
                self.send_response(200)
            elif path_elements[1] == "drinks":
                append_drink(data["item_type"], data["name"], int(path_elements[2]))
                self.send_response(200)
            elif path_elements[1] == "drinks-round":
                create_round(None, int(data["brewer"]), int(path_elements[2]), data["item_type"])
                self.send_response(200)
            elif path_elements[1] == "drinks-order":
                drinks_round = Round()
                drinks_round.add_drink(int(data["drink_id"]), int(data["team_member_id"]))
                update_order_records(drinks_round, int(path_elements[2]))
                self.send_response(200)

    def do_PATCH(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
        path_elements = self.path.split("/")

        if len(path_elements) == 2:
            if path_elements[1] == "teams":
                update_team_password(data["password"], int(data["id"]))
                self.send_response(200)
            if path_elements[1] == "team-members":
                update_team_member_preference(int(data["team_member_id"]), int(data["drink_id"]))
                self.send_response(200)

    def do_DELETE(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
        path_elements = self.path.split("/")

        if len(path_elements) == 2:
            if path_elements[1] == "drinks-round":
                clear_order_records(int(data["id"]))
                self.send_response(200)


if __name__ == "__main__":
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, DataHandler)
    print("Starting server")

    httpd.serve_forever()
