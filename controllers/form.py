## -*- coding: utf-8 -*-
from simpleweb import controller, template
from math import sqrt


class FormPage(object):

    @controller.publish
    def index(self, **kwargs):
        if controller.method() == "GET":
            return template.render('form.html')
        else:
            # Form input fields are received as keyword arguments
            # The submit template will use the submitted arguments
            # extended with the sqrt result
            kwargs['number_sqrt'] = sqrt(float(kwargs['number']))
            return template.render('form_submit.html', **kwargs)


controller.attach('/form/', FormPage())