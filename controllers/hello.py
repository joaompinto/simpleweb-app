## -*- coding: utf-8 -*-
from simpleweb import controller, template


class HelloPage(object):

    @controller.publish
    def index(self, using_template=None):
        if using_template:
            return template.render('hello.html', word='world!')
        else:
            return "Hello world!"

controller.attach('/hello', HelloPage())