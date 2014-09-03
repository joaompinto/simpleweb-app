## -*- coding: utf-8 -*-
from simpleweb import controller, template

class HelloPage(object):

    @controller.publish
    def index(self):
        return template.render('hello.html', word='world!')

controller.attach('/hello/', HelloPage())
