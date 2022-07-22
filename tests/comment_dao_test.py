import pytest

from bp_main.dao import comment_dao
from bp_main.dao.comment import Comment

from bp_main.dao.comment_dao import CommentDAO


def check_fields(comment):
    fields = ["post_id", "commenter_name", "comment", "pk"]

    for field in fields:
        assert hasattr(comment, field), f"Нет поля{field}"


class TestCommentDAO:

    @pytest.fixture
    def comment_dao(self):
        comment_dao_instance = CommentDAO("comments_mock.json")
        return comment_dao_instance

    def test_get_comments_by_post_id_types(self, comment_dao):
        comment = comment_dao.get_comments_by_post_id(1)
        assert type(comment) == list, "Incorrect type for result"

    def test_get_all_fields(self, comment_dao):
        comment = comment_dao.get_comments_by_post_id(1)[0]
        check_fields(comment)

    ### Функция получения по id

    def test_get_comments_by_post_id_single_types(self, comment_dao):
        comment = comment_dao.get_comments_by_post_id(1)[0]
        assert type(comment) == Comment, "Incorrect type for result single item"

    def test_get_comments_by_post_id_not_content(self, comment_dao):
        comment = comment_dao.get_comments_by_post_id(88)
        assert comment == [], "У поста нет комментариев"
