## To Set-Up And Run

1. Check out this repository `git clone git@github.com:nick-lefley-iw/br-iw.git`.
2. Change directory to `br-iw`.
3. Install dependencies from requirements.txt with `pip install -r requirements.txt`.
4. To run CLI, run `python3 -m Source.app`.
5. To run web app, run `python3 -m Source.flask_api`.


## Database Requirements

To run the either application, a database will need to be created and connected.
The required tables and columns are as follows:
+ **team**: id, name, password
+ **drink**: id, name, team_id, item_type
+ **team_member**: id, name, preference_id, team_id, item_type
+ **round**: id, brewer_id, team_id, item_type
+ **drink_order**: drink_id, team_member_id, round_id.

You will then need to set environment variables corresponding to `DB_HOST`, `DB_USER`, `DB_NAME`, `DB_PASSWORD`.


## Contribution Requirements

+ **Keep code consistent** with mine, using PyCharm's inbuilt linter as a guide. 
+ Run all tests using `pytest -m tests`. Any failures will result in pull requests being rejected.
