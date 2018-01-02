from Flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get('name')
    greeting = "Hello, %s!" % name
    render = render_template('index.html', greet=greeting)
    return render

if __name__ =="__main__":
    app.run()
