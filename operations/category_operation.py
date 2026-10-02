import sqlite3


def addCategory(categoryName, categoryImage):

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO Categories (
            category_name,
            category_image
        )
        VALUES (?, ?)
        """,
        (
            categoryName,
            categoryImage
        )
    )

    conn.commit()

    categoryId = cursor.lastrowid

    conn.close()

    return categoryId


def getAllCategories():

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Categories WHERE is_active = 1"
    )

    categories = cursor.fetchall()

    categoryJson = []

    for category in categories:

        tempCategory = {
            "id": category[0],
            "category_name": category[1],
            "category_image": category[2],
            "is_active": category[3],
            "created_at": category[4]
        }

        categoryJson.append(tempCategory)

    conn.close()

    return categoryJson


def getSpecificCategory(categoryId):

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Categories WHERE id = ?",
        (categoryId,)
    )

    category = cursor.fetchone()

    conn.close()

    if category is None:
        return []

    tempCategory = {
        "id": category[0],
        "category_name": category[1],
        "category_image": category[2],
        "is_active": category[3],
        "created_at": category[4]
    }

    categoryList = []
    categoryList.append(tempCategory)

    return categoryList


def updateCategory(
    categoryId,
    categoryName,
    categoryImage
):

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE Categories
        SET category_name = ?,
            category_image = ?
        WHERE id = ?
        """,
        (
            categoryName,
            categoryImage,
            categoryId
        )
    )

    conn.commit()

    updated = cursor.rowcount

    conn.close()

    return updated


def deleteCategory(categoryId):

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM Categories WHERE id = ?",
        (categoryId,)
    )

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    return deleted