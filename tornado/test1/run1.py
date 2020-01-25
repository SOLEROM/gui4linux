import tornado.ioloop
import tornado.web
import subprocess


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class MainHandler1(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("html1.html", title="My title", items=items)


class ledon(tornado.web.RequestHandler):
	def get(self):
		print "Led ON1"
		self.write("Led ON2")
                subprocess.call("/data/tornadoTests/test1/bash1.sh", shell=True)

class MainHandler2(tornado.web.RequestHandler):
    def get(self):
        self.render("html2.html")




def make_app():
    return tornado.web.Application([
        (r"/ledon", ledon),
        (r"/", MainHandler2),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
