# Description: 	The View class contains the different pages that will be rendered. Transmits any commands to the
# 				BusinessLogic class.
# Author: 		Chloe Lee-Hone
# Date: 		14-07-2023
# Course: 		CST8276 - Advanced Database Topics

from flask import Flask, render_template, request
from BusinessLogic import BusinessLogic

app = Flask(__name__)
coordinator = BusinessLogic()

# Defines the landing page
@app.route("/")
def home():
	return render_template("index.html")


# Add a review to an existing item in the database
# Defines redirection after data has been posted
@app.route("/review", methods=["POST"])
def review_page():
	coordinator.insert_review(request)
	return render_template("data.html")


# Hands over control to the BusinessLogic class
# Redirects to the item catalogue page
@app.route("/insert_item", methods=["POST"])
def insert_item():
	coordinator.insert_item(request)
	items = coordinator.retrieve_all_item_data()
	return render_template("items.html", items=items)


# Gets all objects from the catalogue
# Redirects to the items catalogue page
@app.route("/items", methods=["GET"])
def view_items():
	items = coordinator.retrieve_all_item_data()
	return render_template("items.html", items=items)


# Retrieves the selected item's information from the database
# Uses the selected item's id to create a customized url
@app.route("/<string:item_id>")
def view_item(item_id):
	item = coordinator.get_item_data(item_id)
	reviews = coordinator.get_item_reviews(item_id)
	return render_template("itemDetails.html", item=item, reviews=reviews)

