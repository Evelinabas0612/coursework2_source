import pytest

from main import app


class TestApi:
    post_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    @pytest.fixture
    def app_instance(self):
        return app.test_client()

    def test_posts_has_all_type(self, app_instance):
        response = app_instance.get('/api/posts/')
        result = response.get_json()
        assert type(result) == list

    def test_posts_has_all_correct_keys(self, app_instance):
        response = app_instance.get('/api/posts/')
        result = response.get_json()
        result_keys = set(result[0].keys())
        assert result_keys == self.post_keys

    def test_posts_has_single_type(self, app_instance):
        response = app_instance.get('/api/posts/')
        result = response.get_json()
        assert type(result) == dict

    def test_posts_has_single_correct_keys(self, app_instance):
        response = app_instance.get('/api/posts/')
        result = response.get_json()
        result_keys = set(result.keys())
        assert result_keys == self.post_keys

