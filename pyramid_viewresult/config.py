import os.path
from .models import ViewResultContext


def search_paths_for_context(ctx):
    template = ctx.view.template
    ext = ctx.view_extension

    if template.startswith('~/'):
        if not template.endswith(ext):
            return ['%s.%s' % (template[2:], ext)]
        return [template[2:]]

    if ':' in template:
        if not template.endswith(ext):
            return ['%s.%s' % (template, ext)]
        return [template]

    if '.' in template:
        return [template]

    if '/' in template:
        if not template.endswith(ext):
            return ['%s.%s' % (template, ext)]
        return [template]

    filename = '%s.%s' % (template, ext)

    return [
    '%s/%s' % (ctx.name.lower(), filename),
    filename]


class ViewResultViewMapper(object):
    def __init__(self, **kw):
        self.kw = kw

    def __call__(self, view):
        attr = self.kw['attr']

        def wrapper(context, request):
            inst = view(request)
            registry = request.registry
            meth = getattr(inst, attr)
            result = meth(**request.matchdict)

            try:
                result.template = result.template or attr
            except AttributeError:
                return result

            cls = inst.__class__
            ctx = ViewResultContext()
            ctx.view = result
            ctx.view_extension = registry['viewresult.extension']
            ctx.name = cls.__name__.split('Controller', 1)[0]
            ctx.qual_name = '%s.%s.%s' % (cls.__module__, cls.__name__, attr)

            return ctx
        return wrapper
