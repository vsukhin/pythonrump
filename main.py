import http.server
import socketserver

def http_server():
    PORT = 3000
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("Python is serving at port", PORT)
    httpd.serve_forever()
    
if __name__ == '__main__':
    http_server()
