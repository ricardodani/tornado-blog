# -*- coding: utf-8 -*-

from tornado.testing import AsyncHTTPTestCase
from cow.testing import CowTestCase
from derpconf.config import Config  # NOQA
from server import BlogServer
from models import Post


class HandlersTestCase(CowTestCase):

    @property
    def db(self):
        return self.get_app().db

    #def setUp(self):
        #super(HandlersTestCase, self).setUp()
        #self.db.add_all([
            #Post(title="Post 1", description="Description 1", text="Text 1"),
            #Post(title="Post 2", description="Description 2", text="Text 2"),
        #])
        #self.db.commit()

    #def tearDown(self):
        #super(HandlersTestCase, self).tearDown()
        #self.db.commit()

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
        assert 'Post 1' in response.body
        assert 'Post 2' in response.body

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
