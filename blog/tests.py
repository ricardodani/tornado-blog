# -*- coding: utf-8 -*-

from tornado.testing import AsyncHTTPTestCase
from cow.testing import CowTestCase
from derpconf.config import Config  # NOQA
from server import BlogServer


class HandlersTestCase(CowTestCase):
    def get_config(self):
        config = Config(
            SQLALCHEMY_CONNECTION_STRING="mysql+mysqldb://root@localhost:3306/test_tornado_blog",
            SQLALCHEMY_POOL_SIZE=1,
            SQLALCHEMY_POOL_MAX_OVERFLOW=0,
            SQLALCHEMY_AUTO_FLUSH=True,
        )
        return config

    def get_server(self):
        return BlogServer(config=self.get_config())

    def test_home_handler(self):
        response = self.fetch('/')

        assert response.code == 200
        assert response.body == 'Main blog 0!'

    def test_add_handler(self):
        response = self.fetch('/add')

        assert response.code == 200
        assert response.body == 'Add post'

    def test_post_handler(self):
        response = self.fetch('/post/1')

        assert response.code == 200
        assert response.body == 'Post 1'

    def test_post_comments_handler(self):
        response = self.fetch('/post/1/comments')

        assert response.code == 200
        assert response.body == 'Post 1 comments'
