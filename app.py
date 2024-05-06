from flask import Flask, request, jsonify
import ipl

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!!'

@app.route('/api/teams')
def teams():
    teams=ipl.teamsapi()
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamvteam():
    team1=request.args.get('team1')
    team2=request.args.get('team2')
    response=ipl.teamsvsteams(team1, team2)
    return jsonify(response)


app.run(port=5000, debug=True)