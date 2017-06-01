#coding: utf-8

import django
from django.conf import settings
from django.test import TestCase

from preview_image_widget.widgets import PreviewImageWidget
from preview_image_widget.tests.utils import render_django110, render_django111


class TestSimpleImageWidget(TestCase):
    def setUp(self):
        super(TestSimpleImageWidget, self).setUp()
        self.widget = PreviewImageWidget()
        self.image = 'static/img/no-user.png'
        self.preview_url = settings.MEDIA_URL + self.image
        self.args = {
            'name': 'image',
            'value': self.image,
            'attrs': {
                'preview_image_widget': 1,
                'data-preview': self.preview_url
            }
        }
        if django.VERSION >= (1, 11, 0):
            self.render_method = render_django111
            self.args.update({
                'widget': self.widget
            })
        else:
            self.render_method = render_django110

    def tearDown(self):
        super(TestSimpleImageWidget, self).tearDown()
        del self.widget

    def test_widget(self):
        """
        Tests the widget render
        """
        html_expected = self.render_method(**self.args)
        self.assertEqual(self.widget.render('image', self.image), html_expected)
