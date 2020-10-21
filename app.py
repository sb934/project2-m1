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

# user_list = [] # global list of users
counter = 0 # global counter of users
DEFAULT_USERNAME = 'newUSERxx'

MESSAGES_RECEIVED_CHANNEL = 'message history'
USERS_RECEIVED_CHANNEL = 'user history'

AUTH_TYPE_GOOGLE = 'google'

# ---- SQLAlchemy -----
dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

sql_user = os.environ['SQL_USER']
sql_pwd = os.environ['SQL_PASSWORD']
#dbuser = os.environ['USER']

# = 'postgresql://{}:{}@localhost/postgres'.format(sql_user, sql_pwd)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #user = db.Column(db.String(100))
    text = db.Column(db.String(500))
    
    def __init__(self, a):
        self.text = a
        
    def __repr__(self):
        return '<Message Text: %s>' % self.text
        
class AppUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100))

    def __init__(self, b):
        self.user = b
        
    def __repr__(self):
        return '<User: %s>' % self.user
        
class AuthUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auth_type = db.Column(db.String(120))
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    
    def __init__(self, name, auth_type, email):
        self.name = name
        self.auth_type = auth_type
        self.email = email
        
    def __repr__(self):
        return "<User name: {}\nemail:{}\ntype: {}".format(self.name, self.email, self.auth_type)
        
        
db.create_all()
#db.session.add(Message("Hello from Joe-Bot"))
db.session.commit()

# ---- EMIT ALL MESSAGES ----
def emit_all_messages(channel):
    all_messages = [ \
        db_message.text for db_message \
        in db.session.query(Message).all()]
        
    socketio.emit(channel, {
        'allMessages': all_messages
    })
# ----- EMIT ALL USERS -----    
def emit_all_users(channel):
    all_users = [ \
        db_user.user for db_user \
        in db.session.query(AppUser).all()]
    
    socketio.emit(channel, {
        'allUsers': all_users
    })

# def push_new_user_to_db(name, email):
#     db.session.add(AuthUser(name, AUTH_TYPE_GOOGLE, email));
#     db.session.commit();
        
#     emit_all_oauth_users(USERS_UPDATED_CHANNEL)
    
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
        db.session.add(Message(response))
        db.session.commit()
    
    elif action[0].lower() == "help":
        response = "Help will always be given at MyFirstChatApp to those who ask for it... '!! about' to know about me, '!! help' to ask for me help, '!! funtranslate <dialogue>' for surprise translation, '!! kanye' to know what's Kanye West is thinking about, '!! grade' to know your grade in your class..."
        #print(response)
        # DB TODO
        db.session.add(Message(response))
        db.session.commit()
    
    elif action[0].lower() == "funtranslate":
        quote = ""
        for qu in action[1:]:
            quote = quote + qu + " "
        # translate using funtranslations
        response = funT(quote)
        #print(response)
        # DB TODO
        db.session.add(Message(response))
        db.session.commit()
    
    elif action[0].lower() == "kanye":
        response = kanye_says()
        #print(response)
        # DB TODO
        db.session.add(Message(response))
        db.session.commit()
    
    elif action[0].lower() == "grade":
        GRADE_LIST = ['A+ !','A !','B+ !','C+ !','B !','C !','D !','E !','FFFFFF in the chat !!', 'Z?']
        gr = random.choice(GRADE_LIST)
        response = "Your final grade in NOT-CS490 is " + gr
        #print(response)
        # DB TODO
        db.session.add(Message(response))
        db.session.commit()
    
    else:
        response = "You just told me something that I can't do. That's not a first... (cries in the corner)"
        print(response)
        # DB TODO
        db.session.add(Message(response))
        db.session.commit()
        

# runs when new instance of app opened
@socketio.on("connect") 
def on_connect():
    user_num = counter + 1
    user_name = DEFAULT_USERNAME+str(user_num)
    user_enter = "Hello {} from Joe-Bot".format(user_name)
    db.session.add(Message(user_enter))
    
    socketio.emit('connected', {
        'test': 'Connected'
    })
    emit_all_users(USERS_RECEIVED_CHANNEL)
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

# on new oAuth
@socketio.on('new google user')
def on_new_google_user(data):
    print("Got an event for new google user input with data:", data)
    # TODO - Push to DB 
    
# whenever new message sent from app
@socketio.on("new message")
def on_new_message(data):
    print("Got an event for new message with data:", data)
    
    message = data['message']
    
    # Add to DB - TODO
    db.session.add(Message(message))
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

# when a user closes the app     
@socketio.on("disconnect")
def on_disconnect():
    print ('Someone disconnected!')

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