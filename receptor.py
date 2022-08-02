import socket
from bitarray import bitarray

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432    # The port used by the server
class Receptor:
    def __init__(self):
        pass
    # Imprimir mensaje, resultado
    def aplicacion(self):
        return self.mensaje

    # Aplicar algoritmos de deteccion de errores y de correcion
    def verificacion(self):
        
        self.checkReceiverChecksum(self.mensaje)
        # if self.paridadSimple():
        #     print("Mensaje viene bien")
        # else:
        #     print("Mensaje vino mal")

    # deserealizar el mensaje
    def codificacion(self, data):
        self.mensaje = bitarray(str(data.decode()))
        receptor.verificacion()

    # volver a calcular el checksum o bit pariedad para ver si esta bien
    def transmision(self):
        pass

    def checkReceiverChecksum(self, ReceivedMessage):
   
        k = 8
        # Dividing sent message in packets of k bits.
        ReceivedMessage = ReceivedMessage.to01()
        Checksum = ReceivedMessage[0:k]
        c1 = ReceivedMessage[k:2*k]
        c2 = ReceivedMessage[2*k:3*k]
        c3 = ReceivedMessage[3*k:4*k]
        c4 = ReceivedMessage[4*k:5*k]

        # Calculating the binary sum of packets + checksum
        ReceiverSum = bin(int(c1, 2)+int(c2, 2)+int(Checksum, 2) +
                        int(c3, 2)+int(c4, 2)+int(Checksum, 2))[2:]
    
        # Adding the overflow bits
        if(len(ReceiverSum) > k):
            x = len(ReceiverSum)-k
            ReceiverSum = bin(int(ReceiverSum[0:x], 2)+int(ReceiverSum[x:], 2))[2:]
    
        # Calculating the complement of sum
        ReceiverChecksum = ''
        for i in ReceiverSum:
            if(i == '1'):
                ReceiverChecksum += '0'
            else:
                ReceiverChecksum += '1'

        finalsum=bin(int(Checksum,2)+int(ReceiverChecksum,2))[2:]

        # Finding the sum of checksum and received checksum
        finalcomp=''
        for i in finalsum:
            if(i == '1'):
                finalcomp += '0'
            else:
                finalcomp += '1'
        
        # If sum = 0, No error is detected
        if(int(finalcomp,2) == 0):
            print("STATUS: ACCEPTED")
            
        # Otherwise, Error is detected
        else:
            print("STATUS: ERROR DETECTED")

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
        data = s.recv(65432)
        receptor = Receptor()
        receptor.codificacion(data)