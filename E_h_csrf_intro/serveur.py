from flask import Flask, jsonify, request, session
import jwt
import random

app = Flask(__name__)
app.secret_key = "my_secret_key"

def generate_csrf_token():
    token = jwt.encode({"csrf": random.randint(1, 1000000000)},
                      app.secret_key, algorithm="HS256")
    return token

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        csrf_token = generate_csrf_token()
        session["csrf_token"] = csrf_token
        return jsonify({"csrf_token": csrf_token})

    if request.method == "POST":
        csrf_token = request.json.get("csrf_token")
        if csrf_token is None or csrf_token != session["csrf_token"]:
            raise Exception("CSRF token invalide")

        # Traiter la requête POST
        # ...

if __name__ == "__main__":
    app.run(debug=True)
