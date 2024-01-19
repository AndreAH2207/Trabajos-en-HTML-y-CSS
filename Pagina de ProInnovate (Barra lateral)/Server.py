from http.server import BaseHTTPRequestHandler, HTTPServer
import time

#http://localhost:8080
#http://dominio.com => 80
#https://dominio.com => 443

hostName = "localhost"
portNumber = 8080

class AppServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "index.html")
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>Proyectos Financiados ProInnovate</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>App Runing...</body></html>", "utf-8"))

webServer = HTTPServer((hostName, portNumber), AppServer)
print("Server started...")

try:
    webServer.serve_forever()
except:
    pass

webServer.server_close()
print("Server stopped.")

