import json
from json import JSONDecodeError
from bp_main.dao.comment import Comment
from exception.data_exceptions import DataSourceError


class CommentDAO:
    ''' Менеджер комментов'''

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        '''Загружает данные из JSON  и возвращает список словарей'''
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                comments_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Не удается получить данные из файла {self.path}')

        return comments_data

    def _load_comments(self):
        '''Загружает данные из JSON и возвращает список экземпляров'''
        comments_data = self._load_data()

        list_of_comments = [Comment(**comment_data) for comment_data in comments_data]

        return list_of_comments


    def get_comments_by_post_id(self, post_id):
        ''' Получает коммент по id
        :param post_id:
        :return:
        '''

        if type(post_id) != int:
            raise TypeError("id must be like int")

        comments = self._load_comments()
        result = []
        for comment in comments:
            if comment.post_id == post_id:
                result.append(comment)
        return result

