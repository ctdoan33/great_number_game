from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
@app.route("/")
def game():
    if "number" not in session:
        session["number"]=random.randrange(0,101)
    return render_template("index.html")
@app.route("/compare", methods=["POST"])
def compare():
    session["guess"]=int(request.form["number"])
    return redirect("/")
@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")
app.run(debug=True)