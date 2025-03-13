from flask import Flask, request, jsonify

app = Flask(__name__)


comics = [
    {"id": 1, "title": "The Killing Joke", "author": "Alan Moore", "year": 1988},
    {"id": 2, "title": "Batman: Year One", "author": "Frank Miller", "year": 1987},
    {"id":3, "title": "Arkham Asylum: A Serious House on Serious Earth", "author": "Grant Morrison", "year": 1989},
   
]

# Endpoint listado completo de cómics
@app.route('/comics', methods=['GET'])
def get_comics():
    return jsonify({"comics": comics})


@app.route('/comics/<int:comic_id>', methods=['GET'])
def get_comic_by_id(comic_id):
    comic = next((comic for comic in comics if comic["id"] == comic_id), None)
    if not comic:
        return jsonify({"error": "Comic not found"}), 404
    return jsonify({"comic": comic})


@app.route('/comics', methods=['POST'])
def add_comic():
    data = request.json
    new_comic = {
        "id": len(comics) + 1,  # Genera ID 
        "title": data.get("title"),
        "author": data.get("author"),
        "year": data.get("year")
    }
    comics.append(new_comic)
    return jsonify({"message": "Comic added", "comic": new_comic}), 201


@app.route('/comics/<int:comic_id>', methods=['PUT'])
def update_comic(comic_id):
    data = request.json
    comic = next((comic for comic in comics if comic["id"] == comic_id), None)
    if not comic:
        return jsonify({"error": "Comic not found"}), 404
    
    # Actualizar los datos
    comic["title"] = data.get("title", comic["title"])
    comic["author"] = data.get("author", comic["author"])
    comic["year"] = data.get("year", comic["year"])
    return jsonify({"message": "Comic updated", "comic": comic})

@app.route('/comics/<int:comic_id>', methods=['DELETE'])
def delete_comic(comic_id):
    
    for c in comics:
        if c['id'] == comic_id:
            comics.remove(c)  
            return jsonify({"message": "Comic deleted successfully"}), 200
    
    
    return jsonify({"error": "Comic not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)
