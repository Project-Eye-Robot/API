from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello world'

@app.route('/testGet', methods=['GET'])
def testGet():
    return 'Test GET'

@app.route('/testPost', methods=['POST'])
def testPost():
    return request.json['test']

if __name__ == '__main__':
    app.run(debug=True, port=1234, host='0.0.0.0')
