#!/usr/bin/env python
from sys import stdout
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
        "webserver.py", "28/12/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import socket
import io
import sys
import os
import signal
import errno
from datetime import datetime


class WSGIServer(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1024

    def __init__(self, server_address):
        # Create a listening socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )

        # Allow reuse of same address
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind
        listen_socket.bind(server_address)
        # Activate
        listen_socket.listen(self.request_queue_size)
        # Get server host name and port
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        # Return headers set by Web Framework
        self.headers_set = []

    def set_app(self, application):
        self.application = application

    def grim_reaper(self, signum, frame):
        while True:
            try:
                pid, status = os.waitpid(
                    -1,          # Wait for any child process
                     os.WNOHANG  # Do not block and return EWOULDBLOCK error
                )
                print(
                    'Child {pid} terminated with status {status}'
                    '\n'.format(pid=pid, status=status)
                )
            except OSError:
                return

            if pid == 0:  # no more zombies
                return

    def serve_forever(self):
        listen_socket = self.listen_socket

        # Take care of zombie processes
        signal.signal(signal.SIGCHLD, self.grim_reaper)

        while True:
            try:
                # New Client connection
                self.client_connection, client_address = listen_socket.accept()
            except IOError as e:
                code, msg = e.args
                # restart 'accept' if it was interrupted
                if code == errno.EINTR:
                    continue
                else:
                    raise

            pid = os.fork()
            if pid == 0:    # Child
                listen_socket.close()
                self.handle_one_request()
                os._exit(0)
            else:
                self.client_connection.close()

    def handle_one_request(self):
        self.request_data = request_data = self.client_connection.recv(1024).decode()
        # Print out request data
        print(''.join(
            '< {line}\n'.format(line=line)
            for line in request_data.splitlines()
        ))

        if request_data=='':
            return
        self.parse_request(request_data)

        # Construct environment dictionary using request data
        env = self.get_environ()

        # Get back result for application
        result = self.application(env, self.start_response)

        self.finish_response(result)

    def parse_request(self, text):
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip('\r\n')
        # Break request into components
        (self.request_method,   # GET
        self.path,              # /hello
         self.request_version   # HTTP/1.1
         ) = request_line.split()

    def get_environ(self):
        env = {}

        # Required WSGI variables
        env['wsgi.version'] = (1, 0)
        env['wsgi.url_scheme'] = 'http'
        env['wsgi.input'] = io.StringIO(str(self.request_data))
        env['wsgi.errors'] = sys.stderr
        env['wsgi.multithread'] = False
        env['wsgi.multiprocess'] = False
        env['wsgi.run_once'] = False
        # Required CGI variables
        env['REQUEST_METHOD'] = self.request_method
        env['PATH_INFO'] = self.path
        env['SERVER_NAME'] = self.server_name
        env['SERVER_PORT'] = str(self.server_port)
        return env

    def start_response(self, status, response_headers, exc_info=None):
        # Add necessary server headers
        time_now = datetime.today()
        server_headers = [
            ('Date', time_now.strftime("%a, %d %b %Y %H:%M:%S %Z")),
            # ('Date', 'Tue, 31 Mar 2015 12:54:48 GMT'),
            ('Server', 'WSGIServer 0.2')
        ]

        self.headers_set = [status, response_headers + server_headers]
        # Should return self.finish_response

    def finish_response(self, result):
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'

            for data in result:
                response += data.decode('utf-8')
            # Print out request data
            print(''.join(
                '> {line}\n'.format(line=line)
                for line in response.splitlines()
            ))
            self.client_connection.sendall(bytes(response, 'utf-8'))
        finally:
            self.client_connection.close()

# SERVER_ADDRESS = (HOST, PORT) = socket.gethostname(), 8888
# SERVER_ADDRESS = (HOST, PORT) = socket.gethostname(), 80
# SERVER_ADDRESS = (HOST, PORT) = '192.168.1.80', 8888
SERVER_ADDRESS = (HOST, PORT) = '0.0.0.0', 8888


def make_server(server_address, application):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as module:callable')
    app_path = sys.argv[1]
    module, application = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(SERVER_ADDRESS, application)
    print("WSGIServer: Serving HTTP on port {port} ...\n".format(port=PORT))
    httpd.serve_forever()
