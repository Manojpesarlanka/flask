from os import makedirs
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

students_list = [
    {
        "id":0,
        "name": "p_manoj",
        "sec":1,
    },
    {
        "id":1,
        "name": "q_manoj",
        "sec":1,
    }
]

@app.route('/students', methods=['GET','POST'])
def students():
    if request.method == 'GET':
        if len(students_list)>0:
            return jsonify(students_list)
        else:
            'nothing found',404
    if request.method == 'POST':
        new_name = request.form['name']
        new_sec = request.form['sec']
        iD = students_list[-1][id]+1

        new_obj = {
            'id': iD,
            'name': new_name,
            'sec': new_sec,
        }
        students_list.append(new_obj)
        return jsonify(students_list),201

if __name__ == '__main__':
    app.run()