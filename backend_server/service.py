""" Backend service """

import operations
import pyjsonrpc

SERVER_HOST = 'localhost'
SERVER_PORT = 4040


class RequestHandler(pyjsonrpc.HttpRequestHandler):
    """ add twp numbers """
    @pyjsonrpc.rpcmethod
    def add(self, num1, num2):
        """ Test method """
        print "add is called with %d and %d" % (num1, num2)
        return num1 + num2

    """ Get news summaries for a user """
    @pyjsonrpc.rpcmethod
    def getStocksSummariesForUser(self, user_id, page_num):
        return operations.getStocksSummariesForUser(user_id, page_num)

# Threading HTTP Server
HTTP_SERVER = pyjsonrpc.ThreadingHttpServer(
    server_address=(SERVER_HOST, SERVER_PORT),
    RequestHandlerClass=RequestHandler
)

print "Starting HTTP server on %s:%d" % (SERVER_HOST, SERVER_PORT)

HTTP_SERVER.serve_forever()
