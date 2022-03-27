from .import bp as social
from flask import render_template, flash, redirect, url_for, request
# from app.models import User,
from flask_login import login_required, current_user

@social.route('/index', methods=['GET'])
@login_required
def index():
    if request.method == 'GET':
#         body = request.form.get('body')
#         new_post = Post(user_id=current_user.id, body=body)
#         new_post.save()
#         return redirect(url_for('social.index'))    
#     posts = current_user.followed_posts()

        return render_template('index.html.j2')
    