import random
import unittest

def generate_array(size):
    """
    Genera una matriz cuadrada de tamaño NxN y la rellena con números aleatorios entre 0 y 9.

    Args:
        size (int): Tamaño de la matriz.

    Returns:
        array: La matriz generada.
    """
    array = []
    for _ in range(size):
        row = [random.randint(0, 9) for _ in range(size)]
        array.append(row)
    return array

def addUp_rows(array):
    """
    Calcula la suma de los elementos de cada fila de la matriz.

    Args:
        array (list): La matriz.

    Returns:
        list: Una lista con las sumas de cada fila.
    """
    return [sum(row) for row in array]

def addUp_columns(array):
    """
    Calcula la suma de los elementos de cada columna de la matriz.

    Args:
        array (list): La matriz.

    Returns:
        list: Una lista con las sumas de cada columna.
    """
    size = len(array)
    return [sum(array[row][col] for row in range(size)) for col in range(size)]

def print_array(array):
    """
    Imprime la matriz en pantalla.

    Args:
        array (list): La matriz.
    """
    for row in array:
        print(row)

def main():
    try:
        # Solicita al usuario el tamaño de la matriz
        N = int(input("Enter the size of the array (N): "))
        if N <= 0:
            raise ValueError("The size of the array must be a positive integer.")
    except ValueError as e:
        # Captura excepciones de valor no válido
        print(f"Error: {e}")
        return

    # Genera la matriz
    array = generate_array(N)

    # Imprime la matriz generada
    print("generated array:")
    print_array(array)

    # Calcula la suma de cada fila
    addUp_rowsvar = addUp_rows(array)

    # Calcula la suma de cada columna
    addUp_columnsvar = addUp_columns(array)

    # Imprime la suma de cada fila
    print("\nSum of each row:")
    print(addUp_rowsvar)

    # Imprime la suma de cada columna
    print("\nSum of each column:")
    print(addUp_columnsvar)

class TestMatrixOperations(unittest.TestCase):
    def test_generate_array(self):
        # Prueba para verificar la generación de la matriz con el tamaño correcto y los elementos dentro del rango esperado
        array = generate_array(3)

        # Verifica si el tamaño de la matriz generada es 3x3
        self.assertEqual(len(array), 3)
        for row in array:
            # Verifica si cada fila de la matriz tiene 3 elementos
            self.assertEqual(len(row), 3)
            for elemento in row:
                # Verifica si cada elemento es mayor o igual a 0
                self.assertGreaterEqual(elemento, 0)
                # Verifica si cada elemento es menor o igual a 9
                self.assertLessEqual(elemento, 9)
                
    def test_addUp_rows(self):
        # Prueba para verificar el cálculo correcto de la suma de las filas de la matriz
        array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        addUp_rowsvar = addUp_rows(array)
        # Verifica si la suma de las filas es [6, 15, 24]
        self.assertEqual(addUp_rowsvar, [6, 15, 24])

    def test_addUp_columns(self):
        # Prueba para verificar el cálculo correcto de la suma de las columnas de la matriz
        array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        addUp_columnsvar = addUp_columns(array)
        # Verifica si la suma de las columnas es [12, 15, 18]
        self.assertEqual(addUp_columnsvar, [12, 15, 18])

# Si el archivo se está ejecutando como el programa principal
if __name__ == "__main__":
    # Llama a la función principal del programa
    main()
    # Ejecuta las pruebas unitarias utilizando unittest
    unittest.main()
