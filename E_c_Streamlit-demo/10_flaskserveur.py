# -*- coding: utf-8 -*-

from flask import Flask, jsonify

app = Flask(__name__)

# Route pour fournir des données JSON
@app.route('/api/data', methods=["GET"])
def get_data():
    data = {'message': 'Données depuis le serveur Flask'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
