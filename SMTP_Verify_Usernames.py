import socket

smtp_server_address = input("Enter your server IP :")
file_path = input("Enter your username list name :")


def send_vrfy_command(address, port, username):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((address, port))
    response = client_socket.recv(1024)
    client_socket.send("VRFY {} \r\n".format(username).encode())
    response = client_socket.recv(1024)
    client_socket.close()

    if "unknown" in str(response):
        pass
    else:
        print("User {} is recorded!".format(username))
     


def verify_users_from_file(address, port, file_path):
    try:
        with open(file_path, "r") as file:
            usernames = file.read().splitlines()

        for username in usernames:
            send_vrfy_command(address, port, username)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))





smtp_server_port = 25
verify_users_from_file(smtp_server_address, smtp_server_port, file_path)
