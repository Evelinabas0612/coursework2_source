import json
from json import JSONDecodeError
from bp_main.dao.post import Post
from exception.data_exceptions import DataSourceError


class PostDAO:
    ''' Менеджер постов'''

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        '''Загружает данные из JSON  и возвращает список словарей'''
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Не удается получить данные из файла {self.path}')

        return posts_data

    def _load_posts(self):
        '''Загружает данные из JSON и возвращает список экземпляров'''
        posts_data = self._load_data()

        list_of_posts = [Post(**post_data) for post_data in posts_data]

        return list_of_posts

    def get_all(self):
        ''' Получает все посты,
        Возвращает список экземпляров класса Post '''

        posts = self._load_posts()

        return posts

    def get_by_pk(self, pk):
        ''' Получает пост по pk
        :param pk:
        :return:
        '''

        if type(pk) != int:
            raise TypeError("pk must be like int")

        posts = self._load_posts()
        for post in posts:
            if post.pk == pk:
                return post

    def search_in_content(self, substring):
        '''Ищет посты, где в контент встречается substring'''

        if type(substring) != str:
            raise TypeError("substring must be like str")

        substring = substring.lower()

        posts = self._load_posts()

        matching_posts = [post for post in posts if substring in post.content.lower()]

        return matching_posts

    def get_by_poster(self, user_name):
        '''Ищет посты с определённым автором'''
        if type(user_name) != str:
            raise TypeError("user_name must be like str")

        user_name = user_name.lower()

        posts = self._load_posts()

        matching_posts = [post for post in posts if post.poster_name.lower() == user_name]

        return matching_posts


