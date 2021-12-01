from typing import List

from flask import Blueprint, render_template

import model

posts = Blueprint('post', __name__, url_prefix='/posts')


@posts.route('/<postid>')
def index(postid):
    post_id = int(postid)
    post: dict = model.post.get_by_id(post_id)
    post_comments: List[dict] = model.comment.get_by_post_id(post_id)
    return render_template('post.html', post=post, comments=post_comments)
