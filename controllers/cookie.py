## -*- coding: utf-8 -*-
from simpleweb import controller, template
import time


class CookiePage(object):

    @controller.publish
    def index(self, clear_first_visit=None):
        first_visit = controller.get_cookie('first_visit')
        if clear_first_visit:
            controller.delete_cookie('stored_name')
            first_visit = None
        else:
            if not first_visit:
                controller.set_cookie('first_visit', time.strftime("%x %X"))
        return template.render('cookie.html', first_visit=first_visit)

controller.attach('/cookie/', CookiePage())
