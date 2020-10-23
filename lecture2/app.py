from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    names = ['Gunvir','Manvir','Raghvir','Manpreet','Nachatar','Baljit']
    return render_template("test.html", names=names)

@app.route("/time")
def time():
    now = datetime.datetime.now()
    year=now.year
    month=now.month
    day=now.day
    hour=now.hour
    minute=now.minute
    second=now.second
    is_it_new_year=now.month==10 and now.day==25
    return render_template("time.html", year=year,month=month,day=day,hour=hour,minute=minute,second=second,is_it_new_year=is_it_new_year )


@app.route("/<string:name>")
def welcome(name):
    name=name.capitalize()
    return "Welcome {}".format(name)



notes=[]
@app.route("/note", methods=["POST"])
def NOTE1():
    notes= request.form.get("note")
    notes.append(notes)

    return render_template("note.html", notes=notes)





@app.route("/form/welcome/login", methods = ["POST"])
def login():
    name=request.form.get("name")
    return render_template("welcome.html", name=name)


