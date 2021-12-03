from typing import NamedTuple, Optional, List
from .comment import Comment


class Post(NamedTuple):
    poster_name: str
    poster_avatar: str
    pic: str
    content: str
    views_count: int
    likes_count: int
    pk: int
    comments: Optional[List[Comment]] = None

