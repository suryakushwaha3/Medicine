import sqlite3


def add_product(product_id, product_name, category, stock):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO Products
        (product_id, product_name, category, stock)
        VALUES (?, ?, ?, ?)
        """,
        (
            product_id,
            product_name,
            category,
            stock
        )
    )

    conn.commit()
    conn.close()

    return {
        "message": "Product added successfully."
    }


def get_products():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Products"
    )

    products = cursor.fetchall()

    conn.close()

    return products


def update_product(product_id, product_name, category, stock):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE Products
        SET
            product_name = ?,
            category = ?,
            stock = ?
        WHERE product_id = ?
        """,
        (
            product_name,
            category,
            stock,
            product_id
        )
    )

    conn.commit()
    conn.close()

    return {
        "message": "Product updated successfully."
    }


def delete_product(product_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM Products WHERE product_id = ?",
        (product_id,)
    )

    conn.commit()
    conn.close()

    return {
        "message": "Product deleted successfully."
    }