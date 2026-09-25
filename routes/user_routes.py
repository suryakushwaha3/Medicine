from flask import jsonify, request
from operations.addOperation import createUser
from operations.authUser import authenticate_user
from operations.readOperation import getAllUsers, getSpacificUser
from operations.updatesOperation import update_user

def user_routes(app):

    # Test user API
    @app.route('/user', methods=['GET'])
    def get_user():
        return jsonify({'name': 'Surya', 'age': 22, 'city': 'Gorkhpur'})

    # Create / Signup user
    @app.route('/createUser', methods=['POST'])
    def create_user():
        try:
            name = request.form['name']
            password = request.form['password']
            phoneNumber = request.form['phoneNumber']
            email = request.form['email']
            pincode = request.form['pincode']
            address = request.form['address']

            response = createUser(
                name=name,
                password=password,
                phoneNumber=phoneNumber,
                email=email,
                pincode=pincode,
                address=address
            )

            return response

        except Exception as error:
            print("ERROR:", error)
            return jsonify({'message': 'error', 'status': 400}), 400

    # Login user
    @app.route('/login', methods=['POST'])
    def login_user():
        try:
            email = request.form['email']
            password = request.form['password']

            user = authenticate_user(
                email=email,
                password=password
            )

            if user:
                return jsonify({
                    'status': 200,
                    'Message': user[1]
                }), 200

            else:
                return jsonify({
                    'status': 401,
                    'Message': 'Invalid email or password'
                }), 401

        except Exception as error:
            print("ERROR:", error)
            return jsonify({'message': 'error', 'status': 400}), 400

    # Get all users
    @app.route('/getAllUsers', methods=['GET'])
    def get_All_users():
        try:
            return getAllUsers()

        except Exception as error:
            print("ERROR:", error)
            return jsonify({'message': 'error', 'status': 400}), 400

    # Get specific user
    @app.route('/getSpacificUser', methods=['POST'])
    def get_Spacific_User():
        try:
            userId = request.form['user_id']

            user = getSpacificUser(userId=userId)

            return jsonify(user)

        except Exception as error:
            print("ERROR:", error)
            return jsonify({'message': 'error', 'status': 400}), 400

    # Update user
    @app.route('/updateUser', methods=['PATCH'])
    def update_User():
        try:
            userId = request.form['user_id']

            update_fields = {}

            allowed_fields = [
                'password',
                'name',
                'address',
                'email',
                'phone_number',
                'pincode'
            ]

            for field in allowed_fields:
                if field in request.form:
                    update_fields[field] = request.form[field]

            if not update_fields:
                return jsonify({
                    'error': 'No fields provided for update'
                }), 400

            userUpdate = update_user(
                userID=userId,
                **update_fields
            )

            return jsonify(userUpdate), 200

        except Exception as error:
            print("ERROR:", error)

            return jsonify({
                'error': 'Failed to update user'
            }), 400