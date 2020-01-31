import os
import logging

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop


from subprocess import Popen, PIPE, STDOUT
from tornado.process import Subprocess


from tornado.options import define, options


static_path_dir=os.path.join(os.path.dirname(__file__), 'static')

class call1(tornado.web.RequestHandler):
    def get(self):
        logging.info("call1::get")
        self.write("self.write=msg1")
        ##subprocess stdout print
        p=Popen("./bash1.sh", shell=True,stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        self.write(output)

class call2(tornado.websocket.WebSocketHandler):
    def open(self):
         logging.info("call2::open")
         filename = "/tmp/b"
         self.proc = Subprocess(["tail", "-f", filename, "-n", "0"],stdout=Subprocess.STREAM,bufsize=1)
         self.proc.set_exit_callback(self._close)
         self.proc.stdout.read_until("\n", self.write_line)

    def _close(self, *args, **kwargs):
        self.close()

    def on_close(self, *args, **kwargs):
        logging.info("trying to kill process")
        self.proc.proc.terminate()
        self.proc.proc.wait()

    def write_line(self, data):
       logging.info("Returning to client: %s" % data.strip())
       self.write_message(data.strip() + "<br/>")
       self.proc.stdout.read_until("\n", self.write_line)


class call3(call2):
    def open(self):
         print "call3::open"
         self.proc = Subprocess(["./bash1.sh"],stdout=Subprocess.STREAM,bufsize=1)
         ## if subprocess is ending no need for exit callback!!!
         #self.proc.set_exit_callback(self._close)
         self.proc.stdout.read_until("\n", self.write_line)



class MainHandler1(tornado.web.RequestHandler):
    def get(self):
        self.render("html1.html")




def make_app():
    return tornado.web.Application([
        (r"/call1", call1),
        (r"/call2", call2),
        (r"/call3", call3),
        (r'/static/(.*)', tornado.web.StaticFileHandler,  {'path': static_path_dir} ),
        (r"/", MainHandler1),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    logging.basicConfig(level=logging.DEBUG)
    logging.info("main started")
    tornado.ioloop.IOLoop.current().start()
