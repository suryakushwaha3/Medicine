import sqlite3
import uuid
from datetime import date
from flask import Flask , jsonify , request
# from werkzeug.security import generate_password_hash



def createUser(name, password, phoneNumber, email, pincode, address):
    try:
        conn = sqlite3.connect("my_medicalshop.db")
        cursor = conn.cursor()

        userId = str(uuid.uuid4())
        dateOfAccountCreation = date.today()
        # password = generate_password_hash(password)

        cursor.execute('''
            INSERT INTO Users (user_id, password, date_of_account_creation, isApproved, block, name, address, email, phone_number, pincode)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    ''',(userId, password, dateOfAccountCreation, 0, 0, name, address, email, phoneNumber, pincode)) 


        conn.commit()
        conn.close()

        return jsonify({'message ' : userId, "status" : 200})
    except Exception as error:
        return jsonify({'message ' : error, "status" : 400})