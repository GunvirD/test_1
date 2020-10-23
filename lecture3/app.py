from flask import Flask, render_template, request, session
from flask_session import Session


app=Flask(__name__)


@app.route("/")
def INDEX():
    return render_template("index.html")

notes=[]
@app.route("/notes/note", methods=["POST","GET"])
def NOTES():
    if request.method == "POST":
        new_note= request.form.get("note")
        if new_note == "":
            pass
        else:
            notes.append(new_note)
    return render_template("notes.html", notes=notes)
