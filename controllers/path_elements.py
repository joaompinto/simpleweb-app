from simpleweb import controller, template


class PathElementsPage(object):

    @controller.publish
    def default(self, *params):
        template_args = {'current_path': '/'.join(params),
                         'next_path': len(params)}
        return template.render('path_elements.html', **template_args)


controller.attach('/path_elements/', PathElementsPage())