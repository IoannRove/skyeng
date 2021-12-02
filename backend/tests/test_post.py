from backend.model import post


def test_get_all_posts():
    posts = post.get_all()
    assert type(posts[0]) is dict
    assert len(posts) == 8


def test_get_all_posts_with_comments():
    posts_with_comments = post.get_all_with_comments()
    assert posts_with_comments[0].get('comments') is not None


def test_get_by_id():
    first_post = post.get_by_id(1)
    assert first_post['pk'] == 1


def test_get_by_username():
    posts = post.get_by_username('john')
    keys = [post['pk'] for post in posts]
    assert keys == sorted(keys)


