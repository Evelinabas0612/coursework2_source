from flask import Flask

import logger
from bp_api.views import api_blueprint
from bp_main.views import main_blueprint
from exception.data_exceptions import DataSourceError

app = Flask(__name__)

def create_and_config_app(config_path):

    app.config['JSON_AS_ASCII'] = False
    app.config.from_pyfile(config_path)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')

    logger.config()
    return app


app = create_and_config_app("config.py")


@app.errorhandler(404)
def route_not_found(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def internal_server_error(error):
    return f"На сервере произошла ошибка {error}", 500


@app.errorhandler(DataSourceError)
def internal_data_source_error(error):
    return f"Поломались данные {error}", 500


if __name__ == '__main__':
    app.run(debug=True)
