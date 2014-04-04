# -*- coding: utf-8 -*-

import tornado.ioloop
from cow.server import Server
from cow.plugins.sqlalchemy_plugin import SQLAlchemyPlugin
from handlers import (
    MainHandler, AddPostHandler, PostHandler, PostCommentsHandler
)

class BlogServer(Server):

    def __init__(self, *args, **kwargs):
        super(BlogServer, self).__init__(*args, **kwargs)

    def after_start(self, io_loop):
        self.application.db = self.application.get_sqlalchemy_session()

    def get_handlers(self):
        return (
            (r'/', MainHandler),
            (r'/add', AddPostHandler),
            (r'/post/([0-9]+)', PostHandler),
            (r'/post/([0-9]+)/comments', PostCommentsHandler),
        )

    def get_plugins(self):
        return [SQLAlchemyPlugin]

if __name__ == '__main__':
    BlogServer.run()
