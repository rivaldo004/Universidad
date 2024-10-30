class Nodo:
def __init__(self, valor):
self.valor = valor
self.izquierdo = None
self.derecho = None
class ArbolBinarioBusqueda:
def __init__(self):
self.raiz = None
def insertar(self, valor):
"""Inserta un valor en el árbol de búsqueda binario."""
if self.raiz is None:
self.raiz = Nodo(valor)
else:
self._insertar_recursivo(self.raiz, valor)
def _insertar_recursivo(self, nodo_actual, valor):
"""Inserta de manera recursiva en el subárbol correspondiente."""
if valor < nodo_actual.valor:
if nodo_actual.izquierdo is None:
nodo_actual.izquierdo = Nodo(valor)
else:
self._insertar_recursivo(nodo_actual.izquierdo, valor)
else:
if nodo_actual.derecho is None:
nodo_actual.derecho = Nodo(valor)
else:
self._insertar_recursivo(nodo_actual.derecho, valor)
def buscar(self, valor):
"""Busca un valor en el árbol de búsqueda binario."""
return self._buscar_recursivo(self.raiz, valor)
def _buscar_recursivo(self, nodo_actual, valor):
"""Busca recursivamente el valor en el árbol."""
if nodo_actual is None:
return False
if valor == nodo_actual.valor:
return True
elif valor < nodo_actual.valor:
return self._buscar_recursivo(nodo_actual.izquierdo, valor)
else:
return self._buscar_recursivo(nodo_actual.derecho, valor)
def inorden(self):
"""Realiza el recorrido inorden (izquierda-raíz-derecha) del árbol."""
self._inorden_recursivo(self.raiz)
def _inorden_recursivo(self, nodo_actual):
"""Recorre el árbol en inorden de manera recursiva."""
if nodo_actual is not None:
self._inorden_recursivo(nodo_actual.izquierdo)
print(nodo_actual.valor, end=" ")
self._inorden_recursivo(nodo_actual.derecho)
# Ejemplo de uso del Árbol Binario de Búsqueda
if __name__ == "__main__":
arbol = ArbolBinarioBusqueda()
# Insertamos valores en el árbol
valores = [50, 30, 70, 20, 40, 60, 80]
for valor in valores:
arbol.insertar(valor)
print("Recorrido inorden del árbol:")
arbol.inorden() # Debería imprimir: 20 30 40 50 60 70 80
# Buscar un valor en el árbol
print("\n\n¿El valor 40 está en el árbol?", arbol.buscar(40)) # True
print("¿El valor 90 está en el árbol?", arbol.buscar(90))