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

        if self.paridadSimple():
            print("Mensaje viene bien")
        else:
            print("Mensaje vino mal")

    # traducir el mensaje de bits a ascii
    def codificacion(self):

        pass
    # volver a calcular el checksum o bit pariedad para ver si esta bien
    def transmision(self):
        pass

    def paridadSimple(self):
        mensaje_lista = self.mensaje.tolist()
        cantUnos = mensaje_lista[:-1].count(1)
        verificacion = None
        if cantUnos % 2 == 0:
            # cantUnos = cantUnos + "0"
            verificacion = 0
        else:
            # cantUnos = cantUnos + "1"
            verificacion = 1
        if (self.mensaje.tolist()[-1] == verificacion): 
            return True
        else:
            return False

        


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        data = s.recv(65432).decode() # esto va en codificacion
        receptor = Receptor(data)
        receptor.verificacion()
