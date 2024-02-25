"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
from flask import jsonify
#from models import Person

#Se incia Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#Metodo GET para obtener todos los miembros de la familia/Endpoint
@app.route('/members', methods=['GET'])
def handle_hello():
    members = jackson_family.get_all_members()
    response_body = jsonify(members)
    return response_body, 200

#Metodo POST para crear un miembro de la familia/Endpoint
@app.route('/member', methods=['POST'])
def handle_add_member():
    member = request.json
    jackson_family.add_member(member)
    return jsonify({"done": "Familiar agregado!"}), 200

                    #Creando una url dinamica para recibir información

#Metodo DELETE para eliminar un miembro de la familia/Endpoint
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_family_member(member_id):
    deleted_member = jackson_family.delete_member(member_id)

    if deleted_member:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

    
#Metodo GET para obtener un miembro de la familia/Endpoint
@app.route('/member/<int:member_id>', methods=['GET']) #<int:member_id> me crea una url dinamica.
def get_one_member(member_id):
    member = jackson_family.get_member(member_id)
    
    if member is None:
        return jsonify({"error": "Member not found"}), 404

    response_body = {
        "id": member["id"],
        "first_name": member["first_name"],
        "age": member["age"],
        "lucky_numbers": member["lucky_numbers"]
    }

    return jsonify(response_body), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
