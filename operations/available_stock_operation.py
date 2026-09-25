import sqlite3

# Add available stock
def add_available_stock(
    product_id,
    product_name,
    category,
    price,
    stock,
    user_id,
    user_name
):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Available_Stock
        (
            product_id,
            product_name,
            category,
            price,
            stock,
            user_id,
            user_name
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        product_id,
        product_name,
        category,
        price,
        stock,
        user_id,
        user_name
    ))

    conn.commit()
    conn.close()

    return {"message": "Available stock added successfully."}


# Get all available stock
def get_available_stock():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Available_Stock")
    stocks = cursor.fetchall()

    conn.close()

    return stocks


# Get available stock of a specific user
def get_user_available_stock(user_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Available_Stock WHERE user_id = ?",
        (user_id,)
    )

    stocks = cursor.fetchall()

    conn.close()

    return stocks


# Update available stock
def update_available_stock(
    product_id,
    product_name,
    category,
    price,
    stock
):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Available_Stock
        SET
            product_name = ?,
            category = ?,
            price = ?,
            stock = ?
        WHERE product_id = ?
    """, (
        product_name,
        category,
        price,
        stock,
        product_id
    ))

    conn.commit()
    conn.close()

    return {"message": "Available stock updated successfully."}


# Delete available stock
def delete_available_stock(product_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM Available_Stock WHERE product_id = ?",
        (product_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Available stock deleted successfully."}