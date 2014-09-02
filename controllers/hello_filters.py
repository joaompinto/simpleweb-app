## -*- coding: utf-8 -*-
from simpleweb import controller, template


class HelloFiltersPage(object):

    @controller.publish
    def index(self):
        args = {'content': '< This needs HTML filtering>'
                , 'link': u'Hello Günter'}
        return template.render('hello_filters.html', **args)

controller.attach('/hello_filters', HelloFiltersPage())