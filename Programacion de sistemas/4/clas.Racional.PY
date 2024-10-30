class Racional:
    def __init__(self, numerador=0, denominador=1):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def leer(self):
        print("Ingrese el numerador: ")
        self.numerador = int(input())
        print("Ingrese el denominador: ")
        while True:
            denominador = int(input())
            if denominador == 0:
                print("El denominador no puede ser cero. Intente nuevamente.")
            else:
                self.denominador = denominador
                break
        self.simplificar()

    def simplificar(self):
        mcd = self.mcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def suma(self, otro):
        num = self.numerador * otro.denominador + self.denominador * otro.numerador
        den = self.denominador * otro.denominador
        return Racional(num, den)

    def resta(self, otro):
        num = self.numerador * otro.denominador - self.denominador * otro.numerador
        den = self.denominador * otro.denominador
        return Racional(num, den)

    def multiplicacion(self, otro):
        num = self.numerador * otro.numerador
        den = self.denominador * otro.denominador
        return Racional(num, den)

    def division(self, otro):
        if otro.numerador == 0:
            raise ValueError("No se puede dividir por cero")
        num = self.numerador * otro.denominador
        den = self.denominador * otro.numerador
        return Racional(num, den)

    def __lt__(self, otro):
        return self.numerador * otro.denominador < self.denominador * otro.numerador

    def __le__(self, otro):
        return self.numerador * otro.denominador <= self.denominador * otro.numerador

    def __gt__(self, otro):
        return self.numerador * otro.denominador > self.denominador * otro.numerador

    def __ge__(self, otro):
        return self.numerador * otro.denominador >= self.denominador * otro.numerador

    def __eq__(self, otro):
        return self.numerador * otro.denominador == self.denominador * otro.numerador

    def copia(self):
        return Racional(self.numerador, self.denominador)

    def __str__(self):
        if self.denominador == 1:
            return str(self.numerador)
        else:
            return str(self.numerador) + "/" + str(self.denominador)

# Ejemplo de uso:
frac1 = Racional(3, 4)
frac2 = Racional()  # Crea una fracción 0/1
frac2.leer()
print(frac1 + frac2)