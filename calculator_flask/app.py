from flask import Flask, request, jsonify
from utils.calculator import calculate 

app = Flask(__name__)

@app.route('/', methods=['POST'])
def calculator():
    data = request.get_json()
    ans = calculate(data['Num1'], data['OP'], data['Num2'])
    return jsonify({
        'ans': ans
    })

@app.route('/', methods=['GET'])
def helloworld():
    return "hello world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) 