import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = []

@app.route("/products", methods=["GET"])
def get_product():
    response = json.dumps(products)
    return response, 200

@app.route("/products", methods=["POST"])
def post_product():

    try:
        product_data = request.get_json()
        if "name" in product_data and "price" in product_data:
            product = {
                "name": product_data["name"],
                "price": product_data["price"]
            }
            products.append(product)
            response = json.dumps(product)
            return response, 201
        else:
            return "Données incorrectes", 400
    except Exception as e:
        return str(e), 500

@app.route('/route', methods=['GET'])
def route_get():
    return json.dumps({"route":'Ceci est une route GET.'})

@app.route('/route', methods=['POST'])
def route_post():
    return json.dumps({"route":'Ceci est une route POST.'})

@app.route('/route', methods=['PUT'])
def route_put():
    return json.dumps({"route":'Ceci est une route PUT.'})

@app.route('/route', methods=['DELETE'])
def route_delete():
    return json.dumps({"route":'Ceci est une route DELETE.'})

if __name__ == "__main__":
    app.run(port=8080)




# @app.route("/products", methods=["GET", "POST"])
# def products_handler():
#     if request.method == "GET":
#         response = json.dumps(products)
#         return response, 200

#     elif request.method == "POST":
#         try:
#             product_data = request.get_json()
#             if "name" in product_data and "price" in product_data:
#                 product = {
#                     "name": product_data["name"],
#                     "price": product_data["price"]
#                 }
#                 products.append(product)
#                 response = json.dumps(product)
#                 return response, 201
#             else:
#                 return "Données incorrectes", 400
#         except Exception as e:
#             return str(e), 500

# if __name__ == "__main__":
#     app.run(port=8080)
