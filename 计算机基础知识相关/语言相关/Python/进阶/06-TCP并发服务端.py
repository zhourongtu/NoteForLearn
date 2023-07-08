import socketserver


class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        # todo: handle循环
        pass
        # ...
        

sk = socketserver.ThreadingTCPServer(('127.0.0.1', 45126), RequestHandler)
sk.serve_forever()





