
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from my_app import app

try:
    http_server = HTTPServer(WSGIContainer(app), ssl_options={
        "certfile": "/var/www/cert/domain.crt",
        "keyfile": "/var/www/cert/domain.key",
    })
    http_server.listen(443)

except ValueError:
    print "can't find certificate, starting on port 8080 instead"
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(8080)


IOLoop.instance().start()
