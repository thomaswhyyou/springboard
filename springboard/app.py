from pyramid.config import Configurator
from pyramid.view import view_config

@view_config(route_name="feed", renderer="feed.html")
def index(request):
    return {"foo": "barx"}


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Templating config
    config.include("pyramid_jinja2")
    config.add_jinja2_renderer('.html')

    # Routing config
    config.add_route("feed", "/")
    config.scan()

    # Static files config
    config.add_static_view("static", "springboard:static/")

    return config.make_wsgi_app()
