from . import bp as api
from app.blueprints.auth.auth import token_auth
from flask import request, make_response, g, abort
from .models import *
from helpers import require_admin


############
##
##  CATEGORY API ROUTES
##
############


# Get all the Categories

@api.get('/category')
@token_auth.login_required()
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
@token_auth.login_required()
def get_items():
    items = Item.query.all()   
    items_dicts = [item.to_dict() for item in items]
    return make_response({"items":items_dicts},200)

# Get an item by its id
@api.get('/item/<int:id>')
@token_auth.login_required()
def get_item(id):
    item = Item.query.get(id)
    if not item:
        abort(404)
    return make_response(item.to_dict(),200)

# Get all items in a Category (by cat id)
@api.get('/item/category/<int:id>')
@token_auth.login_required()
def get_items_by_cat(id):
    cat = Category.query.get(id)
    if not cat:
        abort(404)
    all_items_in_cat = [item.to_dict() for item in cat.products]
    return make_response({"items":all_items_in_cat}, 200)

