from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user credentials
USER_CREDENTIALS = {
    "testuser": "password123"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials!")

    return render_template("login.html", error="")

@app.route("/dashboard")
def dashboard():
    return "<h1>Welcome to the Dashboard!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
