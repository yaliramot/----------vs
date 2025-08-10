import socket

def send_file():
    try:
     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client_socket.connect((host, port))
     client_socket.sendall((file_name+ "\n").encode("utf-8"))
     with open(file_name, "rb") as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendall(data)

     print("File sent successfully.")
    except Exception as e:
        print("Error occurred:", str(e))
    finally:
     client_socket.close()

if __name__ == "__main__":
    host="127.0.0.1"  
    port=12345
    file_name = r"C://Users//yalir//OneDrive//Desktop//פרוייקטים vs//test.txt"
    send_file()  