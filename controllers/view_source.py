## -*- coding: utf-8 -*-
from simpleweb import controller, template
from pygments import highlight
from pygments.lexers import PythonLexer, MakoHtmlLexer
from pygments.formatters import HtmlFormatter
from os.path import join, exists, dirname, basename
import re


class ViewSourcePage(object):

    @controller.publish
    def default(self, *args):
        source_name = 'index' if len(args) == 0 else args[0]
        if not re.match('^([a-z_])+$', source_name):
            return
        filename = join(dirname(__file__), source_name+'.py')
        if not exists(filename):
            return

        with open(filename) as file:
            code = file.read()
        source = '<b>controllers/%s</b>' % basename(filename)
        source += highlight(code, PythonLexer(), HtmlFormatter(noclasses=True))
        source += self._dump_views_matching_regex("template.render\('([a-z_]*).", code)
        controller.set_response('Content-Type', 'text/html')
        return template.render('view_source.html', content=source)

    def _dump_views_matching_regex(self, regex, data):
        source = ''
        for source_name in re.findall(regex, data):
            filename = join(dirname(__file__), '..', 'views', source_name+'.html')
            if exists(filename):
                with open(filename) as file:
                    code = file.read()
                source += '<b>views/%s</b>' % basename(filename)
                source += highlight(code, MakoHtmlLexer(), HtmlFormatter(noclasses=True))
                # Displaying sub-templates makes the output too noisy, let's keep it commented
                #source += self._dump_views_matching_regex('%inherit file="([a-z_]+).', code)
        return source

controller.attach('/view_source/', ViewSourcePage())