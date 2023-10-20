import unittest

from src.logica.Estadistica import Estadistica, ExceptionDatos


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.estadistica = Estadistica([])

    def tearDown(self):
        self.estadistica = None

    def test_media_listaVacia_retornaExcepcion(self):
        # arrange
        self.estadistica.numeros = []

        # Assert
        with self.assertRaises(ExceptionDatos):
            self.estadistica.media()

    def test_media_unDato_retornaMedia(self):
        # arrange
        self.estadistica.numeros = [3.5, 8, -4.2]
        resultadoEsperado = 2.433
        # Do
        resultadoActual = self.estadistica.media()

        # Assert
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, 3)

    def test_media_noNumerico_retornaException(self):
        # arrange
        self.estadistica.numeros = ["a", "b", 1]

        # Assert
        with self.assertRaises(ExceptionDatos):
            self.estadistica.media()

    def test_media_nCasosNumeros_retornaMedia(self):
        # Arrange
        items = (
            {"Case": "Caso 01", "datos": [15.82], "media": 15.820, "desvstd": 0.000},
            {"Case": "Caso 02", "datos": [15.62, 15.9], "media": 15.760, "desvstd": 0.140},
            {"Case": "Caso 03", "datos": [15.62, 15.9, 14.5], "media": 15.340, "desvstd": 0.605},
            {"Case": "Caso 04", "datos": [15, 16.06, 15.14, -20, 17.25, 14.37, 14.28], "media": 10.300,
             "desvstd": 12.407},
            {"Case": "Caso 04", "datos": [0, 0, 0, 0, 0, 0, 0], "media": 0.000, "desvstd": 0.000},
            {"Case": "Caso 04", "datos": [-15, 16.06, 15.14, -20, -17.25, 14.37, 14.28], "media": 1.086,
             "desvstd": 16.088},
        )
        for item in items:
            with self.subTest(item["Case"]):
                self.estadistica.numeros = item["datos"]
            resultadoEsperado = item["media"]

            # Do
            resultadoActual = self.estadistica.media()

            # Assert
            self.assertAlmostEqual(resultadoActual, resultadoEsperado, places=3)

