# -*- coding: utf-8 -*-

import tornado
from models import Post


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class MainHandler(BaseHandler):
    def get(self):
        self.render('home.html', posts=Post.get_posts(self.db))


class AddPostHandler(BaseHandler):
    def get(self):
        self.write("Add post")


class PostHandler(BaseHandler):
    def get(self, post_id):
        self.write("Post {}".format(post_id))


class PostCommentsHandler(BaseHandler):
    def get(self, post_id):
        self.write("Post {} comments".format(post_id))
