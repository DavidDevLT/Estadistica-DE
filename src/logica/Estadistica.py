from math import sqrt

class ExceptionDatos(Exception):
    pass


class Estadistica:
    def __init__(self, numeros):
        self._numeros = self.validarNumeros(numeros)

    def validarNumeros(self, numeros):
        if numeros is not None:
            for num in numeros:
                if not isinstance(num, int) and not isinstance(num, float):
                    raise ValueError
                return numeros
        else:
            raise ExceptionDatos

    @property
    def numeros(self):
        return self._numeros

    @numeros.setter
    def numeros(self, numeros):
        try:
            self._numeros = self.validarNumeros(numeros)
        except ValueError as e:
            self._numeros = []

    def desviacion_estandar(self):
        media = self.calcular_media()
        suma = 0
        for valor in self.__numeros:
            suma += (valor - media) ** 2
        radicando = suma / (len(self.__numeros) - 1)
        return sqrt(radicando)

    def media(self):
        if self._numeros is None:
            raise ExceptionDatos
        if not self._numeros:
            raise ExceptionDatos
        numeros_validos = [num for num in self._numeros if isinstance(num, (int, float))]
        if not numeros_validos:
            raise ExceptionDatos
        return sum(numeros_validos) / len(numeros_validos)


if __name__ == "__main__":
    try:
        datos = [7, 3, 13, 17, 10, 8, 12, 9]
        estadistica = Estadistica(datos)
        print(estadistica.numeros)
        estadistica.numeros = [7, 3, 13]
        print(estadistica.numeros)
        print(estadistica.desviacion_estandar())
    except ExceptionDatos:
        print("Sin datos")