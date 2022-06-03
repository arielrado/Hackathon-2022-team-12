from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import socketserver
import time
import unlock
# use python 3 only

host_name = '10.176.94.30'
host_port = 9000


def read_html_template(path):
    #function to read HTML file
    try:
        with open(path) as f:
            file = f.read()
    except Exception as e:
        file = e
    return file


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        valid = unlock.main(self.path[1:])
        if valid:
            self.send_response(200, 'OK')
        else:
            self.send_error(404)
        if valid:
            file = read_html_template('./success.html')
            self.end_headers()
            self.wfile.write(bytes(file, 'utf-8'))
        else:
            file = read_html_template('./fail.html')
            self.end_headers()
            self.wfile.write(bytes(file, 'utf-8'))


myServer = HTTPServer((host_name, host_port), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (host_name, host_port))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (host_name, host_port))
