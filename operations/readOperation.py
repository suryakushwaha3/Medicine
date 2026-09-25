import sqlite3



def getAllUsers():


    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    userJson = []

    for user in users:
        tempUser = {
            "id": user[0],
            "user_id": user[1],
            "password": user[2],
            "date_of_account_creation": user[3],
            "isApproved": user[4],
            "block": user[5],
            "name": user[6],
            "address": user[7],
            "email": user[8],
            "phone_number": user[9],
            "pincode": user[10]
        }
        userJson.append(tempUser)

 


    conn.close()
    return userJson


def getSpacificUser(userId):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE user_id = ?",
        (userId,)
    )

    user = cursor.fetchone()

    conn.close()

    if user is None:
        return []

    tempUser = {
        "id": user[0],
        "user_id": user[1],
        "password": user[2],
        "date_of_account_creation": user[3],
        "isApproved": user[4],
        "block": user[5],
        "name": user[6],
        "address": user[7],
        "email": user[8],
        "phone_number": user[9],
        "pincode": user[10]
    }

    userList = []
    userList.append(tempUser)

    print(userList)

    return userList