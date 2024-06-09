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
    def test_coloreo3(self):
        grafo = [[0, 1, 1, 1, 1],
                 [1, 0, 1, 1, 1],
                 [1, 1, 0, 1, 1],
                 [1, 1, 1, 0, 1],
                 [1, 1, 1, 1, 0]]
        colors, current_color = proyecto.coloreo(grafo)
        result = proyecto.generar_matrix(colors, current_color)
        
        expected_result =  [[1, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1]]
        self.assertEqual(result, expected_result)
    def test_coloreo4(self):
        grafo = [[0,1,0,1],
                 [1,0,1,0],
                 [0,1,0,0],
                 [1,0,0,0]]
        colors, current_color = proyecto.coloreo(grafo)
        result = proyecto.generar_matrix(colors, current_color)
        
        expected_result = [[1, 0, 1, 0],
                           [0, 1, 0, 1]]
        self.assertEqual(result, expected_result)
    def test_coloreo5(self):
        grafo = [[0,1,0,1,0],
                 [1,0,1,0,0],
                 [0,1,0,0,0],
                 [1,0,0,0,0],
                 [0,0,0,0,0]]
        colors, current_color = proyecto.coloreo(grafo)
        result = proyecto.generar_matrix(colors, current_color)
        
        expected_result = [[1, 0, 1, 0, 1],
                           [0, 1, 0, 1, 0]]
        self.assertEqual(result, expected_result)
    def test_coloreo6(self):
        grafo = [[0,0,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,1],
                [1,0,0,1,0,0,0,0],
                [1,0,1,0,1,0,1,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,1,1],
                [0,0,0,1,0,1,0,0],
                [0,1,0,0,0,1,0,0]]
        colors, current_color = proyecto.coloreo(grafo)
        result = proyecto.generar_matrix(colors, current_color)
        
        expected_result =  [[0,1,0,1,0,1,0,0],
                            [1,0,0,0,1,0,1,1],
                            [0,0,1,0,0,0,0,0]]
        
        self.assertEqual(result, expected_result)
if __name__ == '__main__':
    unittest.main()