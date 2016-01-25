import tornado.ioloop
import tornado.web
import json
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
    def post(self):
        response = {"success": True, "message": "LOGGED IN"}
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(response))

class MessagePageHandler(tornado.web.RequestHandler):
    def post(self):
        response = {"success": True}
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(response))
        
def make_app():
    handlers = [
        (r"/", ChatPageHandler),
        ("/login" , LoginPageHandler),
        ("/msg", MessagePageHandler)
    ]
    return tornado.web.Application(handlers,debug=True,template_path='./templates',
            static_path='./static',static_url_prefix='/static/')



def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    """
    Purpose: If you use as a module code wont get executed
             If you use it as an executable it will get called 
    """
    main()








    































