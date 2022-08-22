from parser import getDups
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get-dups', methods=['GET'])
def get_dups():
    html = request.args.get('html')
    return jsonify(getDups(str(html)))

if __name__ == "__main__":
    app.run(debug=False)
