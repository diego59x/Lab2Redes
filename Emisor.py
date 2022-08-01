import random
class Emisor:
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.mensajeBinario = ''

    def aplicacion(self):
        return self.mensaje

    def verificacion(self):
        mensaje = self.mensaje
        self.mensajeBinario = ' '.join(format(ord(x), 'b') for x in mensaje)
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

    # bit pariedad, checksum -> hay que enviarla tambien
    def transmision(self, c):

        sendData = str(self.mensajeBinario)
        c.send(sendData.encode())
