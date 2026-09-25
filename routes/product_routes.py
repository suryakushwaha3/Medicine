from flask import jsonify, request
from operations.product_operation import (
    add_product,
    get_products,
    update_product,
    delete_product
)


def product_routes(app):

    # Add product
    @app.route('/addProduct', methods=['POST'])
    def add_Product():
        try:
            product_id = request.form['product_id']
            product_name = request.form['product_name']
            category = request.form['category']
            stock = request.form['stock']

            result = add_product(
                product_id=product_id,
                product_name=product_name,
                category=category,
                stock=stock
            )

            return jsonify({
                "message": "Product added successfully.",
                "data": result,
                "status": 200
            }), 200

        except Exception as error:
            print("ERROR:", error)

            return jsonify({
                "message": "Failed to add product.",
                "data": None,
                "status": 400
            }), 400


    # Get all products
    @app.route('/productsDetails', methods=['GET'])
    def get_Products():
        try:
            products = get_products()
            product_list = []

            for product in products:
                product_list.append({
                    "id": product[0],
                    "product_id": product[1],
                    "product_name": product[2],
                    "category": product[3],
                    "stock": product[4]
                })

            return jsonify(product_list), 200

        except Exception as error:
            print("ERROR:", error)

            return jsonify({
                "error": "Failed to fetch products"
            }), 400


    # Update product
    @app.route('/updateProduct', methods=['PATCH'])
    def update_Product():
        try:
            product_id = request.form['product_id']
            product_name = request.form['product_name']
            category = request.form['category']
            stock = request.form['stock']

            result = update_product(
                product_id=product_id,
                product_name=product_name,
                category=category,
                stock=stock
            )

            return jsonify({
                "message": "Product updated successfully.",
                "data": result,
                "status": 200
            }), 200

        except Exception as error:
            print("ERROR:", error)

            return jsonify({
                "message": "Failed to update product.",
                "data": None,
                "status": 400
            }), 400


    # Delete product
    @app.route('/deleteProduct', methods=['DELETE'])
    def delete_Product():
        try:
            product_id = request.form['product_id']

            result = delete_product(product_id=product_id)

            return jsonify({
                "message": "Product deleted successfully.",
                "data": result,
                "status": 200
            }), 200

        except Exception as error:
            print("ERROR:", error)

            return jsonify({
                "message": "Failed to delete product.",
                "data": None,
                "status": 400
            }), 400
