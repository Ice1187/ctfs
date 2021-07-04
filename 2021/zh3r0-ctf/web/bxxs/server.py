import json
import http.server as SimpleHTTPServer
import socketserver as SocketServer
import logging

PORT = 13337 

class GetHandler(
        SimpleHTTPServer.SimpleHTTPRequestHandler
        ):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print(f'[GET] {self.path}\n')
        print(f'{self.headers}\n')
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):
        print(f'[POST] {self.path}\n')
        print(f'{self.headers}\n')
        content_len = int(self.headers['Content-Length'])
        print(content_len)
        post_data = self.rfile.read(content_len)
        print(json.dumps(json.loads(post_data.decode('utf-8')), indent=2))
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()
