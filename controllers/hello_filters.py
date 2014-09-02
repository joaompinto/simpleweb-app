## -*- coding: utf-8 -*-
from simpleweb import controller, template


class HelloFiltersPage(object):

    @controller.publish
    def index(self):
        return template.render('hello_filters.html', name='Simple+Easy&Nice')

controller.attach('/hello_filters', HelloFiltersPage())