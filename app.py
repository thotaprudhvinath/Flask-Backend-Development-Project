from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form["test_string"]
    regex_pattern = request.form["regex_pattern"]
    matches = re.findall(regex_pattern, test_string)
    return render_template("results.html", matches=matches)

@app.route("/validate-email", methods=["POST"])
def validate_email():
    email = request.form["email"]
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return "Valid email address"
    else:
        return "Invalid email address"

if __name__ == "__main__":
    app.run(debug=True)

