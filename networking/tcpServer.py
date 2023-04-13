import socket

def Main():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    client, addr = s.accept()
    print(f"Connection from: {addr}")
    while True:
        data = client.recv(1024).decode("utf-8")
        if not (data):
            break
        print(f"From connected user: {data}")
        data = data.upper()
        print(f"Sending: {data}")
        client.send(data.encode("utf-8"))

    client.close()

if __name__ == "__main__":
    Main()
        
      