import sqlite3


# Add a new order to the database
def add_order(
    order_id, user_id, product_id, isApproved, quantity,
    date_of_order_creation, price, total_amount,
    product_name, user_name, message, category
):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Orders_Details
        (
            order_id, user_id, product_id, isApproved, quantity,
            date_of_order_creation, price, total_amount,
            product_name, user_name, message, category
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        order_id, user_id, product_id, isApproved, quantity,
        date_of_order_creation, price, total_amount,
        product_name, user_name, message, category
    ))

    conn.commit()
    conn.close()

    return {"message": "Order added successfully."}


# Get all orders from the database
def get_orders():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Orders_Details")
    orders = cursor.fetchall()

    conn.close()

    return orders


# Get all orders of a specific user
def get_orders_by_user(user_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Orders_Details WHERE user_id = ?",
        (user_id,)
    )

    orders = cursor.fetchall()

    conn.close()

    return orders


# Update an existing order
def update_order(order_id, isApproved, quantity, message):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Orders_Details
        SET isApproved = ?, quantity = ?, message = ?
        WHERE order_id = ?
    """, (isApproved, quantity, message, order_id))

    conn.commit()
    conn.close()

    return {"message": "Order updated successfully."}


# Delete an order from the database
def delete_order(order_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM Orders_Details WHERE order_id = ?",
        (order_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Order deleted successfully."}