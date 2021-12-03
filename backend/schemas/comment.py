from typing import NamedTuple


class Comment(NamedTuple):
    post_id: int
    pk: int
    commenter_name: str
    comment: str
