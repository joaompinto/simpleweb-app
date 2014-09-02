## -*- coding: utf-8 -*-
from simpleweb import controller
from os.path import join, exists, dirname
import re

class ViewSourcePage(object):

    @controller.publish
    def default(sel, *args):
        if len(args) != 1:
            return
        name = args[0]
        if not re.match('^([a-z_])+$', name):
            print "not match"
            return
        fname = join(dirname(__file__), name+'.py')
        if exists(fname):
            with open(fname) as f:
                code = f.read()
            return code


controller.attach('/view_source/', ViewSourcePage())