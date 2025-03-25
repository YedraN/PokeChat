from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite solicitudes desde el frontend en SvelteKit

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

@app.route("/pokemon", methods=["GET"])
def get_pokemon():
    pokemon_id = request.args.get("id")
    if not pokemon_id:
        return jsonify({"error": "Se requiere un número de Pokédex"}), 400
    
    response = requests.get(f"{POKEAPI_URL}{pokemon_id}")
    if response.status_code != 200:
        return jsonify({"error": "Pokémon no encontrado"}), 404
    
    data = response.json()
    pokemon_info = {
        "name": data["name"].capitalize(),
        "id": data["id"],
        "image": data["sprites"]["front_default"],
        "types": [t["type"]["name"].capitalize() for t in data["types"]]
    }
    
    return jsonify(pokemon_info)

if __name__ == "__main__":
    app.run(debug=True)