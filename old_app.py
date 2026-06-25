from flask import Flask, request


# create an instance of flask -> central registry
app = Flask(__name__)


user_list = [
    {"id": 1, "firstName": "John", "lastName": "Doe", "email": "john@gmail.com"},
    {"id": 2, "firstName": "Jane", "lastName": "Doe", "email": "jane@gmail.com"},
    {"id": 3, "firstName": "Jack", "lastName": "Sparrow", "email": "jack@gmail.com"},
    {"id": 4, "firstName": "Alex", "lastName": "Hormozi", "email": "alex@gmail.com"},
    {
        "id": 5,
        "firstName": "Michael",
        "lastName": "Scofield",
        "email": "michael@gmail.com",
    },
]


# default HTTP verb is -> GET
@app.route("/")
def index():
    return "Hello, World!"


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        return {"message": "POST Method"}

    return user_list


@app.route("/users/<int:id>")
def get_user(id):
    response = {"id": id}

    return response


@app.route("/users/<int:id>", methods=["PUT", "PATCH"])
def update_user(id):
    if request.method == "PATCH":
        return {"id": id, "message": "PATCH Method"}

    if request.method == "PUT":
        return {"id": id, "message": "PUT Method"}


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    if request.method == "DELETE":
        return {"id": id, "message": "DELETE Method"}


# @app.post()
# @app.put()
# @app.delete()

# CRUD -> CREATE -> READ -> UPDATE -> DELETE
# CRUD Monkey
# add user
# get a user
# get all users
# update one user
# delete one user

# rookie way - NOT RECOMMENDED WAY
# CREATE
# @app.route("/addUser")
# @app.route("/add-user")

# READ
# @app.route("/getUser")
# @app.route("/getUsers")

# UPDATE
# @app.route("/updateUser")

# DELETE
# @app.route("/deleteUser")

# RECOMMENDED CONVENTION
# @app.route("/users") -> get all users (GET)
# @app.route("/users") -> add a user (POST)
# @app.route("/users/<id>") -> get one user (GET)
# @app.route("/users/<id>") -> update one user (PUT)
# @app.route("/users/<id>") -> delete one user (DELETE)

# @app.route("/customers")
# @app.route("/products")

# /users
# /users/

if __name__ == "__main__":
    app.run(port=5555, debug=True)
