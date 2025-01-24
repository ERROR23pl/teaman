from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import ObslugaZapytania as OZ

class handlerZadan(BaseHTTPRequestHandler):

    def do_POST(self):
        dlugosc = int(self.headers['Content-Length'])
        zawartoscBitowa = self.rfile.read(dlugosc)
        daneJSON = json.loads(str(zawartoscBitowa,'utf-8'))
        odpowiedz = OZ.ObsluzZapytanie(daneJSON)
        self.send_response(200)
        self.end_headers()
        self.wfile.write((json.dumps(odpowiedz,ensure_ascii=False)).encode())


serwer = HTTPServer(('localhost',8000),handlerZadan)
serwer.serve_forever()