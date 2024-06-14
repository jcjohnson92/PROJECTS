from flask import Flask, render_template, request, redirect
from cs50 import SQL


app = Flask(__name__)
db = SQL("sqlite:///Login.db")

# @app.route("/", methods=["GET","POST"])
@app.route("/index.html",  methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/account", methods=["POST"])
def account():
    invalid = "Incorrect username/password"
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        if not name or not password:
            return render_template("index.html", invalid=invalid)
        user_info = db.execute("SELECT * from Persons WHERE Username=?", name)

        for user in user_info:
            if user['Username'] == name and user['Password']==password:
                return render_template("account.html",name=name)
            else: 
                return render_template("index.html", invalid=invalid)
        return render_template("account.html",name=name)


@app.route("/create", methods=["POST"])
def create():
    if request.method == "POST":
        return render_template("create.html")
    

# Add user account to database    
@app.route("/create_account", methods=["POST"])
def create_account():
    already_created = "Username taken"
    no_info = "Missing information"
    success = "Successful account creation"
    matches = "passwords dont match"

    get_users = db.execute("SELECT Username from Persons;")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        check_password = request.form.get("check_password")

        if not username or not password or not check_password:
            return render_template("create.html", no_info=no_info)

        if password != check_password:
            return render_template("create.html", matches=matches)

        for user in get_users:
            
            if username.lower() ==user['Username'].lower():
                return render_template("create.html", already_created=already_created)
        
        db.execute("INSERT INTO Persons(Username, Password) VALUES (?,?)", username,password)
    return render_template("index.html", success=success)


