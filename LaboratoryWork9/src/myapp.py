from http.server import HTTPServer

from requests_handler import SimpleHTTPRequestHandler
import data


if __name__ == "__main__":
    data.load_data()
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()