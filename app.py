from flask import Flask, render_template, send_file, send_from_directory
from markupsafe import escape
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/shared/<path:filename>')
def serve_file(filename):
    return send_file(f'shared/{filename}')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/shared/uploaded_file.txt')

@app.route('/shared')
def directory_listing():
    # Get a list of files in the directory and its subdirectories
    files = []
    for root, dirs, filenames in os.walk('shared'):
        for filename in filenames:
            files.append(os.path.relpath(os.path.join(root, filename), 'shared'))
        print(filenames)
    # Render the template with the file list
    return render_template('directory.html', filenames=filenames)

@app.route("/noaa")
def noaa():
    output = "Here we will munge some data from the NOAA and other agencies, and chart it with visualizations from D3js.org and IPython Notebooks utilizing NumPy and SciPy.  Tablau hosts some <a href='https://www.tableau.com/learn/articles/free-public-data-sets'>Free public datasets on climate and environment</a>" 
    return output

@app.route("/doge")
def doge():
    output = "Here we will munge some data from the U.S. Budget, Bureaucratic organization, Yearly Deficit, Debt, and Current Account Balances in Bilateral Trade relationships."
    output = output + "We will chart these with visualizations from D3js.org and IPython Notebooks utilizing NumPy and SciPy."
    output = output + "We will apply the analysis and contribute to the free and open-source education project <a href='http://en.wikiversity.org/wiki/User:Jaredscribe/Department_of_Government_Efficiency'>en.wikiversity.org/wiki/User:Jaredscribe/Department_of_Government_Efficiency</a>"  
    output = output + "<a href='http://Data.gov'>Data.gov is 'The Home of the U.S. Government's Open Data'</a> boasting 307,851 datasets available"
    return output

@app.route("/datetime")
def hello_world():
    return "<p>Hello, World!  It is now: " + datetime.datetime.now().strftime("%A, %d %B, %Y at %X") + "<a href=/goodbye>Say goodbye</a></p>"

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
    return render_template('hello.html', my_dict=seq, n=n)
