import json
from json import JSONDecodeError


def get_posts_all() -> list[dict]:
    '''загрузка постов'''
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            new_file = json.load(file)
    except(FileNotFoundError, JSONDecodeError):
        print('Не удается получить данные из файла')
    return new_file

def get_comments_all() -> list[dict]:
    '''загрузка комментов'''
    try:
        with open('comments.json', 'r', encoding='utf-8') as file:
            new_file = json.load(file)
    except(FileNotFoundError, JSONDecodeError):
        print('Не удается получить данные из файла')
    return new_file

def get_posts_by_user(user_name)-> list[dict]:
    '''поиск постов по пользователю'''
    posts = get_posts_all()
    result = []
    try:
        for post in posts:
            if post['poster_name'] == user_name:
                result.append(post)
    except ValueError:
        print(f'Не удается найти такого пользователя {user_name}')
    return result

def get_comments_by_post_id(post_id) -> list[dict]:
    '''вовзращает комментарии к посту'''
    comments = get_comments_all()
    result = []
    try:
        for comment in comments:
            if comment['post_id'] == post_id:
                result.append(comment)
    except ValueError:
        print(f'Не удается найти такой пост {post_id}')
    return result

def search_for_posts(query) -> list[dict]:
    '''возвращает список постов по ключевому слову'''
    query_lower = query.lower()
    posts = get_posts_all()
    result = []
    try:
        for post in posts:
            if query_lower in post['content'].lower():
                result.append(post)
    except ValueError:
        print(f'Не удается найти посты, которые содержат {query}')
    return result

def get_post_by_pk(pk) -> list:
    '''Возвращает пост по его индентификатору'''
    if type(pk) != int:
        raise TypeError("Введите число")
    posts = get_posts_all()
    result = []
    try:
        for post in posts:
            if post['pk'] == pk:
                result.append(post)
    except ValueError:
        print(f'Не удается найти посты по индентификатору {pk}')
    return result
