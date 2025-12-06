from http.server import HTTPServer

from LaboratoryWork8.src.requests_handler import SimpleHTTPRequestHandler
import LaboratoryWork8.src.data as data


if __name__ == "__main__":
    """
    Entry point
    """
    data.load_data()
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()