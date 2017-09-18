from http.server import BaseHTTPRequestHandler
import smtplib

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("cs2112autograder@gmail.com", "")

        msg = "Testing autograder"
        server.sendmail("cs2112autograder@gmail.com", "", msg)
        server.quit()
