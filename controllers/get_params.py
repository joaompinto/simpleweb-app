## -*- coding: utf-8 -*-
from simpleweb import controller, template


class GetParamsPage(object):

    @controller.publish
    def index(self, name=None):
        return template.render('get_params.html', show_name=name)

controller.attach('/get_params/', GetParamsPage())
