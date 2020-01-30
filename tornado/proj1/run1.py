import os
import tornado.ioloop
import tornado.web
import subprocess

static_path_dir=os.path.join(os.path.dirname(__file__), 'static')

class call1(tornado.web.RequestHandler):
	def get(self):
		print "Led ON1"
		self.write("Led ON2")
                subprocess.call("./bash1.sh", shell=True)

class MainHandler1(tornado.web.RequestHandler):
    def get(self):
        self.render("html1.html")




def make_app():
    return tornado.web.Application([
        (r"/call1", call1),
        (r'/static/(.*)', tornado.web.StaticFileHandler,  {'path': static_path_dir} ),
        (r"/", MainHandler1),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
