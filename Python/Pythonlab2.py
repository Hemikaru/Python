def input_matrix(rows, cols):
    """Функція для введення матриці"""
    matrix = []
    print(f"Введіть елементи матриці {rows}x{cols}:")
    for i in range(rows):
        row = list(map(int, input(f"Рядок {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Помилка: рядок має містити {cols} елементів.")
            return None
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    """Функція для додавання двох матриць"""
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def subtract_matrices(matrix1, matrix2):
    """Функція для віднімання двох матриць"""
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrix_by_number(matrix, number):
    """Функція для множення матриці на число"""
    return [[matrix[i][j] * number for j in range(len(matrix[0]))] for i in range(len(matrix))]

def multiply_matrices(matrix1, matrix2):
    """Функція для множення двох матриць"""
    if len(matrix1[0]) != len(matrix2):
        print("Помилка: кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці.")
        return None
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

def print_matrix(matrix):
    """Функція для виведення матриці"""
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    """Основна функція для роботи з користувачем"""
    while True:
        print("\nОберіть операцію:")
        print("1. Додавання матриць")
        print("2. Віднімання матриць")
        print("3. Множення матриці на число")
        print("4. Множення двох матриць")
        print("5. Вихід")
        
        choice = input("Ваш вибір (1-5): ")

        if choice == '1' or choice == '2':
            rows, cols = map(int, input("Введіть кількість рядків і стовпців матриць: ").split())
            print("Введіть першу матрицю:")
            matrix1 = input_matrix(rows, cols)
            print("Введіть другу матрицю:")
            matrix2 = input_matrix(rows, cols)
            if matrix1 is None or matrix2 is None:
                continue
            if choice == '1':
                result = add_matrices(matrix1, matrix2)
                print("Результат додавання:")
            else:
                result = subtract_matrices(matrix1, matrix2)
                print("Результат віднімання:")
            print_matrix(result)

        elif choice == '3':
            rows, cols = map(int, input("Введіть кількість рядків і стовпців матриці: ").split())
            matrix = input_matrix(rows, cols)
            if matrix is None:
                continue
            number = int(input("Введіть число для множення: "))
            result = multiply_matrix_by_number(matrix, number)
            print("Результат множення матриці на число:")
            print_matrix(result)

        elif choice == '4':
            rows1, cols1 = map(int, input("Введіть кількість рядків і стовпців першої матриці: ").split())
            matrix1 = input_matrix(rows1, cols1)
            rows2, cols2 = map(int, input("Введіть кількість рядків і стовпців другої матриці: ").split())
            matrix2 = input_matrix(rows2, cols2)
            if matrix1 is None or matrix2 is None:
                continue
            result = multiply_matrices(matrix1, matrix2)
            if result:
                print("Результат множення двох матриць:")
                print_matrix(result)

        elif choice == '5':
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
