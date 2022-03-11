from sqlalchemy import desc
from . import bp as api
from app.blueprints.auth.auth import token_auth
from flask import request, make_response, g, abort
from .models import *
from helpers import require_admin
import stripe
import os
from collections import Counter


# This is your test secret API key.

stripe.api_key = os.environ.get('STRIPE_SK')
YOUR_DOMAIN = os.environ.get('HOST_ADDRESS')

@api.route('/create-checkout-session', methods=['POST'])
@token_auth.login_required()
def create_checkout_session():
    data=request.get_json()
    cart= data.get('cart')
    user=data.get('user')
    line_items=[]
    filtered_ids = map(lambda item: item['id'], cart)
    item_counts = Counter(filtered_ids)
    
    for item in cart:
        if item['id'] in item_counts:
            line_items.append({
                'name':item['name'],
                'amount':int(float(item['price'])*100),
                'quantity':item_counts[item['id']],
                'currency':'USD',
            })
            del item_counts[item['id']]

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url=YOUR_DOMAIN + 'checkoutsuccess',
            cancel_url=YOUR_DOMAIN + 'cart/true'
        )
        
    except Exception as e:
        return str(e)

    return make_response({"url":checkout_session.url},200)




############
##
##  CATEGORY API ROUTES
##
############


# Get all the Categories

@api.get('/category')
# @token_auth.login_required()
def get_category():
    cats = Category.query.all()   
    cats_dicts = [cat.to_dict() for cat in cats]
    return make_response({"categories":cats_dicts},200)


# create a new category
# {
#     "name":"my cat name"
# }
@api.post('/category')
@token_auth.login_required()
@require_admin
def post_category():
    cat_name = request.get_json().get("name")
    cat = Category(name=cat_name)
    cat.save()
    return make_response(f"category {cat.id} with name {cat.name} created", 200)

# Change my category
# {
#   "name":"new name"
# }
@api.put('/category/<int:id>')
@token_auth.login_required()
@require_admin
def put_category(id):
    cat_name = request.get_json().get("name")
    cat = Category.query.get(id)
    if not cat:
        abort(404)
    cat.name=cat_name
    cat.save()
    return make_response(f"Category {cat.id} has a new name: {cat.name}",200)

# Delete a category
@api.delete('/category/<int:id>')
@token_auth.login_required()
@require_admin
def delete_category(id):
    cat = Category.query.get(id)
    if not cat:
        abort(404)
    cat.delete()
    return make_response(f"Category {id} has been deleted.")


#############
##
##  ITEM API ROUTES
##
############

# Get All the items from the Shop
@api.get('/item')
# @token_auth.login_required()
def get_items():
    items = Item.query.all()   
    items_dicts = [item.to_dict() for item in items]
    return make_response({"items":items_dicts},200)

# Get an item by its id
@api.get('/item/<int:id>')
# @token_auth.login_required()
def get_item(id):
    item = Item.query.get(id)
    if not item:
        abort(404)
    return make_response(item.to_dict(),200)
{
    "id":3,
    "name":"name",

}
# Get all items in a Category (by cat id)
@api.get('/item/category/<int:id>')
# @token_auth.login_required()
def get_items_by_cat(id):
    cat = Category.query.get(id)
    if not cat:
        abort(404)
    all_items_in_cat = [item.to_dict() for item in cat.products]
    return make_response({"items":all_items_in_cat}, 200)

# Create a new Item
# {
#     "name":"string",
#     "desc":"string",
#     "price":"float",
#     "img":"string",
#     "category_id":"int"
# }
@api.post("/item")
@token_auth.login_required()
@require_admin
def post_item():
    item_dict = request.get_json()
    if not all(key in item_dict for key in ('name','desc','price','img','category_id')):
        abort(400)
    item = Item()
    item.from_dict(item_dict)
    item.save()
    return make_response(f"Item {item.name} was created with an id {item.id}",200)

@api.put('/item/<int:id>')
@token_auth.login_required()
@require_admin
def put_item(id):
    item_dict = request.get_json()
    item = Item.query.get(id)
    if not item:
        abort(404)
    item.from_dict(item_dict)
    item.save()
    return make_response(f"Item {item.name} with ID {item.id} has been updated", 200)

@api.delete('/item/<int:id>')
@token_auth.login_required()
@require_admin
def delete_item(id):
    item_to_delete = Item.query.get(id)
    if not item_to_delete:
        abort(404)
    item_to_delete.delete()
    return make_response(f"Item with id {id} has been deleted",200)