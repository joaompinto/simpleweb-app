## -*- coding: utf-8 -*-
from simpleweb import controller, template


class HelloPage(object):

    @controller.publish
    def index(self):
        return "Hello world!"


class HelloTemplatePage(object):

    @controller.publish
    def index(self):
        return template.render('hello.html', word='world!')

controller.attach('/hello/', HelloPage())
controller.attach('/hello_using_template/', HelloTemplatePage())
