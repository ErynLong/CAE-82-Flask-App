from .import bp as main
from flask import render_template, redirect, url_for, flash, request
import requests
from app.models import User, LyricsPost, GratitudePost, PromptsPost
from flask_login import  login_required, current_user


# @main.route('/students', methods=['GET'])
# @login_required
# def students():
#     my_students = ['Caleb', 'Kristen', 'Eryn', 'Zak', 'David']
#                                             #  Name in Jinja = name in python
#     return render_template('students.html.j2', students = my_students)

@main.route('/lyrics', methods = ['GET', 'POST'])
@login_required
def lyrics():
    if request.method == 'POST':
        body = request.form.get('body')
        new_post = LyricsPost(user_id=current_user.id, body=body)
        new_post.save()
        return redirect(url_for('main.lyrics'))    
    posts = current_user.lyrics_followed_posts()

    return render_template('lyrics.html.j2', posts = posts)

@main.route('/post/<int:id>')
@login_required
def get_post(id):
    post = LyricsPost.query.get(id)
    return render_template('lyrics.html.j2', post=post, view_all=True)

@main.route('/post/my_posts')
@login_required
def my_posts():
    # get all the posts for the person using my site
    posts = current_user.posts
    return render_template('lyrics.html.j2',posts=posts)

@main.route('edit_post/<int:id>', methods=['GET','POST'])
@login_required
def edit_post(id):
    post = LyricsPost.query.get(id)
    if post and post.user_id != current_user.id:
        flash('Stop trying to hack my system!','danger')
        return redirect(url_for('main.lyrics'))
    if request.method=="POST":
        post.edit(request.form.get('body'))
        flash("Your post has been edited","success")

    return render_template('lyrics.html.j2', post=post)

@main.route('/gratitude', methods = ['GET', 'POST'])
@login_required
def gratitude():
    if request.method == 'POST':
        body = request.form.get('body')
        new_post = GratitudePost(user_id=current_user.id, body=body)
        new_post.save()
        return redirect(url_for('main.gratitude'))    
    posts = current_user.gratitude_followed_posts()

    return render_template('gratitude.html.j2', posts = posts)

@main.route('/gratitudepost/<int:id>')
@login_required
def gratitude_get_post(id):
    post = GratitudePost.query.get(id)
    return render_template('lyrics.html.j2', post=post, view_all=True)

@main.route('/gratitudepost/my_posts')
@login_required
def gratitude_my_posts():
    # get all the posts for the person using my site
    posts = current_user.posts
    return render_template('lyrics.html.j2',posts=posts)

@main.route('gratitudeedit_post/<int:id>', methods=['GET','POST'])
@login_required
def gratitude_edit_post(id):
    post = GratitudePost.query.get(id)
    if post and post.user_id != current_user.id:
        flash('Stop trying to hack my system!','danger')
        return redirect(url_for('main.gratitude'))
    if request.method=="POST":
        post.edit(request.form.get('body'))
        flash("Your post has been edited","success")

    return render_template('gratitude.html.j2', post=post)

@main.route('/prompts', methods = ['GET', 'POST'])
@login_required
def prompts():
    if request.method == 'POST':
        body = request.form.get('body')
        new_post = PromptsPost(user_id=current_user.id, body=body)
        new_post.save()
        return redirect(url_for('main.prompts'))    
    posts = current_user.prompts_followed_posts()

    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = {
        "key1": "value",
        "key2": "value"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com",
        "X-RapidAPI-Key": "d0b19964a5msh13047347e1a34ddp1c245ajsn0c6778216de1"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    quotes=response.text

    return render_template('prompts.html.j2', posts = posts, quotes=quotes)

@main.route('/promptspost/<int:id>')
@login_required
def prompts_get_post(id):
    post = PromptsPost.query.get(id)
    return render_template('prompts.html.j2', post=post, view_all=True)

@main.route('/promptspost/my_posts')
@login_required
def prompts_my_posts():
    # get all the posts for the person using my site
    posts = current_user.posts
    return render_template('prompts.html.j2',posts=posts)

@main.route('promptsit_post/<int:id>', methods=['GET','POST'])
@login_required
def prompts_edit_post(id):
    post = PromptsPost.query.get(id)
    if post and post.user_id != current_user.id:
        flash('Stop trying to hack my system!','danger')
        return redirect(url_for('main.gratitude'))
    if request.method=="POST":
        post.edit(request.form.get('body'))
        flash("Your post has been edited","success")

    return render_template('prompts.html.j2', post=post)
