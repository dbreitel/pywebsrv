import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
SPORT=os.getenv('LPORT')
LPORT=int(SPORT)
print (LPORT)
server_object = HTTPServer(server_address=('', LPORT), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()
