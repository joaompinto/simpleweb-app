from simpleweb import controller, template


class Hello(object):

    @controller.publish
    def index(self):
        return template.render('hello.html', word='world!')

controller.attach(Hello(), '/hello')