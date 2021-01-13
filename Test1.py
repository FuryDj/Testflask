from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def homepage():
    return "Homepage"

@app.route("/new/")
def query_strings(greeting="Good Afternoon"):
    query_val = request.args.get("greeting", greeting)
    return "<h1> The greeting is: {0} </h1>".format(query_val)

@app.route("/user")
@app.route("/user/<name>")
def no_query_string(name="Mina"):
    return f"Hello {name}!"

# STRINGS
@app.route("/text/<string:name>")
def working_with_strings(name):
    return "<h1> here is a string " + name +" </h1>"

# NUMBERS
@app.route("/numbers/<int:name>")
def working_with_numbers(name):
    return "<h1> here is a number " + str(name) +" </h1>"

# NUMBERS
@app.route("/add/<int:num1>/<int:num2>")
def adding_integers(num1, num2):
    return "<h1> The sum is: {}".format(num1+num2) + "</h1>"
