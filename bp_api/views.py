from flask import Blueprint, jsonify, abort
import logging

from bp_main.dao.comment_dao import CommentDAO
from bp_main.dao.post_dao import PostDAO
from config import POST_PATH, COMMENTS_PATH
#from utils import get_posts_all, get_post_by_pk

api_blueprint = Blueprint('api_blueprint', __name__)

post_dao = PostDAO(POST_PATH)
comment_dao = CommentDAO(COMMENTS_PATH)

api_logger = logging.getLogger("api_logger")


@api_blueprint.route('/posts/')
def api_all_posts_page():
    '''Эндпоинт.Возвращает все посты'''

    posts = post_dao.get_all()
    api_logger.debug('Загрузили все посты')
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:id>')
def api_posts_by_id_page(pk):
    '''Эндпоинт.Возвращает один пост'''
    post = post_dao.get_by_pk(pk)
    api_logger.debug(f'Загружен пост с индентификатором {pk}')
    if post is None:
        api_logger.error(f"Обращение к несуществующему посту {pk}")
        abort(404)
    return jsonify(post)

@api_blueprint.errorhandler(404)
def api_error_404(error):
    api_logger.error(f"Ошибка {error}")
    return jsonify({"error": str(error)}), 404


@api_blueprint.route('/')
def api_posts_start():
    return "Это API Стартовая"