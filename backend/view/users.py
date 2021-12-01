from typing import List

from flask import Blueprint, render_template

from backend import model

users = Blueprint('users', __name__, url_prefix='/users')


@users.route('/<username>')
def index(username):
    posts: List[dict] = model.post.get_by_username(username.lower())
    return render_template('user-feed.html', posts=posts)
