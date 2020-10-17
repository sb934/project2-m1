import flask
from os.path import join, dirname
from dotenv import load_dotenv
import flask_socketio
import os
import random
import flask_sqlalchemy
import requests as r

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

user_list = [] # global list of users
counter = 0 # global counter of users
DEFAULT_USERNAME = 'newUSERxx'

MESSAGES_RECEIVED_CHANNEL = 'message history'

# ---- SQLAlchemy -----
dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

sql_user = os.environ['SQL_USER']
sql_pwd = os.environ['SQL_PASSWORD']
#dbuser = os.environ['USER']

database_uri = 'postgresql://{}:{}@localhost/postgres'.format(sql_user, sql_pwd)

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

import models

db.create_all()
db.session.commit()

def emit_all_messages(channel):
    all_messages = [ \
        db_message.text for db_message \
        in db.session.query(models.Message).all()]
        
    socketio.emit(channel, {
        'allMessages': all_messages
    })
    
# ----- HELPER FUNCTIONS -----
import requests as r 
import json

# Funtranslations API - 5 requests per hour only. 
def funT(q):
    url = "https://api.funtranslations.com/translate/groot.json"
    params = {"text":q}
    response = (r.get(url,params=params))
    response = response.json()
    translated_txt = response["contents"]["translated"]
    return translated_txt

# Kanye West API - OpenSource Free API
def kanye_says():
    url = "https://api.kanye.rest/"
    response = r.get(url)
    response = response.json()
    kanye_txt = response["quote"]
    return kanye_txt
    

def bot_will_respond(action):
    if action[0].lower() == 'about':
        response = "It's JoeBot. Not Joe average Bot"
        # print(response)
        # DB TODO
        db.session.add(models.Message(response))
        db.session.commit()
    
    elif action[0].lower() == "help":
        response = "Help will always be given at MyFirstChatApp to those who ask for it... '!! about' to know about me, '!! help' to ask for me help, '!! funtranslate <dialogue>' for surprise translation, '!! kanye' to know what's Kanye West is thinking about, '!! grade' to know your grade in your class..."
        #print(response)
        # DB TODO
        db.session.add(models.Message(response))
        db.session.commit()
    
    elif action[0].lower() == "funtranslate":
        quote = ""
        for qu in action[1:]:
            quote = quote + qu + " "
        # translate using funtranslations
        response = funT(quote)
        #print(response)
        # DB TODO
        db.session.add(models.Message(response))
        db.session.commit()
    
    elif action[0].lower() == "kanye":
        response = kanye_says()
        #print(response)
        # DB TODO
        db.session.add(models.Message(response))
        db.session.commit()
    
    elif action[0].lower() == "grade":
        GRADE_LIST = ['A+ !','A !','B+ !','C+ !','B !','C !','D !','E !','FFFFFF in the chat !!', 'Z?']
        gr = random.choice(GRADE_LIST)
        response = "Your final grade in NOT-CS490 is " + gr
        #print(response)
        # DB TODO
        db.session.add(models.Message(response))
        db.session.commit()
    
    else:
        response = "You just told me something that I can't do. That's a first... (cries in the corner)"
        print(response)
        # DB TODO
        db.session.add(models.Message(response))
        db.session.commit()
        



# runs when new instance of app opened
@socketio.on("connect") 
def on_connect():
    user_num = counter + 1
    user_name = DEFAULT_USERNAME+str(user_num)
    
    socketio.emit('connected', {
        'test': 'Connected'
    })
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

# whenever new message sent from app
@socketio.on("new message")
def on_new_message(data):
    print("Got an event for new message with data:", data)
    
    message = data['message']
    
    # Add to DB - TODO
    db.session.add(models.Message(message))
    db.session.commit()
    
    # Check if message for Bot 
    if message.split()[0] == '!!':
        print("Message is for the bot")
        
        # Send string to helper function for bot-commands
        bot_will_respond(message.split()[1:])
     
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    
    # socketio.emit('message received', {
    #     'message': message
    # })
    
@socketio.on("disconnect")
def on_disconnect():
    print ('Someone disconnected!')

#import models

@app.route('/')
def hello():
    return flask.render_template('index.html')


if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )