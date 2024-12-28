from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

USERS = {
    "admin": "password",
    "user": "1234"
}

catalog = {}


@auth.verify_password
def verify(username, password):
    if username in USERS and USERS[username] == password:
        return username
    return None


@app.route('/items', methods=['GET', 'POST'])
@auth.login_required
def handle_items():
    if request.method == 'GET':
        return jsonify(list(catalog.values())), 200

    if request.method == 'POST':
        data = request.get_json()
        item_id = data.get('id')
        if item_id in catalog:
            return jsonify({"error": "Item already exists"}), 400
        catalog[item_id] = {
            "id": item_id,
            "name": data.get('name'),
            "price": data.get('price')
        }
        return jsonify(catalog[item_id]), 201


@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
def handle_item(item_id):
    if item_id not in catalog:
        return jsonify({"error": "Item not found"}), 404

    if request.method == 'GET':
        return jsonify(catalog[item_id]), 200

    if request.method == 'PUT':
        data = request.get_json()
        catalog[item_id]["name"] = data.get('name', catalog[item_id]["name"])
        catalog[item_id]["price"] = data.get('price', catalog[item_id]["price"])
        return jsonify(catalog[item_id]), 200

    if request.method == 'DELETE':
        del catalog[item_id]
        return jsonify({"message": "Item deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
