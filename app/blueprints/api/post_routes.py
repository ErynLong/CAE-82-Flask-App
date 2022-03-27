from . import bp as api
from app.models import GratitudePost, LyricsPost, PromptsPost
from flask import request, make_response, g, abort
from app.blueprints.auth.auth import token_auth


# return all the posts the user follows
@api.get('/gratitudeposts')
@token_auth.login_required()
def gratitude_get_posts():
    user = g.current_user
    posts = user.followed_posts()
    response_list=[]
    for post in posts:
        response_list.append(post.to_dict())
    return make_response({"posts":response_list},200)

# returns a single post from its id
@api.get('/gratitudeposts/<int:id>')
@token_auth.login_required()
def gratitude_get_single_post(id):
    user = g.current_user
    post = GratitudePost.query.get(id)
    if not post:
        abort(404)
    # check to make sure the user has access to the post
    if not user.is_following(post.author) and not post.author.id == user.id:
        abort(403, description="No No No not in my House")
    return make_response(post.to_dict(),200)


# {
#     "body": "the post body"
# }

# create a new post
@api.post('/gratitudeposts')
@token_auth.login_required()
def gratitude_post_post():
    posted_data = request.get_json() #retrieves the payload
    u=g.current_user
    post = GratitudePost(**posted_data)
    post.save()
    u.posts.append(post)
    u.save()
    return make_response(f"Post id: {post.id} created",200)

# {
#     "body": "the post body",
#     "id":2
# }
@api.put('/gratitudeposts')
@token_auth.login_required()
def gratitude_put_post():
    posted_data = request.get_json()
    post = GratitudePost.query.get(posted_data['id'])
    if not post:
        abort(404)
    if not post.author.id == g.current_user.id:
        abort(403)
    post.edit(posted_data['body'])
    return make_response(f"Post id: {post.id} has been changed",200)

# returns a single post from its id
@api.delete('/gratitudeposts/<int:id>')
@token_auth.login_required()
def gratitude_delete_post(id):
    user = g.current_user
    post = GratitudePost.query.get(id)
    if not post:
        abort(404)
    # check to make sure the user has access to the post
    if not post.author.id == user.id:
        abort(403, description="No No No not in my House")
    post.delete()
    return make_response(f"Success Post with id: {id} was deleted",200)

@api.get('/lyricsposts')
@token_auth.login_required()
def lyrics_get_posts():
    user = g.current_user
    posts = user.followed_posts()
    response_list=[]
    for post in posts:
        response_list.append(post.to_dict())
    return make_response({"posts":response_list},200)

# returns a single post from its id
@api.get('/lyricsposts/<int:id>')
@token_auth.login_required()
def lyrics_get_single_post(id):
    user = g.current_user
    post = LyricsPost.query.get(id)
    if not post:
        abort(404)
    # check to make sure the user has access to the post
    if not user.is_following(post.author) and not post.author.id == user.id:
        abort(403, description="No No No not in my House")
    return make_response(post.to_dict(),200)


# {
#     "body": "the post body"
# }

# create a new post
@api.post('/lyricsposts')
@token_auth.login_required()
def lyrics_post_post():
    posted_data = request.get_json() #retrieves the payload
    u=g.current_user
    post = LyricsPost(**posted_data)
    post.save()
    u.posts.append(post)
    u.save()
    return make_response(f"Post id: {post.id} created",200)

# {
#     "body": "the post body",
#     "id":2
# }
@api.put('/lyricsposts')
@token_auth.login_required()
def lyrics_put_post():
    posted_data = request.get_json()
    post = LyricsPost.query.get(posted_data['id'])
    if not post:
        abort(404)
    if not post.author.id == g.current_user.id:
        abort(403)
    post.edit(posted_data['body'])
    return make_response(f"Post id: {post.id} has been changed",200)

# returns a single post from its id
@api.delete('/lyricsposts/<int:id>')
@token_auth.login_required()
def lyrics_delete_post(id):
    user = g.current_user
    post = LyricsPost.query.get(id)
    if not post:
        abort(404)
    # check to make sure the user has access to the post
    if not post.author.id == user.id:
        abort(403, description="No No No not in my House")
    post.delete()
    return make_response(f"Success Post with id: {id} was deleted",200)

@api.get('/promptsposts')
@token_auth.login_required()
def prompts_get_posts():
    user = g.current_user
    posts = user.followed_posts()
    response_list=[]
    for post in posts:
        response_list.append(post.to_dict())
    return make_response({"posts":response_list},200)

# returns a single post from its id
@api.get('/promptsposts/<int:id>')
@token_auth.login_required()
def prompts_get_single_post(id):
    user = g.current_user
    post = PromptsPost.query.get(id)
    if not post:
        abort(404)
    # check to make sure the user has access to the post
    if not user.is_following(post.author) and not post.author.id == user.id:
        abort(403, description="No No No not in my House")
    return make_response(post.to_dict(),200)


# {
#     "body": "the post body"
# }

# create a new post
@api.post('/promptsposts')
@token_auth.login_required()
def prompts_post_post():
    posted_data = request.get_json() #retrieves the payload
    u=g.current_user
    post = PromptsPost(**posted_data)
    post.save()
    u.posts.append(post)
    u.save()
    return make_response(f"Post id: {post.id} created",200)

# {
#     "body": "the post body",
#     "id":2
# }
@api.put('/promptsposts')
@token_auth.login_required()
def prompts_put_post():
    posted_data = request.get_json()
    post = PromptsPost.query.get(posted_data['id'])
    if not post:
        abort(404)
    if not post.author.id == g.current_user.id:
        abort(403)
    post.edit(posted_data['body'])
    return make_response(f"Post id: {post.id} has been changed",200)

# returns a single post from its id
@api.delete('/promptsposts/<int:id>')
@token_auth.login_required()
def prompts_delete_post(id):
    user = g.current_user
    post = PromptsPost.query.get(id)
    if not post:
        abort(404)
    # check to make sure the user has access to the post
    if not post.author.id == user.id:
        abort(403, description="No No No not in my House")
    post.delete()
    return make_response(f"Success Post with id: {id} was deleted",200)