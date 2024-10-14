import numpy as np

def input_matrix(shape):
    """Функція для введення матриці"""
    return np.array([list(map(int, input(f"Рядок {i + 1}: ").split())) for i in range(shape[0])])

def main():
    while True:
        print("\nОберіть операцію:\n1. Додавання\n2. Віднімання\n3. Множення на число\n4. Множення матриць\n5. Вихід")
        choice = input("Ваш вибір (1-5): ")

        if choice in ['1', '2']:
            rows, cols = map(int, input("Введіть кількість рядків і стовпців: ").split())
            matrix1 = input_matrix((rows, cols))
            matrix2 = input_matrix((rows, cols))
            result = (matrix1 + matrix2) if choice == '1' else (matrix1 - matrix2)
            print("Результат:\n", result)

        elif choice == '3':
            rows, cols = map(int, input("Введіть кількість рядків і стовпців: ").split())
            matrix = input_matrix((rows, cols))
            number = int(input("Введіть число: "))
            print("Результат:\n", matrix * number)

        elif choice == '4':
            rows1, cols1 = map(int, input("Введіть розміри першої матриці: ").split())
            matrix1 = input_matrix((rows1, cols1))
            rows2, cols2 = map(int, input("Введіть розміри другої матриці: ").split())
            if cols1 != rows2:
                print("Помилка: кількість стовпців першої матриці повинна дорівнювати кількості рядків другої.")
                continue
            matrix2 = input_matrix((rows2, cols2))
            print("Результат:\n", np.dot(matrix1, matrix2))

        elif choice == '5':
            break

if __name__ == "__main__":
    main()
