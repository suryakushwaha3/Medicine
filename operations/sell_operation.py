import sqlite3


# Add a new sell record
def add_sell(
    sell_id, product_id, quantity, reamining_stock,
    date_of_sell, total_amount, price,
    product_name, user_name, user_id
):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Sell_History
        (
            sell_id, product_id, quantity, reamining_stock,
            date_of_sell, total_amount, price,
            product_name, user_name, user_id
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        sell_id, product_id, quantity, reamining_stock,
        date_of_sell, total_amount, price,
        product_name, user_name, user_id
    ))

    conn.commit()
    conn.close()

    return {"message": "Sell added successfully."}


# Get all sell history
def get_sell_history():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Sell_History")
    sells = cursor.fetchall()

    conn.close()

    return sells


# Get sell history of a specific user
def get_user_sell_history(user_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Sell_History WHERE user_id = ?",
        (user_id,)
    )

    sells = cursor.fetchall()

    conn.close()

    return sells


# Delete a sell record
def delete_sell(sell_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM Sell_History WHERE sell_id = ?",
        (sell_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Sell record deleted successfully."}