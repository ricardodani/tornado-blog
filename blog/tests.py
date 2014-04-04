# -*- coding: utf-8 -*-

from tornado.testing import AsyncHTTPTestCase
from cow.testing import CowTestCase
from server import BlogServer


class HandlersTestCase(CowTestCase):

    def get_server(self):
        return BlogServer()

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
