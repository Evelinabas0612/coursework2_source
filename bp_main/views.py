from json import JSONDecodeError

from bp_main.dao.comment_dao import CommentDAO
from config import POST_PATH, COMMENTS_PATH
from flask import Blueprint, render_template, request, logging, abort
from bp_main.dao.post_dao import PostDAO
#from utils import get_posts_by_user, get_posts_all, search_for_posts, get_post_by_pk

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")


post_dao = PostDAO(POST_PATH)
comment_dao = CommentDAO(COMMENTS_PATH)


@main_blueprint.route('/')
def main_page():
    '''Главная страница'''
    #posts = get_posts_all()
    posts = post_dao.get_all()
    return render_template('index.html', posts=posts)

#@post_blueprint.route('/posts/<int:pk>')
@main_blueprint.route('/posts/<int:pk>')
def post_pk_page(pk):
    '''Страница одного поста'''

    post = post_dao.get_by_pk(pk)
    comments = comment_dao.get_comments_by_post_id(pk)
    if post is None:
        abort(404)
    comment_count = len(comments)

    return render_template('post.html', post=post, comments=comments, comment_count=comment_count)

#@post_blueprint.route('/search/', methods=['GET'])
@main_blueprint.route('/search/')
def search_page():
    '''Страница поиска по слову'''
    search_query = request.args.get('s')
    logging.info('Выполняю поиск')
    try:
        posts_tag = post_dao.search_in_content(search_query)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    posts_count = len(posts_tag)
    return render_template('search.html', query=search_query, posts=posts_tag, count=posts_count)


@main_blueprint.route('users/<username>/')
def user_feed_page(username):
    '''Страница с постами пользователя'''
    try:
        posts = post_dao.get_by_poster(username)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('user_feed.html', posts=posts, username=username)

