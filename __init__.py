from flask import Flask,render_template,session
import uuid

app = Flask(__name__)

app.secret_key = "1509"

@app.route('/')
def index():
    meet_id = ""
    meet_id += str(uuid.uuid1()).replace("-","")
    session['meet_id'] = meet_id
    
    return render_template('index.html',meet_id=meet_id)

@app.route('/meeting/<meeting_id>')
def meeting(meeting_id):    
    return render_template('meet.html',meeting_id=meeting_id)

if __name__ == "__main__" :
    app.run(debug=True)