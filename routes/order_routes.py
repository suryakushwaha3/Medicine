from flask import jsonify, request
from operations.order_operation import (
    add_order,
    get_orders,
    get_orders_by_user,
    update_order,
    delete_order
)


def order_routes(app):

    # Add order
    @app.route('/addOrder', methods=['POST'])
    def add_Order():
        try:
            result = add_order(
                order_id=request.form['order_id'],
                user_id=request.form['user_id'],
                product_id=request.form['product_id'],
                isApproved=request.form['isApproved'],
                quantity=request.form['quantity'],
                date_of_order_creation=request.form['date_of_order_creation'],
                price=request.form['price'],
                total_amount=request.form['total_amount'],
                product_name=request.form['product_name'],
                user_name=request.form['user_name'],
                message=request.form['message'],
                category=request.form['category']
            )

            return jsonify(result), 200

        except Exception as error:
            print("ERROR:", error)
            return jsonify({"error": "Failed to add order"}), 400


    # Get all orders
    @app.route('/orders', methods=['GET'])
    def get_Orders():
        try:
            orders = get_orders()
            order_list = []

            for order in orders:
                order_list.append({
                    "id": order[0],
                    "order_id": order[1],
                    "user_id": order[2],
                    "product_id": order[3],
                    "isApproved": order[4],
                    "quantity": order[5],
                    "date_of_order_creation": order[6],
                    "price": order[7],
                    "total_amount": order[8],
                    "product_name": order[9],
                    "user_name": order[10],
                    "message": order[11],
                    "category": order[12]
                })

            return jsonify(order_list), 200

        except Exception as error:
            print("ERROR:", error)
            return jsonify({"error": "Failed to fetch orders"}), 400


    # Get orders of a user
    @app.route('/userOrders/<user_id>', methods=['GET'])
    def get_UserOrders(user_id):
        try:
            orders = get_orders_by_user(user_id)
            order_list = []

            for order in orders:
                order_list.append({
                    "id": order[0],
                    "order_id": order[1],
                    "user_id": order[2],
                    "product_id": order[3],
                    "isApproved": order[4],
                    "quantity": order[5],
                    "date_of_order_creation": order[6],
                    "price": order[7],
                    "total_amount": order[8],
                    "product_name": order[9],
                    "user_name": order[10],
                    "message": order[11],
                    "category": order[12]
                })

            return jsonify(order_list), 200

        except Exception as error:
            print("ERROR:", error)
            return jsonify({"error": "Failed to fetch user orders"}), 400


    # Update order
    @app.route('/updateOrder', methods=['PATCH'])
    def update_Order():
        try:
            result = update_order(
                order_id=request.form['order_id'],
                isApproved=request.form['isApproved'],
                quantity=request.form['quantity'],
                message=request.form['message']
            )

            return jsonify(result), 200

        except Exception as error:
            print("ERROR:", error)
            return jsonify({"error": "Failed to update order"}), 400


    # Delete order
    @app.route('/deleteOrder', methods=['DELETE'])
    def delete_Order():
        try:
            result = delete_order(
                order_id=request.form['order_id']
            )

            return jsonify(result), 200

        except Exception as error:
            print("ERROR:", error)
            return jsonify({"error": "Failed to delete order"}), 400
