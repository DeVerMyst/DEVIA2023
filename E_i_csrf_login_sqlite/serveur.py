# serveur.py
from flask import Flask, render_template, request, jsonify, session
from manager import create_user, get_all_users
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
            return jsonify({"error": "CSRF token invalide"}), 400

        username = request.json.get("username")
        email = request.json.get("email")

        create_user(username, email)

        return jsonify({"message": "Utilisateur créé avec succès"}), 200

@app.route("/users", methods=["GET"])
def users():
    users = get_all_users()
    user_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify({"users": user_list})

if __name__ == "__main__":
    app.run(debug=True)
