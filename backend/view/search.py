from typing import List

from flask import Blueprint, render_template, request

import model

search = Blueprint('search', __name__, url_prefix='/search')


@search.route('/')
def index():
    query = request.args.get('s')
    posts: List[dict] = model.post.search(query)
    return render_template('search.html', posts=posts)
