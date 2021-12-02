from typing import List

from .base import BaseData
from .comment import comment


class Post(BaseData):
    def __init__(self, file_name):
        super().__init__(file_name)

    def get_all_with_comments(self) -> List[dict]:
        posts: List[dict] = self.get_all()
        return [{**post, 'comments': comment.get_by_post_id(post['pk'])} for post in posts]

    def get_by_username(self, username: str) -> List[dict]:
        posts: List[dict] = [post for post in self.get_all_with_comments() if post['poster_name'] == username]
        return sorted(posts, key=lambda post: post['pk'])

    def search(self, query: str) -> List[dict]:
        posts: List[dict] = self.get_all_with_comments()
        return [post for post in posts if query.lower() in post['content'].lower()]


post = Post('data.json')
