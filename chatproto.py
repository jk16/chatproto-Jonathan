import tornado.ioloop
import tornado.web
import json
from tornado import gen
import asyncio
from tornado.ioloop import IOLoop
from tornado.platform.asyncio import AsyncIOMainLoop


"""
* Client:
    * Chat Page
        * Message Buffer
            * Watch for new messages
        * Login Form
            * Nick name
            * Submit button
            * Submits data via ajax
            * If login is successful, will show Input Form
        * Input Form
            * Replaces Login Form after successful login
            * Input box for new messages
            * Submit button to send messages
        * Nick Buffer
            * Shows all chatters' nicks
            * When someone new joins, nick shows up here
            * When someone logs out or disconnects, nick goes away from here
* Server
    * Serves Chat Page
    * Answer login queries
    * Take message submissions
    * Rebroadcast message submissions
    * Rebroadcast nick logins/logouts
"""


class ChatPageHandler(tornado.web.RequestHandler):
    def get(self):
        """
        GET request from browser
        """
        self.render('chatpage.html')

class LoginPageHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self):
        response = {"success": True, "message": "logged in successfully"}
        self.set_header("Content-Type", "application/json")

        self.write(json.dumps(response))
                            #self.func_asyncio_coroutine() is a corotine function
                            #   and returns a coroutine
        #yield asyncio.async( self.func_asyncio_coroutine() )
                            #asyncio.async turns it into a Task ie type of 
                            #   asyncio Future which Tornado understands
        


    @asyncio.coroutine #this is the coroutine function
    def func_asyncio_coroutine(self):
        #asyncio is always yield from
        yield from asyncio.sleep(0.5)

class MessagePageHandler(tornado.web.RequestHandler):
    def post(self):
        response = {"success": True, "message": "message sent"}
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(response))

class LogoutPageHandler(tornado.web.RequestHandler):
    def post(self):
        response = {"success": True, "message":"logged out successfully"}
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(response))


def make_app():
    handlers = [
        (r"/", ChatPageHandler),
        ("/login" , LoginPageHandler),
        ("/msg", MessagePageHandler),
        ("/logout", LogoutPageHandler)
    ]
    return tornado.web.Application(handlers,debug=True,template_path='./templates',
            static_path='./static',static_url_prefix='/static/')



def main():
    AsyncIOMainLoop().install()
    app = make_app()
    app.listen(8888)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    """
    Purpose: If you use as a module code wont get executed
             If you use it as an executable it will get called 
    """
    main()








    































