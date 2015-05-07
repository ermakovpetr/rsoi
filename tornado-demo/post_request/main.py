import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template.html")

    def post(self):
        id = self.get_argument('id', '')

        if not id:
            response = {
                'error': True, 
                'msg': 'id is None'
            }
        else:
            response = {
                'error': False, 
                'msg': 'All right'
            }

        # redirect after post
        # http://habrahabr.ru/post/86258/

        self.write(response)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
