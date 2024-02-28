from quart import Quart, request, jsonify

app = Quart(__name__)

@app.route('/api', methods=['GET'])
async def get_data():
    # Here you can retrieve and return data
    return jsonify({"message": "GET request successful"}), 200

@app.route('/api', methods=['POST'])
async def post_data():
    data = await request.get_json()
    # Here you can process the data
    return jsonify({"message": "POST request successful", "data": data}), 201

if __name__ == '__main__':
    app.run()

