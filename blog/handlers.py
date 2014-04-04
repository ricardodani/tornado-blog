# -*- coding: utf-8 -*-

import tornado
from models import Post

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        posts = self.application.db.query(Post).all()
        self.write("Main blog {}!".format(len(posts)))


class AddPostHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Add post")


class PostHandler(tornado.web.RequestHandler):
    def get(self, post_id):
        self.write("Post {}".format(post_id))


class PostCommentsHandler(tornado.web.RequestHandler):
    def get(self, post_id):
        self.write("Post {} comments".format(post_id))
