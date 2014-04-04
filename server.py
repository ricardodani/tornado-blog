# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Main blog")


class AddPostHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Add post")


class PostHandler(tornado.web.RequestHandler):
    def get(self, post_id):
        self.write("Post {}".format(post_id))


class PostCommentsHandler(tornado.web.RequestHandler):
    def get(self, post_id):
        self.write("Post {} comments".format(post_id))


application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/add', AddPostHandler),
    (r'/post/([0-9]+)', PostHandler),
    (r'/post/([0-9]+)/comments', PostCommentsHandler),
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
