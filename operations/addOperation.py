import sqlite3
import uuid
from datetime import date
from flask import Flask, jsonify, request


def createUser(name, password, phoneNumber, email, pincode, address):
    try:
        conn = sqlite3.connect("my_medicalshop.db")
        cursor = conn.cursor()

        # Check if email already exists
        cursor.execute(
            "SELECT id FROM Users WHERE email = ?",
            (email,)
        )

        existingUser = cursor.fetchone()

        if existingUser:
            conn.close()

            return jsonify({
                "message": "Email already registered",
                "status": 409
            }), 409

        userId = str(uuid.uuid4())
        dateOfAccountCreation = date.today()

        cursor.execute('''
            INSERT INTO Users (
                user_id,
                password,
                date_of_account_creation,
                isApproved,
                block,
                name,
                address,
                email,
                phone_number,
                pincode
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            userId,
            password,
            dateOfAccountCreation,
            0,
            0,
            name,
            address,
            email,
            phoneNumber,
            pincode
        ))

        conn.commit()
        conn.close()

        return jsonify({
            "message": userId,
            "status": 200
        })

    except Exception as error:
        return jsonify({
            "message": str(error),
            "status": 400
        }), 400