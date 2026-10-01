import sqlite3


DATABASE_NAME = "my_medicalshop.db"


# ============================================================
# CREATE NOTIFICATION
# ============================================================

def create_notification(
    title,
    message,
    notification_type
):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Notifications (
            title,
            message,
            type,
            is_read
        )
        VALUES (?, ?, ?, 0)
    """, (
        title,
        message,
        notification_type
    ))

    notification_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return {
        "message": "Notification created successfully.",
        "notification_id": notification_id
    }


# ============================================================
# GET ALL NOTIFICATIONS
# ============================================================

def get_all_notifications():

    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            message,
            type,
            is_read,
            created_at
        FROM Notifications
        ORDER BY id DESC
    """)

    notifications = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return notifications


# ============================================================
# GET UNREAD NOTIFICATIONS
# ============================================================

def get_unread_notifications():

    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            message,
            type,
            is_read,
            created_at
        FROM Notifications
        WHERE is_read = 0
        ORDER BY id DESC
    """)

    notifications = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return notifications


# ============================================================
# GET UNREAD NOTIFICATION COUNT
# ============================================================

def get_unread_notification_count():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM Notifications
        WHERE is_read = 0
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return {
        "count": count
    }


# ============================================================
# MARK SINGLE NOTIFICATION AS READ
# ============================================================

def mark_notification_as_read(notification_id):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Notifications
        SET is_read = 1
        WHERE id = ?
    """, (
        notification_id,
    ))

    affected_rows = cursor.rowcount

    conn.commit()
    conn.close()

    if affected_rows == 0:
        return {
            "error": "Notification not found."
        }

    return {
        "message": "Notification marked as read."
    }


# ============================================================
# MARK ALL NOTIFICATIONS AS READ
# ============================================================

def mark_all_notifications_as_read():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Notifications
        SET is_read = 1
        WHERE is_read = 0
    """)

    affected_rows = cursor.rowcount

    conn.commit()
    conn.close()

    return {
        "message": "All notifications marked as read.",
        "updated_count": affected_rows
    }


# ============================================================
# DELETE SINGLE NOTIFICATION
# ============================================================

def delete_notification(notification_id):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM Notifications
        WHERE id = ?
    """, (
        notification_id,
    ))

    affected_rows = cursor.rowcount

    conn.commit()
    conn.close()

    if affected_rows == 0:
        return {
            "error": "Notification not found."
        }

    return {
        "message": "Notification deleted successfully."
    }


# ============================================================
# DELETE ALL NOTIFICATIONS
# ============================================================

def delete_all_notifications():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM Notifications
    """)

    deleted_count = cursor.rowcount

    conn.commit()
    conn.close()

    return {
        "message": "All notifications deleted successfully.",
        "deleted_count": deleted_count
    }