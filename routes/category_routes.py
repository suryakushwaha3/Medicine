from flask import request, jsonify

from operations.category_operation import (
    addCategory,
    getAllCategories,
    getSpecificCategory,
    updateCategory,
    deleteCategory
)

from operations.category_image import save_category_image


def category_routes(app):

    # =========================
    # ADD CATEGORY
    # =========================

    @app.route("/addCategory", methods=["POST"])
    def add_category():

        categoryName = request.form.get("category_name")

        if not categoryName:
            return jsonify({
                "success": False,
                "message": "Category name is required."
            }), 400

        categoryImage = request.files.get("category_image")

        if categoryImage is None:
            return jsonify({
                "success": False,
                "message": "Category image is required."
            }), 400

        result = save_category_image(
            categoryImage,
            "uploads/categories"
        )

        if "error" in result:
            return jsonify({
                "success": False,
                "message": result["error"]
            }), 400

        categoryId = addCategory(
            categoryName,
            result["filename"]
        )

        return jsonify({
            "success": True,
            "message": "Category added successfully.",
            "data": {
                "id": categoryId,
                "category_name": categoryName,
                "category_image": result["filename"]
            }
        }), 201


    # =========================
    # GET ALL CATEGORIES
    # =========================

    @app.route("/getAllCategories", methods=["GET"])
    def get_all_categories():

        categories = getAllCategories()

        return jsonify({
            "success": True,
            "data": categories
        }), 200


    # =========================
    # GET SPECIFIC CATEGORY
    # =========================

    @app.route("/getCategory/<int:categoryId>", methods=["GET"])
    def get_specific_category(categoryId):

        category = getSpecificCategory(categoryId)

        if not category:
            return jsonify({
                "success": False,
                "message": "Category not found."
            }), 404

        return jsonify({
            "success": True,
            "data": category
        }), 200


    # =========================
    # UPDATE CATEGORY
    # =========================

    @app.route("/updateCategory/<int:categoryId>", methods=["PUT"])
    def update_category(categoryId):

        categoryName = request.form.get("category_name")

        if not categoryName:
            return jsonify({
                "success": False,
                "message": "Category name is required."
            }), 400

        category = getSpecificCategory(categoryId)

        if not category:
            return jsonify({
                "success": False,
                "message": "Category not found."
            }), 404

        categoryImage = request.files.get("category_image")

        imageName = category[0]["category_image"]

        if categoryImage:

            result = save_category_image(
                categoryImage,
                "uploads/categories"
            )

            if "error" in result:
                return jsonify({
                    "success": False,
                    "message": result["error"]
                }), 400

            imageName = result["filename"]

        updated = updateCategory(
            categoryId,
            categoryName,
            imageName
        )

        if updated == 0:
            return jsonify({
                "success": False,
                "message": "Category update failed."
            }), 400

        return jsonify({
            "success": True,
            "message": "Category updated successfully."
        }), 200


    # =========================
    # DELETE CATEGORY
    # =========================

    @app.route("/deleteCategory/<int:categoryId>", methods=["DELETE"])
    def delete_category(categoryId):

        category = getSpecificCategory(categoryId)

        if not category:
            return jsonify({
                "success": False,
                "message": "Category not found."
            }), 404

        deleted = deleteCategory(categoryId)

        if deleted == 0:
            return jsonify({
                "success": False,
                "message": "Category delete failed."
            }), 400

        return jsonify({
            "success": True,
            "message": "Category deleted successfully."
        }), 200