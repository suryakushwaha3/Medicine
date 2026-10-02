from flask import request, jsonify

from operations.poster_operation import (
    addPoster,
    getAllPosters,
    getSpecificPoster,
    updatePoster,
    deletePoster
)

from operations.poster_image import save_poster_image


def poster_routes(app):

    # =========================curl.exe http://127.0.0.1:5000/getAllPosters
    # ADD POSTER
    # =========================

    @app.route("/addPoster", methods=["POST"])
    def add_poster():

        posterName = request.form.get("poster_name")

        if not posterName:
            return jsonify({
                "success": False,
                "message": "Poster name is required."
            }), 400

        posterImage = request.files.get("poster_image")

        if posterImage is None:
            return jsonify({
                "success": False,
                "message": "Poster image is required."
            }), 400

        result = save_poster_image(
            posterImage,
            "uploads/posters"
        )

        if "error" in result:
            return jsonify({
                "success": False,
                "message": result["error"]
            }), 400

        posterId = addPoster(
            posterName,
            result["filename"]
        )

        return jsonify({
            "success": True,
            "message": "Poster added successfully.",
            "data": {
                "id": posterId,
                "poster_name": posterName,
                "poster_image": result["filename"]
            }
        }), 201


    # =========================
    # GET ALL POSTERS
    # =========================

    @app.route("/getAllPosters", methods=["GET"])
    def get_all_posters():

        posters = getAllPosters()

        return jsonify({
            "success": True,
            "data": posters
        }), 200


    # =========================
    # GET SPECIFIC POSTER
    # =========================

    @app.route("/getPoster/<int:posterId>", methods=["GET"])
    def get_specific_poster(posterId):

        poster = getSpecificPoster(posterId)

        if not poster:
            return jsonify({
                "success": False,
                "message": "Poster not found."
            }), 404

        return jsonify({
            "success": True,
            "data": poster
        }), 200


    # =========================
    # UPDATE POSTER
    # =========================

    @app.route("/updatePoster/<int:posterId>", methods=["PUT"])
    def update_poster(posterId):

        posterName = request.form.get("poster_name")

        if not posterName:
            return jsonify({
                "success": False,
                "message": "Poster name is required."
            }), 400

        poster = getSpecificPoster(posterId)

        if not poster:
            return jsonify({
                "success": False,
                "message": "Poster not found."
            }), 404

        posterImage = request.files.get("poster_image")

        imageName = poster[0]["poster_image"]

        if posterImage:

            result = save_poster_image(
                posterImage,
                "uploads/posters"
            )

            if "error" in result:
                return jsonify({
                    "success": False,
                    "message": result["error"]
                }), 400

            imageName = result["filename"]

        updated = updatePoster(
            posterId,
            posterName,
            imageName
        )

        if updated == 0:
            return jsonify({
                "success": False,
                "message": "Poster update failed."
            }), 400

        return jsonify({
            "success": True,
            "message": "Poster updated successfully."
        }), 200


    # =========================
    # DELETE POSTER
    # =========================

    @app.route("/deletePoster/<int:posterId>", methods=["DELETE"])
    def delete_poster(posterId):

        poster = getSpecificPoster(posterId)

        if not poster:
            return jsonify({
                "success": False,
                "message": "Poster not found."
            }), 404

        deleted = deletePoster(posterId)

        if deleted == 0:
            return jsonify({
                "success": False,
                "message": "Poster delete failed."
            }), 400

        return jsonify({
            "success": True,
            "message": "Poster deleted successfully."
        }), 200