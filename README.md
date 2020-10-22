project2-m2

# CS490-Project2
## Online chatting web application with a chatbot

### Languages used:
- Python
- React-Javascript
- HTML/CSS
- SQL

#### App is based on a client-server architecture and communicates using socket.io. Backend is developed using Python with PostgreSQL, Flask, Sockets, APIs, SQLAlchemy. Frontend is developed using React Components (Functional) and styled using HTML/CSS. 

### APIs Used: 
- Funtranslate - https://funtranslations.com/api/ 
- Kanye - https://kanye.rest/ 
- Google OAuth - https://developers.google.com/identity/protocols/oauth2 

### Instructions
pip or any up to date de facto standard package-managment system will be needed for installing modules.

- To install flask: `pip install flask`
- Other requirements: `pip install flask-socketio` && `pip install eventlet`
- Run the following in order in the same working directory as the project: `npm install` && `npm install -g webpack` && `npm install --save-dev webpack` && `npm install socket.io-client --save`

* IGNORE WARNING MESSAGES
* IF ANY ERROR MESSAGES OCCUR: Try using `sudo pip` OR `sudo [path to pip from which pip] install` OR `sudo npm`

### Set Up DB: PostGreSQL 
- Install PostGreSQL: `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`
- Initialize PSQL database: `sudo service postgresql initdb`
- Start PSQL: `sudo service postgresql start`
- Make a new superuser: `sudo -u postgres createuser --superuser $USER`
- Make a new database: `sudo -u postgres createdb $USER`
- Make sure your user shows up: `psql` && `\du` for users && `\l` for database
- Make a new user (REPLACE VALUES IN THIS COMMAND! Type with a new (short) password): 
  a) `psql`
  b) `create user [some_username_here] superuser password '[some_unique_new_password_here]';`
  c) `\q`
- In the main working directory, make a new file called `sql.env` and add `SQL_USER=` and `SQL_PASSWORD=` in it

### Enabling read/write from SQLAlchemy
- Open the file in vim: `sudo vim /var/lib/pgsql9/data/pg_hba.conf`
- Replace all values of ident with md5 in Vim: `:%s/ident/md5/g`
- After changing those lines, run `sudo service postgresql restart`

### For Google OAuth:
- Refer to https://www.npmjs.com/package/react-google-login 
- Change client app id in `/Scripts/GoogleButton.jsx`

### Run your code! 
  a) `npm run watch`  
  b) `python app.py` in new terminal
  
### Issues and Improvements
- Styling changes required. The app is functional with all working components dumped. The webpage needs to be redesigned and structured. 
- Send button only pops up after successful Google oAuth. That enables messages to sent with sender's name. However, message can be sent without login using `Return` key instead of button. 
- List of Active Users is being updated upon new connections. However, it is not being updated when a client disconnects. 
- Valid URL's are being checked in the backend however, they are not being formatted and rendered on the front-end. (Same for Image URIs)

##### WILL KEEP UPDATING THIS REPO IN THE COMING WEEKS! STAY TUNED!!!!

