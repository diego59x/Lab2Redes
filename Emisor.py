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
        print(probabilidadCambiarBit)
        if (probabilidadCambiarBit < 50):
            bitACambiar = random.randint(0, len(self.mensajeBinario))

            reemplazo = '1' if self.mensajeBinario[bitACambiar] == '0' else '0'
            self.mensajeBinario = self.mensajeBinario[:bitACambiar] + \
                reemplazo + \
                self.mensajeBinario[bitACambiar + 1:]
            
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

    def calculateChecksum(self):
        
        mensaje = self.mensajeBinario
        split = 8
        bloque1 = int(mensaje[0 : split], 2)
        bloque2 = int(mensaje[split : 2 * split], 2)
        bloque3 = int(mensaje[2 * split : 3 * split], 2)
        bloque4 = int(mensaje[3 * split : 4 * split], 2)

        sumaBinaria = bin(bloque1 + bloque2 + bloque3 + bloque4)[2:]
    
        if(len(sumaBinaria) > split):
            x = len(sumaBinaria) - split
            sumaBinaria = bin(int(sumaBinaria[0:x], 2)+int(sumaBinaria[x:], 2))[2:]
        if(len(sumaBinaria) < split):
            sumaBinaria = '0' * (split-len(sumaBinaria))+sumaBinaria
    
        # Hacemos string porque si fuera int, se sumarian los valores y no la representacion bits
        Checksum = ''
        for i in sumaBinaria:
            if(int(i) == 0):
                Checksum += '1'
            else:
                Checksum += '0'
        self.mensajeBinario = Checksum + mensaje

    # bit pariedad, checksum -> hay que enviarla tambien
    def transmision(self, c):

        sendData = str(self.mensajeBinario)
        c.send(sendData.encode())
