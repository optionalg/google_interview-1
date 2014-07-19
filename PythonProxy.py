import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import urlparse,urllib2

'''
Bypass cross domain ajax call constrain
http://localhost:8000/http://yahoo.com
'''

class MyHandler(SimpleHTTPRequestHandler):
   def do_GET(self):

       print self.headers
       # Parse query data & params to find out what was passed
       parsedParams = urlparse.urlparse(self.path)
       queryParsed = urlparse.parse_qs(parsedParams.query)

       # request is either for a file to be served up or our test
       #if parsedParams.path == "/test":
       self.processMyRequest(self.path.lstrip('/'))
       #else:
          # Default to serve up a local file 
          #SimpleHTTPRequestHandler.do_GET(self);
   def processMyRequest(self, url):
  
       print 'opening url:',url

       self.send_response(200)
       self.send_header('Content-Type', 'text/plain')
       self.send_header('Access-Control-Allow-Origin', '*')
       #self.send_header('Access-Control-Allow-Origin', 'http://localhost:8000/')
       #self.send_header('Access-Control-Allow-Origin', 'http://localhost/')
       self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
       self.send_header('Access-Control-Max-Age','1000')
       self.send_header('Access-Control-Allow-Headers', 'Content-Type')
       self.end_headers()

       self.wfile.write(urllib2.urlopen(url).read());
       self.wfile.close();

HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, MyHandler)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()
