from flask import Blueprint, render_template

user_route = Blueprint("user", __name__)

@user_route.route("/")
def user_list(): # list the users
    return render_template("user_list.html")

@user_route.route("/", methods=["POST"])
def insert_user(): # insert the user data
    pass

@user_route.route("/new")
def form_user(): # form to register a user
    return render_template("form_user.html")

@user_route.route("/<int:user_id>")
def detail_user(user_id): # show user details
    return render_template("detail_user.html")

@user_route.route("/<int:user_id>/edit")
def form_edit_user(user_id): # form to edit a user
    return render_template("form_edit_user.html")

@user_route.route("/<int:user_id>/update", methods=["PUT"])
def update_user(user_id): # update user data
    pass

@user_route.route("/<int:user_id>/delete", methods=["DELETE"])
def delete_user(user_id): # delete user data
    pass