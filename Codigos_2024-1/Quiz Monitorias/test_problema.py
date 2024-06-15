import unittest
from problema import es_primo
from problema import organizar_lista
from problema import entero_a_binario
from problema import convertir_tiempos
from problema import conjetura_collatz
from problema import factorial
from problema import fibonacci
from problema import multiplicacion
from problema import potencia
from problema import numero_perfecto
from problema import numero_narcisista
from problema import verificar_datos_txt


class TestEsPrimo(unittest.TestCase):
    def test_primo(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(5))
        self.assertTrue(es_primo(7))
        self.assertTrue(es_primo(11))
    
    def test_no_primo(self):
        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(6))
        self.assertFalse(es_primo(8))
        self.assertFalse(es_primo(9))
        self.assertFalse(es_primo(10))
    
    def test_limites(self):
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(-1))
        self.assertFalse(es_primo(-10))
class TestOrganizarLista(unittest.TestCase):
    def test_organizar_lista(self):
        self.assertEqual(organizar_lista([1, 3, 2, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(organizar_lista([1, 3, 2, 4, 5, 0]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(organizar_lista([1, 3, 2, 4, 5, 0, -1]), [-1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(organizar_lista([1, 3, 2, 4, 5, 0, -1, -5]), [-5, -1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(organizar_lista([1, 5, 2, 4, 3, 0, -1, -5, -10]), [-10, -5, -1, 0, 1, 2, 3, 4, 5])
class TestEnteroABinario(unittest.TestCase):
    def test_entero_a_binario(self):
        self.assertEqual(entero_a_binario(0), '0')
        self.assertEqual(entero_a_binario(1), '1')
        self.assertEqual(entero_a_binario(2), '10')
        self.assertEqual(entero_a_binario(3), '11')
        self.assertEqual(entero_a_binario(4), '100')
        self.assertEqual(entero_a_binario(5), '101')
        self.assertEqual(entero_a_binario(6), '110')
        self.assertEqual(entero_a_binario(7), '111')
        self.assertEqual(entero_a_binario(8), '1000')
        self.assertEqual(entero_a_binario(9), '1001')
        self.assertEqual(entero_a_binario(10), '1010')    
class TestConvertirTiempos(unittest.TestCase):
    def test_convertir_tiempos(self):
        self.assertEqual(convertir_tiempos(1, 1, 1), (1, 1, 1))
        self.assertEqual(convertir_tiempos(1, 1, 60), (1, 2, 0))
        self.assertEqual(convertir_tiempos(1, 60, 60), (2, 1, 0))
        self.assertEqual(convertir_tiempos(24, 0, 0), (24, 0, 0))
        self.assertEqual(convertir_tiempos(24, 0, 1), (24, 0, 1))
        self.assertEqual(convertir_tiempos(24, 1, 0), (24, 1, 0))
        self.assertEqual(convertir_tiempos(24, 1, 1), (24, 1, 1))
        self.assertEqual(convertir_tiempos(24, 60, 60), (25, 1, 0))
        self.assertEqual(convertir_tiempos(24, 60, 59), (25, 0, 59))
class TestConjeturaCollatz(unittest.TestCase):
    def test_conjetura_collatz(self):
        self.assertEqual(conjetura_collatz(1), [1])
        self.assertEqual(conjetura_collatz(2), [2,1])
        self.assertEqual(conjetura_collatz(3), [3,10,5,16,8,4,2,1])
        self.assertEqual(conjetura_collatz(4), [4,2,1])
        self.assertEqual(conjetura_collatz(5), [5,16,8,4,2,1])
        self.assertEqual(conjetura_collatz(6), [6,3,10,5,16,8,4,2,1])
class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(3), [0, 1, 1])
        self.assertEqual(fibonacci(4), [0, 1, 1, 2])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(6), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])  
class TestMultiplicacion(unittest.TestCase):
    def test_Multiplicacion(self):
        self.assertEqual(multiplicacion(2,5),10)
        self.assertEqual(multiplicacion(3,4),12)
        self.assertEqual(multiplicacion(5,6),30)
        self.assertEqual(multiplicacion(7,8),56)
        self.assertEqual(multiplicacion(9,10),90)
class TestPotencia(unittest.TestCase):
    def test_potencia(self):
        self.assertEqual(potencia(2,5),32)
        self.assertEqual(potencia(3,4),81)
        self.assertEqual(potencia(5,6),15625)
        self.assertEqual(potencia(7,8),5764801)
        self.assertEqual(potencia(9,10),3486784401)
class TestNumeroPerfecto(unittest.TestCase):
    def test_perfecto(self):
        self.assertTrue(numero_perfecto(6))
        self.assertTrue(numero_perfecto(28))
        self.assertTrue(numero_perfecto(496))
        self.assertTrue(numero_perfecto(8128))

class TestNumeroNarcisista(unittest.TestCase):
    def test_narcista(self):
        self.assertTrue(numero_narcisista(153))
        self.assertTrue(numero_narcisista(370))
        self.assertTrue(numero_narcisista(371))
        self.assertTrue(numero_narcisista(407))
        self.assertTrue(numero_narcisista(1634))
        self.assertTrue(numero_narcisista(8208))
class TestDatosArchivoTXT(unittest.TestCase):
    def test_datos_txt(self):
        self.assertTrue(verificar_datos_txt(fr"datos.txt","python"))
        self.assertTrue(verificar_datos_txt(fr"datos.txt","java"))
        self.assertTrue(verificar_datos_txt(fr"datos.txt","c++"))
        self.assertTrue(verificar_datos_txt(fr"datos.txt","php"))
        self.assertTrue(verificar_datos_txt(fr"datos.txt","ruby"))
        
        
if __name__ == '__main__':
    unittest.main()
