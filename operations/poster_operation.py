import sqlite3


def addPoster(posterName, posterImage):

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO Posters (
            poster_name,
            poster_image
        )
        VALUES (?, ?)
        """,
        (
            posterName,
            posterImage
        )
    )

    conn.commit()

    posterId = cursor.lastrowid

    conn.close()

    return posterId


def getAllPosters():

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Posters WHERE is_active = 1"
    )

    posters = cursor.fetchall()

    posterJson = []

    for poster in posters:

        tempPoster = {
            "id": poster[0],
            "poster_name": poster[1],
            "poster_image": poster[2],
            "is_active": poster[3],
            "created_at": poster[4]
        }

        posterJson.append(tempPoster)

    conn.close()

    return posterJson


def getSpecificPoster(posterId):

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Posters WHERE id = ?",
        (posterId,)
    )

    poster = cursor.fetchone()

    conn.close()

    if poster is None:
        return []

    tempPoster = {
        "id": poster[0],
        "poster_name": poster[1],
        "poster_image": poster[2],
        "is_active": poster[3],
        "created_at": poster[4]
    }

    posterList = []
    posterList.append(tempPoster)

    return posterList


def updatePoster(posterId, posterName, posterImage):

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE Posters
        SET poster_name = ?,
            poster_image = ?
        WHERE id = ?
        """,
        (
            posterName,
            posterImage,
            posterId
        )
    )

    conn.commit()

    updated = cursor.rowcount

    conn.close()

    return updated


def deletePoster(posterId):

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM Posters WHERE id = ?",
        (posterId,)
    )

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    return deleted