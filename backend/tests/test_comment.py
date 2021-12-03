from backend.model import comment


def test_comment_get_by_post_id():
    assert comment.get_by_post_id(-1) == []


def test_format_comment_word_ending():
    assert comment.format_comment_word_ending(0) == 'ев'
    assert comment.format_comment_word_ending(1) == 'й'
    assert comment.format_comment_word_ending(2) == 'я'
    assert comment.format_comment_word_ending(11) == 'ев'
    assert comment.format_comment_word_ending(21) == 'й'
    assert comment.format_comment_word_ending(22) == 'я'
    assert comment.format_comment_word_ending(25) == 'ев'


class A:
    def _a(self):
        print('_a')
    def __a(self):
        print('__a')