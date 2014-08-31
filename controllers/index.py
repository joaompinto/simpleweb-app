from simpleweb import controller, template


class Index(object):

    @controller.publish
    def index(self):
        return template.render('index.html', world='World!')

controller.attach(Index(), '/')