from pyramid.httpexceptions import HTTPFound
from .models import ViewResult
from .config import ViewResultViewMapper


class Controller(object):
    __view_mapper__ = ViewResultViewMapper

    def __init__(self, request):
        self.request = request
        self.view_data = {}

    def view(self, model=None, template=None):
        result = ViewResult()
        result.template = template
        result.model = model or self.view_data
        return result

    def redirect_to_route(self, route_name, *elements, **kw):
        return self.redirect(self.request.route_url(
            route_name,
            *elements,
            **kw))

    def redirect(self, location, headers=None):
        return HTTPFound(location=location, headers=headers)
