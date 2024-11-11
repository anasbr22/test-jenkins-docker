import http.server
import socketserver
import urllib.parse

PORT = 5000

class CalculatorHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Extraire les paramètres de l'URL
        query_params = urllib.parse.parse_qs(urllib.parse.urlsplit(self.path).query)
        if 'operation' in query_params:
            operation = query_params['operation'][0]
            try:
                num1 = float(query_params['num1'][0])
                num2 = float(query_params['num2'][0])

                result = None
                if operation == 'add':
                    result = num1 + num2
                elif operation == 'subtract':
                    result = num1 - num2
                elif operation == 'multiply':
                    result = num1 * num2
                elif operation == 'divide':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        result = "Error: Division by zero"

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f"Result: {result}".encode())
            except ValueError:
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Error: Invalid input")
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Error: Missing parameters")

# Configuration du serveur
def run_server():
    with socketserver.TCPServer(("", PORT), CalculatorHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    run_server()
