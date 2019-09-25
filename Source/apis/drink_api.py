from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from Source.controllers.persistence_management_controller import read_drink, read_team, append_drink
from Source.classes.drinks import Drinks
from Source.classes.drink import Drink
from Source.classes.teams import Teams
from Source.apis.encoder import MyEncoder

drinks = Drinks()
teams = Teams()
item_type = 0


class DrinkHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        read_team(teams)
        teams.update_current_team("academy")
        read_drink(teams.current_team_id, drinks, item_type)
        jd = json.dumps(drinks.drinks, cls=MyEncoder)
        self.wfile.write(jd.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
        drink_id = append_drink(data["item_type"], data["name"], data["team_id"])
        drink = Drink(data["name"].lower(), drink_id)
        drinks.add_drink(drink)

        self.send_response(200)


if __name__ == "__main__":
    httpd = HTTPServer(('', 8081), DrinkHandler)
    print("Starting server")

    httpd.serve_forever()
