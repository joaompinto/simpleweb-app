## -*- coding: utf-8 -*-
from simpleweb import controller, template


class FormPage(object):

    @controller.publish
    def index(self, **kwargs):
        if controller.method() == "GET":
            return template.render('form.html')
        else:
            # Form fields are received as key named arguments
            return self._submit(kwargs)

    def _submit(self, kwargs):
        # Pass the form fields to the template
        return template.render('form_submit.html', **kwargs)


controller.attach('/form/', FormPage())