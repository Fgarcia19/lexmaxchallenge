from unittest import result
from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

def database():
    return sqlite3.connect("people.sqlite")


@app.route("/people", methods=["GET","POST"])
def people():
    conn = database()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM people")
        people = [ dict(id=element[0], name=element[1],lastname=element[2],email=element[3],address=element[4],reference_address=element[5],phone_number=element[6]) for element in cursor.fetchall()]
        return jsonify(people)
    if request.method == "POST":
        if "name" not in request.form or "lastname" not in request.form or "email" not in request.form:
            return "Name, lastname and email are requeried",400
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        address = ""
        if "address" in request.form:
            address = request.form['address']
        reference_address = ""
        if "reference_address" in request.form:
            reference_address = request.form['reference_address']
        phone_number = ""
        if "phone_number" in request.form:
            phone_number = request.form['phone_number']
        sql= "INSERT INTO people (name,lastname,email,address,reference_address,phone_number) values (?,?,?,?,?,?)"
        cursor.execute(sql,(name,lastname,email,address,reference_address,phone_number))
        conn.commit()
        return "Created",200

@app.route("/people/<int:id>", methods=["GET","PUT","DELETE"])
def person(id):
    conn = database()
    cursor = conn.cursor()
    if request.method == "GET":
        sql = "SELECT * FROM people WHERE id = ?"
        cursor.execute(sql,(id,))
        result_query = cursor.fetchall()
        if len(result_query) == 0:
            return "Not Found",404
        result = result_query[0]
        r = dict(id=result[0], name=result[1],lastname=result[2],email=result[3],address=result[4],reference_address=result[5],phone_number=result[6])
        return r
        
    if request.method == "PUT":
        if "name" not in request.form or "lastname" not in request.form or "email" not in request.form:
            return "Name, lastname and email are requeried",400
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        address = ""
        if "address" in request.form:
            address = request.form['address']
        reference_address = ""
        if "reference_address" in request.form:
            reference_address = request.form['reference_address']
        phone_number = ""
        if "phone_number" in request.form:
            phone_number = request.form['phone_number']
        sql= "UPDATE people SET name=?,lastname=?,email=?,address=?,reference_address=?,phone_number=? WHERE id = ?"
        cursor.execute(sql,(name,lastname,email,address,reference_address,phone_number,id))
        conn.commit()
        return "Update"
    
    if request.method == "DELETE":
        sql = "DELETE FROM people WHERE id = ?"
        conn.execute(sql,(id,))
        conn.commit()
        return "Delete person with id: "+str(id)




if __name__ == '__main__':
    app.run()

        