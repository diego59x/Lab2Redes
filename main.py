from multiprocessing.spawn import old_main_modules

from Emisor import *
import socket
from multiprocessing.spawn import old_main_modules

# binario, checksum, probabilidad para agregar ruido


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432    # Port to listen on (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print("Socket Up and running with a connection from", addr)
        while True:
            print("Opciones 1. Enviar mensaje 2. Salir")
            opcion = input()
            if (opcion == "1"):
                mensaje = input("Escriba el mensaje que desea enviar: ")
                emisor = Emisor(mensaje)
                emisor.verificacion()
                # emisor.paridadSimple()

                # emisor.hamming()
                emisor.ruido()
                emisor.calculateChecksum()

                # emisor.transmision(conn, isHamming = True) # para hamming
                emisor.transmision(conn) # para el resto de algoritmos
            else:
                conn.close()

