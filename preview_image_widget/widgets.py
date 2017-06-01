from django.conf import settings
from django.forms import FileInput


class PreviewImageWidget(FileInput):
    """
    Widget for displaying a image-preview in file fields.
    """
    def __init__(self, *args, **kwargs):
        """
        Adds a 'preview_image_widget' attr for the input
        """
        kwargs['attrs'] = {
            'preview_image_widget': 1
        }
        super(PreviewImageWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        """
        Adds the previous value of the file to an attr, if there is any, for preview.
        """
        if value:
            preview = {"data-preview": settings.MEDIA_URL + str(value)}
            if not attrs:
                attrs = {}
            attrs.update(preview)
        return super(PreviewImageWidget, self).render(name, value, attrs=attrs)

    class Media:
        css = {
            'all': ('plugins/preview_image_widget/preview_image_widget.css',)
        }
        js = ('plugins/preview_image_widget/preview_image_widget.js',)
