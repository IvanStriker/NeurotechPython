from http.server import HTTPServer

from LaboratoryWork9.src import data
from LaboratoryWork9.src.requests_handler import SimpleHTTPRequestHandler

if __name__ == "__main__":
    """
    Entry point
    """
    data.load_data()
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()