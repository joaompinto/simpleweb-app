## -*- coding: utf-8 -*-
from simpleweb import controller, template
from math import sqrt


class FormPage(object):

    @controller.publish
    def index(self, **kwargs):  # Form input fields are received as keyword arguments
        if controller.method() == "GET":
            return template.render('form.html')
        else:
            # For the template we provide the input variables extended with the sqrt result
            kwargs['number_sqrt'] = str(sqrt(float(kwargs['number'])))
            return template.render('form_submit.html', **kwargs)


controller.attach('/form/', FormPage())