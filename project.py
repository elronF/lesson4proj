from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}
restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


# ROUTES FOR RESTAURANT

# View all restaurants
@app.route('/')
@app.route('/restaurants')
def restaurantList():
    return render_template('restaurants.html', restaurants=restaurants)
    #return "This is the page to see a list of restaurants"


# New restaurant
@app.route('/restaurants/new')
def newRestaurant():
    return render_template('newrestaurant.html')
    #return "This is the page to create a new restaurant"


# Edit restaurant
@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return render_template('editrestaurant.html', restaurants=restaurants, id=restaurant_id)
    #return "This is the page to edit the name of restaurant {}".format(restaurant_id)


# Delete restaurant
@app.route('/restaurants/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return render_template('deleterestaurant.html', restaurants=restaurants, id=restaurant_id)
    # return "This is the page to delete restaurant {}".format(restaurant_id)

# ROUTES FOR MENUS

# View menu
@app.route('/restaurants/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
	return "This is the page to view the menu for restaurant {}".format(restaurant_id)


# New menu item
@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id, menu_id):
    return "This is the page to create a new menu item for restaurant {}".format(restaurant_id)


# Edit menu item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "This is the page to edit menu item {} for restaurant {}".format(menu_id, restaurant_id)


# Delete menu item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
	return "This is the page to delete menu item {} for restaurant {}".format(menu_id, restaurant_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	