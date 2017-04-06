from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():

    # print dir(request)
    # print request.values['data']
    return render_template("hello_world.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/about")
def about():
    return render_template("about.html")
app.run(debug=True)