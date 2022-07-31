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
        return self.mensajeBinario

    # bit pariedad, checksum -> hay que enviarla tambien
    def transmision(self, c):

        sendData = str(self.mensajeBinario)
        c.send(sendData.encode())
