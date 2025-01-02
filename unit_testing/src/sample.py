from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify(result=a + b)

@app.route('/subtract', methods=['GET'])
def subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify(result=a - b)

@app.route('/multiply', methods=['GET'])
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify(result=a * b)

@app.route('/divide', methods=['GET'])
def divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    if b == 0:
        return jsonify(error="Cannot divide by zero"), 400
    return jsonify(result=a / b)

if __name__ == '__main__':
    app.run(debug=True)