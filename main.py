from multiprocessing.spawn import old_main_modules

from Emisor import *

from multiprocessing.spawn import old_main_modules

# binario, checksum, probabilidad para agregar ruido


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 12345  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket()
s.bind(('', PORT))
s.listen(5)
c, addr = socket.accept()
print("Socket Up and running with a connection from", addr)

mensaje = input("Escriba el mensaje que desea enviar: ")

emisor = Emisor(mensaje)
mensajeAEnviar = emisor.mensaje
emisor.verificacion()
emisor.transmision(c)