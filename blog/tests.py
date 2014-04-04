# -*- coding: utf-8 -*-

from tornado.testing import AsyncHTTPTestCase
from server import application


class HandlersTestCase(AsyncHTTPTestCase):

    def get_app(self):
        return application

    def test_home_handler(self):
        response = self.fetch('/')

        assert response.code == 200
        assert response.body == 'Main blog'

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
