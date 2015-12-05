from pyramid.view import view_config, view_defaults


@view_defaults(renderer="json")
class APIViews:
    def __init__(self, request):
        self.request = request

    # api/products
    @view_config(route_name='products')
    def home(self):
        return {"content": "Hello!"}
