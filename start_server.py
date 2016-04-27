
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
#from ssl import *

#change this to your app
from my_app import app

#ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#ssl_ctx.load_cert_chain("/var/www/cert/domain.crt", "/var/www/cert/domain.key")

http_server = HTTPServer(WSGIContainer(app),ssl_options={
        "certfile": "/var/www/cert/domain.crt",
        "keyfile": "/var/www/cert/domain.key",
    })
http_server.listen(443)
IOLoop.instance().start()
