import socket
from bitarray import bitarray

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432    # The port used by the server
class Receptor:
    def __init__(self, mensaje):
        self.mensaje = bitarray(str(mensaje))
    # Imprimir mensaje, resultado
    def aplicacion(self):
        return self.mensaje

    # Aplicar algoritmos de deteccion de errores y de correcion
    def verificacion(self):
        print(type(self.mensaje))
        # return self.mensaje

    # traducir el mensaje de bits a ascii
    def codificacion(self):

        pass
    # volver a calcular el checksum o bit pariedad para ver si esta bien
    def transmision(self):
        pass

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        data = s.recv(65432).decode()
        receptor = Receptor(data)
        receptor.verificacion()
