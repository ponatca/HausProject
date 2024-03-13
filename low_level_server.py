import json
import socket

class DataStoreServer:
    def __init__(self, host='localhost', port=9999):
        self.host = host
        self.port = port
        self.data = {}
        self.transactions = {}

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print(f"Server listening on {self.host}:{self.port}")

            while True:
                conn, addr = server_socket.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        command = data.decode('utf-8').strip()
                        response = self.handle_command(command)
                        conn.sendall(response.encode('utf-8'))

    def handle_command(self, command):
        parts = command.split(' ')
        cmd = parts[0]

        if cmd == 'START':
            self.start_transaction()
            return '{"status":"Ok"}'
        elif cmd == 'COMMIT':
            self.commit_transaction()
            return '{"status":"Ok"}'
        elif cmd == 'ROLLBACK':
            self.rollback_transaction()
            return '{"status":"Ok"}'
        elif cmd == 'PUT':
            key, value = parts[1], ' '.join(parts[2:])
            self.transactions[key] = value
            return '{"status":"Ok"}'
        elif cmd == 'GET':
            key = parts[1]
            value = self.get_value(key)
            if value is None:
                return '{"status":"Error", "mesg":"Key not found"}'
            else:
                return json.dumps({"status":"Ok", "result":value})
        elif cmd == 'DEL':
            key = parts[1]
            if key in self.transactions:
                del self.transactions[key]
            return '{"status":"Ok"}'
        else:
            return '{"status":"Error", "mesg":"Invalid command"}'

    def start_transaction(self):
        self.transactions = self.data.copy()

    def commit_transaction(self):
        self.data = self.transactions.copy()
        self.transactions.clear()

    def rollback_transaction(self):
        self.transactions.clear()

    def get_value(self, key):
        if key in self.transactions:
            return self.transactions[key]
        elif key in self.data:
            return self.data[key]
        else:
            return None

if __name__ == "__main__":
    server = DataStoreServer()
    server.run()
