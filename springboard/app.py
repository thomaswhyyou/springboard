from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from springboard.models import sess, Base


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Configure database connection
    engine = engine_from_config(settings, 'sqlalchemy.')
    sess.configure(bind=engine)
    Base.metadata.bind = engine

    # Configure renderer
    config.include("pyramid_jinja2")
    config.add_jinja2_renderer('.html')

    # Configure routing & wire up views
    config.add_route("feed", "/")
    config.add_route("products", "/api/products")
    config.scan(".views")

    # Manage static files
    config.add_static_view("static", "springboard:static/")

    return config.make_wsgi_app()
