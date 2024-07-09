from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api')
def get_data():
    data = {
        'message': 'Hello, World!'
    }
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
