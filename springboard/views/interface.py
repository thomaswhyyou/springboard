from pyramid.view import view_config


@view_config(route_name="feed", renderer="feed.html")
def feed(request):
    return {"foo": "barx"}
