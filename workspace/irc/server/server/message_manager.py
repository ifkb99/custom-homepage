import socketserver as ss

class IRCServer(ss.StreamRequestHandler):

    def load_messages(self, num_messages):

    def store_message(self, message):

    def send_message(self, message):

    def handle(self):
        # self.request is TCP socket connected to client
        self.data = self.rfile.readline().strip()
        print('{}:'.format(self.client_address[0]))
        print(self.data)
        # send back data in upper case
        self.wfile.write(self.data.upper())

if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999

    # create server at localhost on port
    with ss.TCPServer((HOST, PORT), IRCServer) as server:
        # will keep running until interrupted
        server.serve_forever()