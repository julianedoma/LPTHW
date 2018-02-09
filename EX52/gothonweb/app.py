from flask import Flask, session, request, url_for, redirect, abort, render_template, flash
from sqlalchemy.orm import sessionmaker
from tabledef import *
import maps, map1, map2
engine = create_engine('sqlite:///tutorial.db', echo=True)

# So this is really sad...
# My game has been working (at least the scenes and the actual game).
# Now I wanted to give it its final polish. By the attempt to do so I messed up the whole thing:(
# You can only play through it once and you will never awake from the dead again
# now you cannot even do that, over night it decided to not let me get to the game at all and identify the 'scene' as a KeyError.

# The coolest thing of the whole game however, is the helpfunction is only seen in the scenes.

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect (url_for('choose_map'))

def index():
    if 'username' in session:
       username = session['username']
       session['Scene'] = map1.START.urlname
       return redirect(url_for('game_get'))
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_admin_login():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return render_template('welcome.html')

@app.route('/test') # test works.. yeahhhy :)
def test():

    POST_USERNAME = "python"
    POST_PASSWORD = "python"

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        return "Object found"
    else:
        return "Object not found" + POST_USERNAME + " " + POST_PASSWORD

@app.route("/logout")
def logout():
    session['logged_in'] = False
    #session.pop('logged_in', None)
    return home()

@app.route('/signup', methods=['GET'])
def signup_get():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    Session = sessionmaker(bind=engine)
    session = Session()

    username = str(request.form['username'])
    password = str(request.form['password'])


    user = User('username', 'password')
    session.add(user)

    session.commit()
    session.commit()

    return redirect(url_for('welcome'))

@app.route('/welcome', methods=['GET'])
def choose_map():
    return render_template('welcome.html')
    if nextscene == None:
        # session.pop('scene')
        username = session['username']
        session['Scene'] = map1.START.urlname
        return render_template('show_scene.html')

@app.route('/welcome', methods=['POST'])
def choose_planet():
    pass
    # if 'action' == 'moon':
    #     thescene = map2.SCENES[session['scene']]
    #     return render_template('show_scene.html', scene=thescene)
    # elif 'action' == 'mars':
    #     thescene = map2.SCENES[session['scene']]
    #     return render_template('show_scene.html', scene=thescene)
    # else:
    #     pass


@app.route('/game', methods=['GET'])
def game_get():
    userinput = request.form.get('userinput')
    currentscene = map1.SCENES[session['Scene']]
    nextscene = currentscene.go(userinput)

    if 'Scene' in session:
        thescene = map1.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        session['Scene'] = map1.START.urlname
        return render_template('show_scene.html') #####start at the beginning???

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'Scene' in session:
        if userinput is None:
            pass
            # return render_template('show_Scene2.html') # this does not want to display...
        else:
            currentscene = map1.SCENES[session['Scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                username = session['username']
                #session['scene'] = map1.START.urlname
                return session.pop('Scene')
                #render_template('show_scene.html')
            else:
                session['Scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        return render_template('welcome.html')


app.secret_key = 'g7hFm9UYyS23RHd3V5pGlnqJZmw6G7S8'


if __name__ == '__main__':

    app.run(debug=True) # OMG this is sooo useful :)
