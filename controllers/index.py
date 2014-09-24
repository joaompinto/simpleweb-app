from simpleweb import controller, template


class IndexPage(object):

    @controller.publish
    def index(self):
        return template.render('index.html')

controller.attach('/', IndexPage())