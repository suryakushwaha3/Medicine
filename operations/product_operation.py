import sqlite3


# Add Product
def add_product(
    product_id,
    product_name,
    category,
    stock,
    product_image
):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO Products
        (
            product_id,
            product_name,
            category,
            stock,
            product_image
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            product_id,
            product_name,
            category,
            stock,
            product_image
        )
    )

    conn.commit()
    conn.close()

    return {
        "message": "Product added successfully."
    }


# Get Products
def get_products():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            product_id,
            product_name,
            category,
            stock,
            product_image
        FROM Products
        """
    )

    products = cursor.fetchall()

    conn.close()

    return products


# Update Product
def update_product(
    product_id,
    product_name,
    category,
    stock,
    product_image
):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE Products
        SET
            product_name = ?,
            category = ?,
            stock = ?,
            product_image = ?
        WHERE product_id = ?
        """,
        (
            product_name,
            category,
            stock,
            product_image,
            product_id
        )
    )

    conn.commit()
    conn.close()

    return {
        "message": "Product updated successfully."
    }


# Delete Product
def delete_product(product_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM Products
        WHERE product_id = ?
        """,
        (product_id,)
    )

    conn.commit()
    conn.close()

    return {
        "message": "Product deleted successfully."
    }