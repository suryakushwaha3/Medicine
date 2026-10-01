from flask import request, jsonify

from operations.notificationOperation import (
    create_notification,
    get_all_notifications,
    get_unread_notifications,
    get_unread_notification_count,
    mark_notification_as_read,
    mark_all_notifications_as_read,
    delete_notification,
    delete_all_notifications
)


def notification_routes(app):

    # ============================================================
    # CREATE NOTIFICATION
    # ============================================================

    @app.route('/createNotification', methods=['POST'])
    def createNotification():

        try:

            title = request.form.get('title')
            message = request.form.get('message')
            notification_type = request.form.get('type')

            if not title:
                return jsonify({
                    'error': 'Title is required'
                }), 400

            if not message:
                return jsonify({
                    'error': 'Message is required'
                }), 400

            if not notification_type:
                return jsonify({
                    'error': 'Notification type is required'
                }), 400

            result = create_notification(
                title=title,
                message=message,
                notification_type=notification_type
            )

            return jsonify(result), 201

        except Exception as error:

            print("ERROR:", error)

            return jsonify({
                'error': 'Failed to create notification'
            }), 500


    # ============================================================
    # GET ALL NOTIFICATIONS
    # ============================================================

    @app.route('/notifications', methods=['GET'])
    def getNotifications():

        try:

            notifications = get_all_notifications()

            return jsonify(
                notifications
            ), 200

        except Exception as error:

            print("ERROR:", error)

            return jsonify({
                'error': 'Failed to fetch notifications'
            }), 500


    # ============================================================
    # GET UNREAD NOTIFICATIONS
    # ============================================================

    @app.route('/notifications/unread', methods=['GET'])
    def getUnreadNotifications():

        try:

            notifications = get_unread_notifications()

            return jsonify(
                notifications
            ), 200

        except Exception as error:

            print("ERROR:", error)

            return jsonify({
                'error': 'Failed to fetch unread notifications'
            }), 500


    # ============================================================
    # GET UNREAD NOTIFICATION COUNT
    # ============================================================

    @app.route('/notifications/unread-count', methods=['GET'])
    def getUnreadNotificationCount():

        try:

            result = get_unread_notification_count()

            return jsonify(
                result
            ), 200

        except Exception as error:

            print("ERROR:", error)

            return jsonify({
                'error': 'Failed to fetch unread notification count'
            }), 500


    # ============================================================
    # MARK SINGLE NOTIFICATION AS READ
    # ============================================================

    @app.route(
        '/notifications/<int:notification_id>/read',
        methods=['PATCH']
    )
    def markNotificationAsRead(notification_id):

        try:

            result = mark_notification_as_read(
                notification_id
            )

            if 'error' in result:
                return jsonify(result), 404

            return jsonify(result), 200

        except Exception as error:

            print("ERROR:", error)

            return jsonify({
                'error': 'Failed to mark notification as read'
            }), 500


    # ============================================================
    # MARK ALL NOTIFICATIONS AS READ
    # ============================================================

    @app.route(
        '/notifications/read-all',
        methods=['PATCH']
    )
    def markAllNotificationsAsRead():

        try:

            result = mark_all_notifications_as_read()

            return jsonify(
                result
            ), 200

        except Exception as error:

            print("ERROR:", error)

            return jsonify({
                'error': 'Failed to mark all notifications as read'
            }), 500


    # ============================================================
    # DELETE SINGLE NOTIFICATION
    # ============================================================

    @app.route(
        '/notifications/<int:notification_id>',
        methods=['DELETE']
    )
    def deleteNotification(notification_id):

        try:

            result = delete_notification(
                notification_id
            )

            if 'error' in result:
                return jsonify(result), 404

            return jsonify(result), 200

        except Exception as error:

            print("ERROR:", error)

            return jsonify({
                'error': 'Failed to delete notification'
            }), 500


    # ============================================================
    # DELETE ALL NOTIFICATIONS
    # ============================================================

    @app.route(
        '/notifications',
        methods=['DELETE']
    )
    def deleteAllNotifications():

        try:

            result = delete_all_notifications()

            return jsonify(
                result
            ), 200

        except Exception as error:

            print("ERROR:", error)

            return jsonify({
                'error': 'Failed to delete all notifications'
            }), 500