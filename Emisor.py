import socket

class Emisor:
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.mensajeBinario = ''

    def aplicacion(self):
        return self.mensaje

    def verificacion(self):
        mensaje = self.mensaje
        self.mensajeBinario = ' '.join(format(ord(x), 'b') for x in mensaje)
        print(self.mensajeBinario)
        return self.mensajeBinario

    def ruido(self):
        return self.mensajeBinario

    def transmision(self, c):

        sendData = self.mensajeBinario
        c.send(sendData.encode())
        if(sendData == "Bye" or sendData == "bye"):
            c.close()