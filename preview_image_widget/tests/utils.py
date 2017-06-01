from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.safestring import mark_safe

try:
    from django.forms.renderers import get_default_renderer
except ImportError:
    def get_default_renderer():
        return None

def render_django111(**kwargs):
    """
    Renders the widget using the django 1.11+ way
    :param kwargs: key word arguments with the test data
    :return: widget rendered
    """
    widget = kwargs.pop("widget")
    renderer = get_default_renderer()
    context = widget.get_context(kwargs['name'], kwargs['value'], kwargs['attrs'])
    return mark_safe(renderer.render('django/forms/widgets/input.html', context))

def render_django110(**kwargs):
    """
    Renders the widget using the django 1.11+ way
    :param kwargs: key word arguments with the test data
    :return: widget rendered
    """
    final_attrs = {'type': 'file', 'name': kwargs['name']}
    final_attrs.update(kwargs['attrs'])
    html_expected = format_html('<input{} />', flatatt(final_attrs))
    return html_expected