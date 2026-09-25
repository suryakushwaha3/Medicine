import sqlite3


def update_user(userID, **fields):

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    # User ko sirf ye fields change karne ki permission hai
    allowed_fields = {
        "password",
        "name",
        "address",
        "email",
        "phone_number",
        "pincode"
    }

    # Sirf allowed fields ko select karo
    update_fields = {
        key: value
        for key, value in fields.items()
        if key in allowed_fields
    }

    # Agar koi valid field nahi bheji gayi
    if not update_fields:
        conn.close()
        return {
            "error": "No valid fields provided for update."
        }

    # Dynamic SET clause banana
    set_clause = ", ".join(
        f"{field} = ?" for field in update_fields
    )

    # Values ko list me convert karna
    values = list(update_fields.values())

    # Last value userID hogi
    values.append(userID)

    # SQL query
    query = f"""
        UPDATE Users
        SET {set_clause}
        WHERE user_id = ?
    """

    cursor.execute(query, values)

    # Changes save karo
    conn.commit()

    # Database connection close
    conn.close()

    return {
        "message": "User data updated successfully."
    }