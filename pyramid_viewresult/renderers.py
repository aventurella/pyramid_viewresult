import sys
from jinja2.exceptions import TemplatesNotFound
from jinja2.exceptions import TemplateNotFound
from pyramid_jinja2 import _get_or_build_default_environment
from pyramid_jinja2 import Jinja2TemplateRenderer
from .config import search_paths_for_context


class ViewResultJinjaRenderer(Jinja2TemplateRenderer):

    def __init__(self, info, environment):
        super(ViewResultJinjaRenderer, self).__init__(info, environment)
        self.location_cache = {}

    @property
    def template(self):
        view_context = self.info.view_context
        name = view_context.view.template
        key = '%s:%s' % (view_context.qual_name, name)
        path = self.location_cache.get(key, None)

        if not path:
            candidates = search_paths_for_context(view_context)
            for each in candidates:
                try:
                    template = self.environment.get_template(each)
                    self.location_cache[key] = each
                    return template
                except TemplateNotFound:
                    continue
            raise TemplatesNotFound(candidates)

        return self.environment.get_template(path)

    def __call__(self, view_context, system):
        model = view_context.view.model
        self.info.view_context = view_context

        return super(ViewResultJinjaRenderer, self).\
            __call__(model, system)


def jinja_render_factory(info):
    environment = _get_or_build_default_environment(info.registry)
    return ViewResultJinjaRenderer(info, environment)
