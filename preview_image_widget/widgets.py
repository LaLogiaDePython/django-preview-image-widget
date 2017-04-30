from django.conf import settings
from django.forms import FileInput


class SimpleImageWidget(FileInput):
    """
    Autor: Milton Lenis
    Fecha: Abril 2 2017
    Widget para archivos de tipo imágen para mejorar un poco la apariencia visual de manera sencilla.
    """
    def __init__(self, *args, **kwargs):
        """
        Autor: Milton Lenis
        Fecha: Abril 2 2017
        Método constructor para agregar el atributo 'simple_image_widget' al campo y poder activarlo desde javascript
        :param args: Argumentos de la función
        :param kwargs: Keyword arguments de la función
        """
        kwargs['attrs'] = {
            'simple_image_widget': 1
        }
        super(SimpleImageWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        """
        Autor: Milton Lenis
        Fecha: Abril 2 2017
        Se sobrecarga el método render para agregar la imágen a la vista previa al editar en caso de que tenga un valor
        almacenado
        :param name:
        :param value:
        :param attrs:
        :return:
        """
        if value:
            preview = {"data-preview": settings.MEDIA_URL + str(value)}
            if attrs:
                attrs.update(preview)
            else:
                attrs = preview
        return super(SimpleImageWidget, self).render(name, value, attrs=attrs)

    class Media:
        css = {
            'all': ('plugins/simple_image_widget/simple_image_widget.css',)
        }
        js = ('plugins/simple_image_widget/simple_image_widget.js',)
