from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from Source.controllers.persistence_management_controller import read_team_member, read_team, append_team_member
from Source.classes.team_members import TeamMembers
from Source.classes.team_member import TeamMember
from Source.classes.teams import Teams
from Source.apis.encoder import MyEncoder

team_members = TeamMembers()
teams = Teams()
item_type = 0


class TeamMemberHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        read_team(teams)
        teams.update_current_team("academy")
        read_team_member(teams.current_team_id, team_members, item_type)
        jd = json.dumps(team_members.team_members, cls=MyEncoder)
        self.wfile.write(jd.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
        team_member_id = append_team_member(data["item_type"], data["name"], int(data["preference"]), int(data["team_id"]))
        team_member = TeamMember(data["name"].lower(), int(data["preference"]), team_member_id)
        team_members.add_team_member(team_member)

        self.send_response(200)


if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, TeamMemberHandler)
    print("Starting server")

    httpd.serve_forever()
