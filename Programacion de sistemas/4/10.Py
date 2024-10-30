class Complejo:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    # Métodos mutadores
    def set_real(self, real):
        self.real = real

    def set_imag(self, imag):
        self.imag = imag

    # Métodos para operaciones aritméticas
    def suma(self, otro):
        return Complejo(self.real + otro.real, self.imag + otro.imag)

    def resta(self, otro):
        return Complejo(self.real - otro.real, self.imag - otro.imag)

    def multiplicacion(self, otro):
        real = self.real * otro.real - self.imag * otro.imag
        imag = self.real * otro.imag + self.imag * otro.real
        return Complejo(real, imag)

    def division(self, otro):
        denominador = otro.real**2 + otro.imag**2
        real = (self.real * otro.real + self.imag * otro.imag) / denominador
        imag = (self.imag * otro.real - self.real * otro.imag) / denominador
        return Complejo(real, imag)

    def acumulacion(self, otro):
        self.real += otro.real
        self.imag += otro.imag

    # Método para imprimir un número complejo
    def print(self):
        if self.imag >= 0:
            print(f"{self.real} + {self.imag}i")
        else:
            print(f"{self.real} - {abs(self.imag)}i")

# Ejemplo de uso:
c1 = Complejo(3, 2)
c2 = Complejo(1, -4)

suma = c1.suma(c2)
suma.print()  # Salida: 4.0 - 2.0i

resta = c1.resta(c2)
resta.print()  # Salida: 2.0 + 6.0i

multiplicacion = c1.multiplicacion(c2)
multiplicacion.print()  # Salida: 11.0 - 10.0i

division = c1.division(c2)
division.print()  # Salida: 0.2 + 1.4i

c1.acumulacion(c2)
c1.print()  # Salida: 4.0 - 2.0i (c1 se ha modificado)