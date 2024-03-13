import socket

class DataStoreClient:
    def __init__(self, host='localhost', port=9999):
        self.host = host
        self.port = port

    def send_command(self, command):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(command.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            return response

if __name__ == "__main__":
    client = DataStoreClient()

    # Example command sequence
    commands = [
        "START",
        "GET most_popular_leader",
        "PUT georgew {\"first_name\":\"George\", \"last_name\":\"Washington\", \"role\":\"President\"}",
        "PUT winstonc {\"first_name\":\"Winston\", \"last_name\":\"Churchill\", \"role\":\"Prime Minister\"}",
        "COMMIT"
    ]

    for command in commands:
        response = client.send_command(command)
        print(f"Command: {command}\nResponse: {response}")
