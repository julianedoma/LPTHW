from Flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    usergreet = request.args.get('greet')
    username = request.args.get('name')
    if usergreet is None or usergreet == "":
        usergreet = "Hello"
    if username is None or username == "":
        username = "Nobody"
    greeting = "%S, %s!" % (usergreet, username)
    render = render_template('index.html', greet=greeting)
    return render

if __name__ =="__main__":
    app.run()
