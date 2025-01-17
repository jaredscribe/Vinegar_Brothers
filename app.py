from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/world")
def hello_world():
    return "<p>Hello, World!  <a href=/goodbye>Say goodbye</a></p>"

@app.route("/goodbye")
@app.route("/goodbye/<name>")
def goodbye_world(name=None):
    # "<p>Goodbye, World!  <a href=/>Say hello</a></p>"
    return render_template('hello.html', saying="goodbye", person=name)

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', saying="hello", person=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/fib')
@app.route('/fib/<int:n>')
def fib(n=None):    # write Fibonacci series up to n
    # modified version of https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
    """Print a Fibonacci series up to n."""
    print('Print again Fibonacci series up to', n, "on the console, and send it over HTTP")
    seq=[]
    i=1
    a, b = 0, 1
    if (n==None): 
        n=500
    while a < n:
        print(i, a, end=' ')
        seq.append((i,a))
        a, b = b, a+b
        i=i+1
    return render_template('hello.html', my_dict=seq)
