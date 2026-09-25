from flask import jsonify, request
from operations.sell_operation import (
    add_sell,
    get_sell_history,
    get_user_sell_history,
    delete_sell
)


def sell_routes(app):

    # Add sell
    @app.route('/addSell', methods=['POST'])
    def add_Sell():
        try:
            result = add_sell(
                sell_id=request.form['sell_id'],
                product_id=request.form['product_id'],
                quantity=request.form['quantity'],
                reamining_stock=request.form['reamining_stock'],
                date_of_sell=request.form['date_of_sell'],
                total_amount=request.form['total_amount'],
                price=request.form['price'],
                product_name=request.form['product_name'],
                user_name=request.form['user_name'],
                user_id=request.form['user_id']
            )

            return jsonify(result), 200

        except Exception as error:
            print("ERROR:", error)
            return jsonify({
                "error": "Failed to add sell"
            }), 400


    # Get all sell history
    @app.route('/sellHistory', methods=['GET'])
    def get_SellHistory():
        try:
            sells = get_sell_history()
            sell_list = []

            for sell in sells:
                sell_list.append({
                    "id": sell[0],
                    "sell_id": sell[1],
                    "product_id": sell[2],
                    "quantity": sell[3],
                    "reamining_stock": sell[4],
                    "date_of_sell": sell[5],
                    "total_amount": sell[6],
                    "price": sell[7],
                    "product_name": sell[8],
                    "user_name": sell[9],
                    "user_id": sell[10]
                })

            return jsonify(sell_list), 200

        except Exception as error:
            print("ERROR:", error)
            return jsonify({
                "error": "Failed to fetch sell history"
            }), 400


    # Get sell history of a user
    @app.route('/userSellHistory/<user_id>', methods=['GET'])
    def get_UserSellHistory(user_id):
        try:
            sells = get_user_sell_history(user_id)
            sell_list = []

            for sell in sells:
                sell_list.append({
                    "id": sell[0],
                    "sell_id": sell[1],
                    "product_id": sell[2],
                    "quantity": sell[3],
                    "reamining_stock": sell[4],
                    "date_of_sell": sell[5],
                    "total_amount": sell[6],
                    "price": sell[7],
                    "product_name": sell[8],
                    "user_name": sell[9],
                    "user_id": sell[10]
                })

            return jsonify(sell_list), 200

        except Exception as error:
            print("ERROR:", error)
            return jsonify({
                "error": "Failed to fetch user sell history"
            }), 400


    # Delete sell record
    @app.route('/deleteSell', methods=['DELETE'])
    def delete_Sell():
        try:
            result = delete_sell(
                sell_id=request.form['sell_id']
            )

            return jsonify(result), 200

        except Exception as error:
            print("ERROR:", error)
            return jsonify({
                "error": "Failed to delete sell"
            }), 400
