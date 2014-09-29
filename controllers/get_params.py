## -*- coding: utf-8 -*-
from simpleweb import controller, template


class GetParamsPage(object):

    @controller.publish
    def index(self, name=None):
        upper_name = name.upper()
        return template.render('get_params.html', show_name=upper_name)

controller.attach('/get_params/', GetParamsPage())
