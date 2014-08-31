from simpleweb import controller, template


class Cookies(object):

    @controller.publish
    def index(self, Name=None, clear_cookie=None):
        if clear_cookie:
            stored_name = None
            controller.delete_cookie('stored_name')
        if Name:  # Receiving data from form submit
            stored_name = Name
            controller.set_cookie('stored_name', Name)
        else:
            stored_name = controller.get_cookie('stored_name')
        return template.render('cookies.html', stored_name=stored_name)


controller.attach('/cookies/', Cookies())