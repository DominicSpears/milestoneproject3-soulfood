import os
from flask import (
    Flask, flash, render_template, abort,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# home function
@app.route("/")
@app.route("/get_home")
def get_home():
    return render_template("home.html")


# recipes function
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    users = list(mongo.db.users.find())
    return render_template("recipes.html", recipes=recipes, users=users)


# search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# register function
@app.route("/register", methods=["GET", "POST"])
def register():
    if is_authenticated():
        flash("Please Logout First to execute this operation")
        return redirect(url_for("get_home"))

    if request.method == "POST":

        # check if username exists
        username = request.form.get("username").lower()
        existing_user = mongo.db.users.find_one(
            {"username": username})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": username,
            "is_admin": "off",
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # add new user into 'session' cookie
        session["user"] = username
        flash("Congratulations - you are registered!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if is_authenticated():
        flash("Please Logout First to execute this operation")
        return redirect(url_for("get_home"))

    if request.method == "POST":
        # check if username exists in db
        username = request.form.get("username").lower()
        existing_user = mongo.db.users.find_one(
            {"username": username})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = username
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # password invalid
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # if username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# profile function
@app.route("/profile", methods=["GET", "POST"])
def profile():
    if is_authenticated():
        # get the session user's name from the database
        username = mongo.db.users.find_one_or_404(
            {"username": session["user"]})["username"]
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
        return render_template("profile.html", username=username,
                               recipes=recipes)

    flash('You are currently not logged in')
    return redirect(url_for("login"))


# logout function
@app.route("/logout")
def logout():
    if not is_authenticated():
        flash("You are currently not logged in")
        return redirect(url_for('get_home'))

    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# add recipe function
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if is_authenticated():
        if request.method == "POST":
            vegetarian = "on" if request.form.get("vegetarian") else "off"
            vegan = "on" if request.form.get("vegan") else "off"
            spicy = "on" if request.form.get("spicy") else "off"
            recipe = {
                "recipe_name": request.form.get("recipe_name"),
                "cuisine_name": request.form.get("cuisine_name"),
                "recipe_image": request.form.get("recipe_image"),
                "recipe_description": request.form.get("recipe_description"),
                "prep_time": request.form.get("prep_time"),
                "cook_time": request.form.get("cook_time"),
                "serves": request.form.get("serves"),
                "calories": request.form.get("calories"),
                "vegetarian": vegetarian,
                "vegan": vegan,
                "spicy": spicy,
                "allergens": request.form.getlist("allergens[]"),
                "ingredients": request.form.getlist("ingredients[]"),
                "method": request.form.getlist("method[]"),
                "created_by": session["user"]
            }
            mongo.db.recipes.insert_one(recipe)
            flash("Recipe Successfully Added")
            return redirect(url_for("get_recipes"))

        cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
        allergens = mongo.db.allergens.find().sort("allergens", 1)
        return render_template("add_recipe.html", cuisines=cuisines,
                               allergens=allergens)

    flash("You are currently not logged in")
    return redirect(url_for('get_home'))


# edit recipe function
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if is_authenticated():
        if not is_object_id_valid(recipe_id):
            abort(404)

        recipe_id = ObjectId(recipe_id)
        if request.method == "POST":
            # validate first if recipet exists
            mongo.db.recipes.find_one_or_404({"_id": recipe_id})

            vegetarian = "on" if request.form.get("vegetarian") else "off"
            vegan = "on" if request.form.get("vegan") else "off"
            spicy = "on" if request.form.get("spicy") else "off"
            submit = {
                "recipe_name": request.form.get("recipe_name"),
                "cuisine_name": request.form.get("cuisine_name"),
                "recipe_image": request.form.get("recipe_image"),
                "recipe_description": request.form.get("recipe_description"),
                "prep_time": request.form.get("prep_time"),
                "cook_time": request.form.get("cook_time"),
                "serves": request.form.get("serves"),
                "calories": request.form.get("calories"),
                "vegetarian": vegetarian,
                "vegan": vegan,
                "spicy": spicy,
                "allergens": request.form.getlist("allergens[]"),
                "ingredients": request.form.getlist("ingredients[]"),
                "method": request.form.getlist("method[]"),
                "created_by": session["user"]
            }
            mongo.db.recipes.update({"_id": recipe_id}, submit)
            flash("Recipe Successfully Updated")

        recipe = mongo.db.recipes.find_one_or_404({"_id": recipe_id})
        cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
        allergens = mongo.db.allergens.find().sort("allergens", 1)
        return render_template("edit_recipe.html", recipe=recipe,
                               cuisines=cuisines, allergens=allergens)

    flash("You are currently not logged in")
    return redirect(url_for('get_home'))


# view recipe function
@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    if not is_object_id_valid(recipe_id):
        abort(404)
    recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=recipe)


# delete recipe function
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    if is_authenticated():
        if not is_object_id_valid(recipe_id):
            abort(404)
        recipe_id = ObjectId(recipe_id)
        mongo.db.recipes.find_one_or_404({"_id": recipe_id})
        mongo.db.recipes.remove({"_id": recipe_id})
        flash("Recipe Successfully Deleted")
    else:
        flash("Unauthorized")

    return redirect(url_for("get_recipes"))


# cuisines function
@app.route("/get_cuisines")
def get_cuisines():
    if is_authenticated():
        cuisines = list(mongo.db.cuisines.find().sort("cuisine_name", 1))
        return render_template("cuisines.html", cuisines=cuisines)

    flash("You are currently not logged in")
    return redirect(url_for('get_home'))


# add cuisine function
@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if is_authenticated():
        if request.method == "POST":
            cuisine = {
                "cuisine_name": request.form.get("cuisine_name")
            }
            mongo.db.cuisines.insert_one(cuisine)
            flash("New Cuisine Added")
            return redirect(url_for("get_cuisines"))

        return render_template("add_cuisine.html")

    flash("You are currently not logged in")
    return redirect(url_for('get_home'))


# edit cuisine function
@app.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    if is_authenticated():
        if not is_object_id_valid(cuisine_id):
            abort(404)

        cuisine_id = ObjectId(cuisine_id)
        cuisine = mongo.db.cuisines.find_one_or_404(
            {"_id": cuisine_id})

        if request.method == "POST":
            submit = {
                "cuisine_name": request.form.get("cuisine_name")
            }
            mongo.db.cuisines.update({"_id": cuisine_id}, submit)
            flash("Cuisine Successfully Updated")
            return redirect(url_for("get_cuisines"))

        return render_template("edit_cuisine.html", cuisine=cuisine)

    flash("You are currently not logged in")
    return redirect(url_for('get_home'))


# delete cuisine function
@app.route("/delete_cuisine/<cuisine_id>")
def delete_cuisine(cuisine_id):
    if is_authenticated():
        if not is_object_id_valid(cuisine_id):
            abort(404)
        cuisine_id = ObjectId(cuisine_id)
        mongo.db.cuisines.find_one_or_404({"_id": cuisine_id})
        mongo.db.cuisines.remove({"_id": cuisine_id})
        flash("Cuisine Successfully Deleted")
    else:
        flash("Unauthorized action")

    return redirect(url_for("get_cuisines"))


# users function
@app.route("/get_users")
def get_users():
    if is_authenticated():
        users = list(mongo.db.users.find().sort("username", 1))
        return render_template("users.html", users=users)

    flash("You are currently not logged in")
    return redirect(url_for('get_home'))


# edit user function
@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if is_authenticated():
        if not is_object_id_valid(user_id):
            abort(404)

        user_id = ObjectId(user_id)
        user = mongo.db.users.find_one_or_404({"_id": user_id})

        if request.method == "POST":
            is_admin = "on" if request.form.get("is_admin") else "off"
            add = {
                "username": request.form.get("username"),
                "is_admin": is_admin,
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.update({"_id": user_id}, add)
            flash("User Successfully Updated")
            return redirect(url_for("get_users"))

        return render_template("edit_user.html", user=user)

    flash("You are currently not logged in")
    return redirect(url_for('get_home'))


# delete user function
@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    if is_authenticated():
        if not is_object_id_valid(user_id):
            abort(404)

        user_id = ObjectId(user_id)
        mongo.db.users.find_one_or_404({"_id": user_id})
        mongo.db.users.remove({"_id": user_id})
        flash("User Successfully Deleted")
    else:
        flash("Unauthorized")

    return redirect(url_for("get_users"))


# cookware function
@app.route("/get_cookware")
def get_cookware():
    cookware = list(mongo.db.cookware.find().sort("cookware_name", 1))
    return render_template("cookware.html", cookware=cookware)


# add cookware function
@app.route("/add_cookware", methods=["GET", "POST"])
def add_cookware():
    if is_authenticated():
        if request.method == "POST":
            cookware = {
                "cookware_name": request.form.get("cookware_name"),
                "cookware_image": request.form.get("cookware_image"),
                "cookware_link": request.form.get("cookware_link"),
                "cookware_price": request.form.get("cookware_price")
            }
            mongo.db.cookware.insert_one(cookware)
            flash("New Cookware Item Added")
            return redirect(url_for("get_cookware"))

        return render_template("add_cookware.html")

    flash("You are currently not logged in")
    return redirect(url_for('get_home'))


# edit cookware function
@app.route("/edit_cookware/<cookware_id>", methods=["GET", "POST"])
def edit_cookware(cookware_id):
    if is_authenticated():
        if not is_object_id_valid(cookware_id):
            abort(404)

        cookware_id = ObjectId(cookware_id)
        cookware = mongo.db.cookware.find_one_or_404(
            {"_id": cookware_id})

        if request.method == "POST":
            enter = {
                "cookware_name": request.form.get("cookware_name"),
                "cookware_image": request.form.get("cookware_image"),
                "cookware_link": request.form.get("cookware_link"),
                "cookware_price": request.form.get("cookware_price")
            }
            mongo.db.cookware.update({"_id": cookware_id}, enter)
            flash("Cookware Item Successfully Updated")
            return redirect(url_for("get_cookware"))

        return render_template("edit_cookware.html", cookware=cookware)

    flash("You are currently not logged in")
    return redirect(url_for('get_home'))


# delete cookware function
@app.route("/delete_cookware/<cookware_id>")
def delete_cookware(cookware_id):
    if is_authenticated():
        if not is_object_id_valid(cookware_id):
            abort(404)

        cookware_id = ObjectId(cookware_id)
        mongo.db.cookware.find_one_or_404({"_id": cookware_id})
        mongo.db.cookware.remove({"_id": cookware_id})
        flash("Cookware Item Successfully Deleted")
    else:
        flash("Unauthorized")

    return redirect(url_for("get_cookware"))


# Error messages
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_message/404.html'), 404


@app.errorhandler(500)
def internal_server(error):
    return render_template('error_message/500.html'), 500


def is_authenticated():
    """ Ensure that user is authenticated
    """
    return 'user' in session


def is_object_id_valid(id_value):
    """ Validate is the id_value is a valid ObjectId
    """
    return id_value != "" and ObjectId.is_valid(id_value)


# debug should = false when finalising project
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
