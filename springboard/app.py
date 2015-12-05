from pyramid.config import Configurator
from pyramid.view import view_config

@view_config(route_name="index", renderer="index.html")
def index(request):
    return {"foo": "barx"}


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Templating config
    config.include("pyramid_jinja2")
    config.add_jinja2_renderer('.html')

    # Routing config
    config.add_route("index", "/")
    config.scan()

    return config.make_wsgi_app()
