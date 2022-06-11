from http import server
print('fff')
server = server.HTTPServer(('0.0.0.0', 8080), server.SimpleHTTPRequestHandler)
server.serve_forever()
