import math

class Rectangulo:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        """
        Constructor que crea un rectángulo a partir de sus cuatro vértices.

        Args:
            x1 (int, optional): Coordenada x del vértice inferior izquierdo. Defaults to 0.
            y1 (int, optional): Coordenada y del vértice inferior izquierdo. Defaults to 0.
            x2 (int, optional): Coordenada x del vértice superior derecho. Defaults to 0.
            y2 (int, optional): Coordenada y del vértice superior derecho. Defaults to 0.
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @classmethod
    def from_base_altura(cls, base, altura):
        """
        Constructor que crea un rectángulo a partir de su base y altura.

        Args:
            base (int): Base del rectángulo.
            altura (int): Altura del rectángulo.

        Returns:
            Rectangulo: Un nuevo objeto Rectangulo.
        """
        return cls(0, 0, base, altura)

    def calcular_superficie(self):
        """Calcula la superficie del rectángulo.

        Returns:
            int: La superficie del rectángulo.
        """
        base = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)
        return base * altura

    def desplazar(self, dx, dy):
        """Desplaza el rectángulo en el plano.

        Args:
            dx (int): Desplazamiento en el eje x.
            dy (int): Desplazamiento en el eje y.
        """
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

# Ejemplo de uso:
# Crear un rectángulo a partir de sus vértices
rectangulo1 = Rectangulo(1, 2, 5, 4)

# Crear un rectángulo a partir de su base y altura
rectangulo2 = Rectangulo.from_base_altura(3, 2)

print("Superficie del rectángulo 1:", rectangulo1.calcular_superficie())
print("Superficie del rectángulo 2:", rectangulo2.calcular_superficie())

# Desplazar el rectángulo 1
rectangulo1.desplazar(2, -1)
print("Nuevo vértice inferior izquierdo del rectángulo 1:", rectangulo1.x1, rectangulo1.y1)