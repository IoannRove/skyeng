from typing import List

import schemas
from .base import BaseData
from .comment import comment


class Post(BaseData):

    def get_all_with_comments(self) -> List[schemas.Post]:
        posts: List[schemas.Post] = self.get_all()
        return [post._replace(comments=comment.get_by_post_id(post.pk)) for post in posts]

    def get_by_username(self, username: str) -> List[schemas.Post]:
        posts: List[schemas.Post] = [post for post in self.get_all_with_comments() if post.poster_name == username]
        return sorted(posts, key=lambda post: post.pk)

    def search(self, query: str) -> List[schemas.Post]:
        posts: List[schemas.Post] = self.get_all_with_comments()
        return [post for post in posts if query.lower() in post.content.lower()]


post = Post('data.json', schemas.Post)
