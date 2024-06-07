import unittest
import proyecto
class MyTestCase(unittest.TestCase):
    def test_coloreo(self):
        # Prueba 1
        graph = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        colors, current_color = proyecto.coloreo(graph)
        result = proyecto.generar_matrix(colors, current_color)
        
        expected_result = [[1, 1, 1, 1]]
        self.assertEqual(result, expected_result)

        # Prueba 2
        graph = [[0, 1, 1, 1, 1],
                 [1, 0, 1, 1, 1],
                 [1, 1, 0, 1, 1],
                 [1, 1, 1, 0, 1],
                 [1, 1, 1, 1, 0]]
        
        
        colors, current_color = proyecto.coloreo(graph)
        result = proyecto.generar_matrix(colors, current_color)
        
        expected_result = [[1, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0],
                           [0, 0, 1, 0, 0],
                           [0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 1]]        
        self.assertEqual(result, expected_result)
    def test_coloreo2(self):
        # Prueba 3
        """
0, 1, 0, 1, 0, 1, 0, 1, 1, 1
1, 0, 1, 0, 0, 0, 0, 0, 0, 0
0, 1, 0, 0, 0, 0, 0, 0, 0, 0
1, 0, 0, 0, 0, 0, 0, 0, 0, 0
0, 0, 0, 0, 0, 0, 0, 0, 0, 0
1, 0, 0, 0, 0, 0, 0, 0, 0, 0
0, 0, 0, 0, 0, 0, 0, 0, 0, 0
1, 0, 0, 0, 0, 0, 0, 0, 0, 0
1, 0, 0, 0, 0, 0, 0, 0, 0, 0
1, 0, 0, 0, 0, 0, 0, 0, 0, 0
        
        
        
        """
        
        
        grafo = [[0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        colors, current_color = proyecto.coloreo(grafo)
        result = proyecto.generar_matrix(colors, current_color)
        
        expected_result = [[1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                           [0, 1, 0, 1, 0, 1, 0, 1, 1, 1]]        
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()