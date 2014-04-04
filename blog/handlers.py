# -*- coding: utf-8 -*-

import tornado


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
