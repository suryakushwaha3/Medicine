from flask import jsonify, request
from operations.available_stock_operation import (
    add_available_stock,
    get_available_stock,
    get_user_available_stock,
    update_available_stock,
    delete_available_stock
)

def available_stock_routes(app):

    # Add available stock
    @app.route('/addAvailableStock', methods=['POST'])
    def add_AvailableStock():
        try:
            result = add_available_stock(
                product_id=request.form['product_id'],
                product_name=request.form['product_name'],
                category=request.form['category'],
                price=request.form['price'],
                stock=request.form['stock'],
                user_id=request.form['user_id'],
                user_name=request.form['user_name']
            )
            return jsonify(result), 200
        except Exception as error:
            print("ERROR:", error)
            return jsonify({"error": "Failed to add available stock"}), 400

    # Get all available stock
    @app.route('/availableStock', methods=['GET'])
    def get_AvailableStock():
        try:
            stocks = get_available_stock()
            stock_list = []
            for stock in stocks:
                stock_list.append({
                    "id": stock[0],
                    "product_id": stock[1],
                    "product_name": stock[2],
                    "category": stock[3],
                    "price": stock[4],
                    "stock": stock[5],
                    "user_id": stock[6],
                    "user_name": stock[7]
                })
            return jsonify(stock_list), 200
        except Exception as error:
            print("ERROR:", error)
            return jsonify({"error": "Failed to fetch available stock"}), 400

    # Get available stock of a user
    @app.route('/userAvailableStock/<user_id>', methods=['GET'])
    def get_UserAvailableStock(user_id):
        try:
            stocks = get_user_available_stock(user_id)
            stock_list = []
            for stock in stocks:
                stock_list.append({
                    "id": stock[0],
                    "product_id": stock[1],
                    "product_name": stock[2],
                    "category": stock[3],
                    "price": stock[4],
                    "stock": stock[5],
                    "user_id": stock[6],
                    "user_name": stock[7]
                })
            return jsonify(stock_list), 200
        except Exception as error:
            print("ERROR:", error)
            return jsonify({"error": "Failed to fetch user available stock"}), 400

    # Update available stock
    @app.route('/updateAvailableStock', methods=['PATCH'])
    def update_AvailableStock():
        try:
            result = update_available_stock(
                product_id=request.form['product_id'],
                product_name=request.form['product_name'],
                category=request.form['category'],
                price=request.form['price'],
                stock=request.form['stock']
            )
            return jsonify(result), 200
        except Exception as error:
            print("ERROR:", error)
            return jsonify({"error": "Failed to update available stock"}), 400

    # Delete available stock
    @app.route('/deleteAvailableStock', methods=['DELETE'])
    def delete_AvailableStock():
        try:
            result = delete_available_stock(
                product_id=request.form['product_id']
            )
            return jsonify(result), 200
        except Exception as error:
            print("ERROR:", error)
            return jsonify({"error": "Failed to delete available stock"}), 400