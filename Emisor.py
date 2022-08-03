import random
import sys
import json
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
        print("MENSAJE SIN RUIDO", self.mensajeBinario)

        # Probabilidad 1 en 100
        if (probabilidadCambiarBit < 99):
            bitACambiar = random.randint(0, len(self.mensajeBinario))

            reemplazo = '1' if self.mensajeBinario[bitACambiar] == '0' else '0'
            self.mensajeBinario = self.mensajeBinario[:bitACambiar] + \
                reemplazo + \
                self.mensajeBinario[bitACambiar + 1:]
            
        print("MENSAJE CON RUIDO", self.mensajeBinario)
        return self.mensajeBinario
    
    def paridadSimple(self):
        cantUnos = self.mensajeBinario.count('1')
        if cantUnos % 2 == 0:
            self.mensajeBinario += '0'
        else:
            self.mensajeBinario += '1'

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
    def transmision(self, c, isHamming = False):

        if isHamming:
            m = {"rValue": self.r, "message": self.mensajeBinario}
            data = json.dumps(m)
            c.sendall(bytes(data,encoding="utf-8"))
        else:
            sendData = str(self.mensajeBinario)
            c.send(sendData.encode())


    def calcRedundantBits(self, m):
 
        # Use the formula 2 ^ r >= m + r + 1
        # to calculate the no of redundant bits.
        # Iterate over 0 .. m and return the value
        # that satisfies the equation
    
        for i in range(m):
            if(2**i >= m + i + 1):
                return i
 
    def posRedundantBits(self, data, r):
    
        # Redundancy bits are placed at the positions
        # which correspond to the power of 2.
        j = 0
        k = 1
        m = len(data)
        res = ''
    
        # If position is power of 2 then insert '0'
        # Else append the data
        for i in range(1, m + r+1):
            if(i == 2**j):
                res = res + '0'
                j += 1
            else:
                res = res + data[-1 * k]
                k += 1
    
        # The result is reversed since positions are
        # counted backwards. (m + r+1 ... 1)
        return res[::-1]
    
    
    def calcParityBits(self, arr, r):
        n = len(arr)
    
        # For finding rth parity bit, iterate over
        # 0 to r - 1
        for i in range(r):
            val = 0
            for j in range(1, n + 1):
    
                # If position has 1 in ith significant
                # position then Bitwise OR the array value
                # to find parity bit value.
                if(j & (2**i) == (2**i)):
                    val = val ^ int(arr[-1 * j])
                    # -1 * j is given since array is reversed
    
            # String Concatenation
            # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
            arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
        return arr

    def hamming(self):
        # Se agrega el conjunto de bits "overhead" y se asigna a self.mensajeBinario
        # para ser pasado a la funcion de transmision.
        data = self.mensajeBinario
        m = len(data)
        r = self.calcRedundantBits(m)
        self.r = r
        arr = self.posRedundantBits(data, r)
        self.mensajeBinario = self.calcParityBits(arr, r)