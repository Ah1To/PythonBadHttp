from http.server import HTTPServer, CGIHTTPRequestHandler



host = 'localhost'
port = 8080
httpd = HTTPServer((host, port), CGIHTTPRequestHandler)
httpd.serve_forever()
