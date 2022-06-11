from http import server

server = server.HTTPServer(('0.0.0.0', 8080), server.SimpleHTTPRequestHandler)
server.serve_forever()
