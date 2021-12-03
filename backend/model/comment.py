from typing import List

import schemas
from model.base import BaseData


class Comment(BaseData):
    def get_by_post_id(self, post_id: int) -> List[schemas.Comment]:
        comments: List[schemas.Comment] = self.get_all()
        return [comment for comment in comments if comment.post_id == post_id]

    @staticmethod
    def format_comment_word_ending(comment_count: int) -> str:
        ending = ('ев', 'й', 'я')
        if comment_count == 0:
            return ending[0]
        elif 10 <= comment_count % 100 <= 20:
            return ending[0]
        elif comment_count % 10 == 1:
            return ending[1]
        elif 2 <= comment_count % 10 <= 4:
            return ending[2]
        else:
            return ending[0]


comment = Comment('comments.json', schemas.Comment)
