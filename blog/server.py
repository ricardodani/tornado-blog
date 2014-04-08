# -*- coding: utf-8 -*-

import tornado.ioloop
from cow.server import Server
from cow.plugins.sqlalchemy_plugin import SQLAlchemyPlugin
from handlers import (
    MainHandler, AddPostHandler, PostHandler, PostCommentsHandler,
    AuthLoginHandler, AuthLogoutHandler
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
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
        )

    def get_settings(self):
        settings = super(BlogServer, self).get_settings()
        settings.update(dict(
            site_title='Tornado Blog',
            site_desc='A simple Tornado Blog written to learning purposes.',
            debug=True,
            cookie_secret='973590c362a6475f9a12e3151b253dc6'
        ))
        return settings

    def get_plugins(self):
        return [SQLAlchemyPlugin]

if __name__ == '__main__':
    BlogServer.run()
