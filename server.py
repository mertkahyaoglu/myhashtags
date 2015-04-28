# -*- coding: utf-8 -*-
import web
import tweepy
import utils

urls = (
    '/', 'index',
    '/username/(.*)', 'username',
    '/notfound', 'notfound'
)

render = web.template.render('templates/', base='base')

count = 500

class index:
    def GET(self):
        return render.index()

class username:
    def GET(self, username):
        if username == "":
            raise web.seeother('/')
        hashtags = utils.getHashtags(username, count)
        if not hashtags:
            raise web.seeother('/notfound')
        return render.username(hashtags, username)

class notfound:
    def GET(self):
        return render.notfound()


if __name__ == "__main__":
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ("127.0.0.1", 3000))
