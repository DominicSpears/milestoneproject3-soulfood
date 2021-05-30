import os
from flask import (
    Flask, flash, render_template,
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


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


#-------------------- register function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #-------------------- check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        #-------------------- new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Congratulations - you are registered!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


#-------------------- login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #-------------------- check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            #-------------------- ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                #-------------------- invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            #-------------------- username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


#-------------------- profile function
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    #-------------------- grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        vegetarian = "on" if request.form.get("vegetarian") else "off"
        vegan = "on" if request.form.get("vegan") else "off"
        spicy = "on" if request.form.get("spicy") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_description": request.form.get("recipe_description"),
            "prep_time": request.form.get("prep-time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "calories": request.form.get("calories"),
            "vegetarian": vegetarian,
            "vegan": vegan,
            "spicy": spicy,
            "allergens": request.form.getlist("allergens"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    allergens = mongo.db.allergens.find().sort("allergen", 1)
    return render_template("add_recipe.html", cuisines=cuisines, allergens=allergens)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        vegetarian = "on" if request.form.get("vegetarian") else "off"
        vegan = "on" if request.form.get("vegan") else "off"
        spicy = "on" if request.form.get("spicy") else "off"
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_description": request.form.get("recipe_description"),
            "prep_time": request.form.get("prep-time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "calories": request.form.get("calories"),
            "vegetarian": vegetarian,
            "vegan": vegan,
            "spicy": spicy,
            "allergens": request.form.getlist("allergens"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    allergens = mongo.db.allergens.find().sort("allergen", 1)
    return render_template("edit_recipe.html", recipe=recipe, cuisines=cuisines, allergens=allergens)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_cuisines")
def get_cuisines():
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_name", 1))
    return render_template("cuisines.html", cuisines=cuisines)


@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if request.method == "POST":
        cuisine = {
            "cuisine_name": request.form.get("cuisine_name")
        }
        mongo.db.cuisines.insert_one(cuisine)
        flash("New Cuisine Added")
        return redirect(url_for("get_cuisines"))

    return render_template("add_cuisine.html")


@app.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    if request.method == "POST":
        submit = {
            "cuisine_name": request.form.get("cuisine_name")
        }
        mongo.db.cuisines.update({"_id": ObjectId(cuisine_id)}, submit)
        flash("Cuisine Successfully Updated")
        return redirect(url_for("get_cuisines"))

    cuisine = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=cuisine)


@app.route("/delete_cuisine/<cuisine_id>")
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({"_id": ObjectId(cuisine_id)})
    flash("Cuisine Successfully Deleted")
    return redirect(url_for("get_cuisines"))


@app.route("/get_cookware")
def get_cookware():
    cookware = list(mongo.db.cookware.find().sort("cookware_name", 1))
    return render_template("cookware.html", cookware=cookware)


@app.route("/add_cookware", methods=["GET", "POST"])
def add_cookware():
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


@app.route("/edit_cookware/<cookware_id>", methods=["GET", "POST"])
def edit_cookware(cookware_id):
    if request.method == "POST":
        enter = {
            "cookware_name": request.form.get("cookware_name"),
            "cookware_image": request.form.get("cookware_image"),
            "cookware_link": request.form.get("cookware_link"),
            "cookware_price": request.form.get("cookware_price")
        }
        mongo.db.cookware.update({"_id": ObjectId(cookware_id)}, enter)
        flash("Cookware Item Successfully Updated")
        return redirect(url_for("get_cookware"))

    cookware = mongo.db.cookware.find_one({"_id": ObjectId(cookware_id)})
    return render_template("edit_cookware.html", cookware=cookware)


@app.route("/delete_cookware/<cookware_id>")
def delete_cookware(cookware_id):
    mongo.db.cookware.remove({"_id": ObjectId(cookware_id)})
    flash("Cookware Item Successfully Deleted")
    return redirect(url_for("get_cookware"))


# debug should = false when finalising project
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
