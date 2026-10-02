import os

from flask import jsonify, request, send_from_directory

from operations.product_operation import (
    add_product,
    get_products,
    update_product,
    delete_product
)

from operations.productImageOperation import (
    save_product_image
)

def product_routes(app):

    # Product image upload folder
    upload_folder = os.path.join(
        app.root_path,
        "uploads",
        "products"
    )

    os.makedirs(
        upload_folder,
        exist_ok=True
    )


    # Add product
    @app.route('/addProduct', methods=['POST'])
    def add_Product():

        try:

            product_id = request.form['product_id']
            product_name = request.form['product_name']
            category = request.form['category']
            stock = request.form['stock']

            # Get product image
            image = request.files.get('product_image')

            if image is None:
                return jsonify({
                    "message": "Product image is required.",
                    "data": None,
                    "status": 400
                }), 400

            # Save image
            image_result = save_product_image(
                image_file=image,
                upload_folder=upload_folder
            )

            if "error" in image_result:
                return jsonify({
                    "message": image_result["error"],
                    "data": None,
                    "status": 400
                }), 400

            # Image path saved in database
            product_image = (
                "uploads/products/"
                + image_result["filename"]
            )

            # Add product
            result = add_product(
                product_id=product_id,
                product_name=product_name,
                category=category,
                stock=stock,
                product_image=product_image
            )

            return jsonify({
                "message": "Product added successfully.",
                "data": result,
                "product_image": product_image,
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
                    "stock": product[4],
                    "product_image": product[5]
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

            # Image optional during update
            image = request.files.get('product_image')

            # Existing image path
            product_image = request.form.get(
                'product_image'
            )

            # If new image is uploaded
            if image is not None and image.filename != "":

                image_result = save_product_image(
                    image_file=image,
                    upload_folder=upload_folder
                )

                if "error" in image_result:
                    return jsonify({
                        "message": image_result["error"],
                        "data": None,
                        "status": 400
                    }), 400

                product_image = (
                    "uploads/products/"
                    + image_result["filename"]
                )

            result = update_product(
                product_id=product_id,
                product_name=product_name,
                category=category,
                stock=stock,
                product_image=product_image
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

            result = delete_product(
                product_id=product_id
            )

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


    # Get product image
    @app.route(
        '/uploads/products/<filename>',
        methods=['GET']
    )
    def get_product_image(filename):

        try:

            return send_from_directory(
                upload_folder,
                filename
            )

        except Exception as error:

            print("ERROR:", error)

            return jsonify({
                "error": "Product image not found."
            }), 404