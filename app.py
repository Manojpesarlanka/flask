from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)

@app.route('/calculator/add')
def index():
    #import pdb;pdb.set_trace()
    a = request.args['a']
    b = request.args['b']
    s = int(a) + int(b)
    return jsonify("sum--> "+ str(s))

@app.route('/calculator/sub')
def index1():
    #import pdb;pdb.set_trace()
    a = request.args['a']
    b = request.args['b']
    s = int(a) - int(b)
    return "sub--> "+ str(s)

@app.route('/calculator/mul')
def index2():
    #import pdb;pdb.set_trace()
    a = request.args['a']
    b = request.args['b']
    s = int(a) * int(b)
    return "mul--> "+ str(s)

@app.route('/calculator/div')
def index3():
    #import pdb;pdb.set_trace()
    a = request.args['a']
    b = request.args['b']
    s = int(a) // int(b)
    return "div--> "+ str(s)



if __name__ == '__main__':
    app.run(debug=True)