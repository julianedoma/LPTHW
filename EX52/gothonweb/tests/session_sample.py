from flask import Flask, session

app = Flask(__name__)

@app.route('/count')
def count():
    if 'count' in session:
        session['count'] += 1
    else:

        session['count'] = 0
    return """
    <html>
    <head><title>Counting...</title></head>
    <body>
    Count %d
    </body>
    </html>
    """ % session['count']

app.route('/reset')
def reset():
    session.pop('count')
    return "Your session was reset."

app.secret_key = '\xd1(\xd4\x80\x01US\x91,\xa2\xc4\x87zZ\x9cL\xd2\xc9\xdfy\xfa\xb52\x87'

if __name__ == "__main__":
    app.run()
