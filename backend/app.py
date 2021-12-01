from flask import Flask

from backend.model import comment
from view import main, posts, search, users

app = Flask(__name__)

for page in (main, posts, search, users):
    app.register_blueprint(page)


@app.context_processor
def utility_processor():
    def format_comment_word_ending(comment_count: int) -> str:
        return comment.format_comment_word_ending(comment_count)

    return dict(format_comment_word_ending=format_comment_word_ending)


if __name__ == "__main__":
    app.run(debug=True)
