import random
class Emisor:
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.mensajeBinario = ''

    def aplicacion(self):
        return self.mensaje

    def verificacion(self):
        mensaje = self.mensaje
        self.mensajeBinario = (' '.join(format(ord(x), 'b') for x in mensaje)).replace(' ','')
        return self.mensajeBinario

    # cambiar bit
    def ruido(self):
        probabilidadCambiarBit = random.randint(0,99)

        # Probabilidad 1 en 100
        if (probabilidadCambiarBit == 5):
            bitACambiar = random.randint(0, len(self.mensajeBinario))

            mensajeEnLista = list(self.mensajeBinario)

            reemplazo = '1' if mensajeEnLista[bitACambiar] == '0' else '0'

            mensajeEnLista[bitACambiar] = reemplazo

        return self.mensajeBinario
    
    def paridadSimple(self):
        cantUnos = self.mensajeBinario.count('1')
        if cantUnos % 2 == 0:
            # cantUnos = cantUnos + "0"
            self.mensajeBinario += '0'
            """ return False   """
        else:
            # cantUnos = cantUnos + "1"
            self.mensajeBinario += '1'
            """ return True """

    def findChecksum(self):
        # Dividing sent message in packets of k bits.
        SentMessage = self.mensajeBinario
        k = 8
        c1 = SentMessage[0:k]
        c2 = SentMessage[k:2*k]
        c3 = SentMessage[2*k:3*k]
        c4 = SentMessage[3*k:4*k]
    
        # Calculating the binary sum of packets
        Sum = bin(int(c1, 2)+int(c2, 2)+int(c3, 2)+int(c4, 2))[2:]
    
        # Adding the overflow bits
        if(len(Sum) > k):
            x = len(Sum)-k
            Sum = bin(int(Sum[0:x], 2)+int(Sum[x:], 2))[2:]
        if(len(Sum) < k):
            Sum = '0'*(k-len(Sum))+Sum
    
        # Calculating the complement of sum
        Checksum = ''
        for i in Sum:
            if(i == '1'):
                Checksum += '0'
            else:
                Checksum += '1'
        self.mensajeBinario = Checksum + SentMessage

    # bit pariedad, checksum -> hay que enviarla tambien
    def transmision(self, c):

        sendData = str(self.mensajeBinario)
        c.send(sendData.encode())
