import socket
from bitarray import bitarray
import json

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
        self.mensaje = bitarray(str(data))
        receptor.verificacion()

    # volver a calcular el checksum o bit pariedad para ver si esta bien
    def transmision(self):
        pass

    def checkReceiverChecksum(self, mensajeRecibido):
   
        split = 8
        
        mensajeRecibido = mensajeRecibido.to01()
        Checksum = int(mensajeRecibido[0 : split], 2)
        bloque1 = int(mensajeRecibido[split : 2 * split], 2)
        bloque2 = int(mensajeRecibido[2 * split : 3 * split], 2)
        bloque3 = int(mensajeRecibido[3 * split : 4 * split], 2)
        bloque4 = int(mensajeRecibido[4 * split : 5 * split], 2)

        # bloques + checksum
        sumaDeBloques = bin(bloque1 + bloque2 + Checksum + bloque3 + bloque4 + Checksum )[2:]
    
        # Si hay bits de mas se agregan a la suma
        if(len(sumaDeBloques) > split):
            x = len(sumaDeBloques)-split
            sumaDeBloques = bin(int(sumaDeBloques[0:x], 2)+int(sumaDeBloques[x:], 2))[2:]
    
        checkSumR = ''
        for i in sumaDeBloques:
            if(i == '1'):
                checkSumR += '0'
            else:
                checkSumR += '1'

        sumaFinal=bin(Checksum + int(checkSumR,2))[2:]

        # Hacemos string porque si fuera int, se sumarian los valores y no la representacion bits
        complemento = ''
        for i in sumaFinal:
            if(int(i) == 0):
                complemento += '1'
            else:
                complemento += '0'
        
        # Si la suma no es cero, el error no fue detectado
        if(int(complemento,2) == 0):
            print("Mensaje viene bien")
        else:
            print("Mensaje vino mal")

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

    def detectHammingError(self, arr, nr):
        n = len(arr)
        res = 0
    
        # Calculate parity bits again
        for i in range(nr):
            val = 0
            for j in range(1, n + 1):
                if(j & (2**i) == (2**i)):
                    val = val ^ int(arr[-1 * j])
    
            # Create a binary no by appending
            # parity bits together.
    
            res = res + val*(10**i)
    
        # Convert binary to decimal
        return int(str(res), 2)

        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        data = s.recv(65432).decode("utf-8")
        receptor = Receptor()
        print("DATA", data)
        if "rValue" in data:
            dataSerialized = json.loads(data)
            arr = dataSerialized.get("message")
            r = dataSerialized.get("rValue")
            correction = receptor.detectHammingError(arr, r)
            if(correction==0):
                print("There is no error in the received message.")
            else:
                print("The position of error is ",len(arr)-correction+1,"from the left")
        else:
            receptor.codificacion(data)