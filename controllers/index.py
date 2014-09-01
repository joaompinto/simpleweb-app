from simpleweb import controller, template

class IndexPage(object):

    @controller.publish
    def index(self):
        controller.set_cookie('xpto', 'xpto')
        return template.render('index.html')

controller.attach('/', IndexPage())