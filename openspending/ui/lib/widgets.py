# widgets config
import logging
from urlparse import urljoin
from pylons.i18n import _
from pylons import config, app_globals

log = logging.getLogger(__name__)


def get_widget(name):
    """ Get a dict to describe various properties of a named widget. """
    if not name in list_widgets():
        raise ValueError(_("No widget named '%s' exists.") % name)
    base_url = urljoin(app_globals.script_root + '/', 'widgets/')
    prefix = urljoin(base_url, name)

    widget_class = ''.join([p.capitalize() for p in name.split('_')])
    widget_class = 'OpenSpending.' + widget_class
    return {
        'js': '%s/main.js' % prefix,
        'base': prefix,
        'class_name': widget_class,
        'name': name
        }


def list_widgets():
    """ List of widgets registered in configuration file. """
    widgets = config.get('openspending.widgets', '').split()
    return map(lambda w: w.strip(), widgets)
