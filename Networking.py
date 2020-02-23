
import socket
"""
	class that deals with network communication with the java service 
"""


class Python_Network:
    def __init__(self):
        pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print ('here1')
    host = socket.gethostname()
    print(host)
    s.bind((host, 25565))
    print ('here2')
    s.listen(1)
    print ('here3')
    while True:
        print ('here4')
        conn, addr = s.accept()
        print ('here5')
        print ('here6')
        filename = "data.csv"
        file = open(filename, 'wb')
        data = conn.recv(1024)
        file.write(data)
        file.close()
        print("file has been received")
        if not data:
            break
