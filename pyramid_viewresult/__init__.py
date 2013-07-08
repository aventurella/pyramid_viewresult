from .controllers import Controller
from .renderers import jinja_render_fatcory


def set_viewresult_view_extension(config, value):
    ext = value[1:] if value.startswith('.') else value
    config.registry['viewresult.extension'] = ext


def includeme(config):
    """Set up standard configurator registrations.  Use via:

    .. code-block:: python

       config = Configurator()
       config.include('pyramid_viewresult')


    - ``set_viewresult_view_extension``: Set the default view extension. The
      default is 'html'

    """
    config.add_renderer(None, jinja_render_fatcory)
    config.add_directive('set_viewresult_view_extension', set_viewresult_view_extension)
    config.set_viewresult_view_extension('html')
