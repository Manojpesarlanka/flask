from flask import Flask, request
import requests
import wikipedia
from flask.json import jsonify

app = Flask(__name__)

@app.route('/wikipedia/search')
def wiki():
    a = request.args['a']
    b = request.args['b']
    p=wikipedia.search(a)
    r=[]
    for x in p:
        n=wikipedia.page(x)
        try:
            title = n.title
            url = n.url
        except:
            pass
        respons = {"Title" : title, "Url" : url}
        r.append(respons)
    return jsonify(r[b])

if __name__ == '__main__':
    app.run(debug=True)
