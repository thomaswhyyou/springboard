from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Configure templating
    config.include("pyramid_jinja2")
    config.add_jinja2_renderer('.html')

    # Configure routing & wire up views
    config.add_route("feed", "/")

    config.add_route("products", "/api/products")
    config.scan(".views")

    # Manage static files
    config.add_static_view("static", "springboard:static/")

    return config.make_wsgi_app()
