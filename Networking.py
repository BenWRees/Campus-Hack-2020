
import socket
"""
	class that deals with network communication with the java service 
"""


class Python_Network:
    def __init__(self):
        pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind(('127.0.0.1', 50500))
    s.listen(1)
    while True:
        conn, addr = s.accept()
    with conn:
        print('Connected by ', adrr)
        while True:
            filename = "data.csv"
            file = open(filename, 'wb')
            data = conn.recv(1024)
            file.write(data)
            file.close()
            print("file has been received")
            if not data:
                break
