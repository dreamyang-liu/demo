from http import server

server = server.HTTPServer(('localhost', 8080), server.SimpleHTTPRequestHandler)
server.serve_forever()