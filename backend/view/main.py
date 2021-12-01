from typing import List

from flask import Blueprint, render_template

from model import post

main = Blueprint('main', __name__, url_prefix='/')


@main.route("/")
def index():
    posts: List[dict] = post.get_all_with_comments()
    return render_template('index.html', posts=posts)
