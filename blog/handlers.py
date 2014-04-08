# -*- coding: utf-8 -*-

import tornado
import tornado.auth
from models import Post


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_json = self.get_secure_cookie("chatdemo_user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)

    @property
    def global_context(self):
        return dict(user=self.get_current_user())

    def render(self, template, **kwargs):
        '''Adds global_context data to the render template env.
        '''
        context = self.global_context
        context.update(kwargs)
        super(BaseHandler, self).render(template, **context)


class MainHandler(BaseHandler):
    def get(self):
        self.render('home.html', posts=Post.get_recent_posts(self.db))


class AddPostHandler(BaseHandler):
    def get(self):
        self.write("Add post")


class PostHandler(BaseHandler):
    def get(self, post_id):
        self.write("Post {}".format(post_id))


class PostCommentsHandler(BaseHandler):
    def get(self, post_id):
        self.write("Post {} comments".format(post_id))


class AuthLoginHandler(BaseHandler, tornado.auth.GoogleMixin):
    @tornado.gen.coroutine
    def get(self):
        if self.get_argument("openid.mode", None):
            user = yield self.get_authenticated_user()
            self.set_secure_cookie("chatdemo_user",
                                   tornado.escape.json_encode(user))
            self.redirect("/")
            return
        self.authenticate_redirect(ax_attrs=["name"])


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("chatdemo_user")
        self.redirect("/")
