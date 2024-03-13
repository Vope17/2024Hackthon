from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['POST', 'GET'])
def hello():
    req_data = request.get_json()

    hi = req_data['hi']
    xd = req_data['xd']
    return '''the msg is {}, the msg2 is {}'''.format(hi, xd) 

if __name__ == '__main__':
    app.run(debug=True)