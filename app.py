from flask import Flask
from database.views import products, shopCar
from conf.config import DevelopmentConfig

ACTIVE_ENDPOINTS = [('/products', products), ('/shopcar', shopCar)]

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
