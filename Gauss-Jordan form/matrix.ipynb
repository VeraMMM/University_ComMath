def input_matrix(name):
    """Функция для ввода матрицы с клавиатуры"""
    print(f"\nВведите матрицу {name}:")
    rows = int(input("Количество строк: "))
    cols = int(input("Количество столбцов: "))
    
    matrix = []
    print(f"Введите элементы матрицы {name} построчно (через пробел):")
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != cols:
                    print(f"Ошибка: должно быть {cols} элементов в строке")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Ошибка: введите числа, разделенные пробелами")
    
    return matrix

def multiply_matrices(A, B):
    """Функция для умножения матриц"""
    if len(A[0]) != len(B):
        raise ValueError("Несовместимые размеры матриц для умножения")
    
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_val = 0
            for k in range(len(B)):
                sum_val += A[i][k] * B[k][j]
            row.append(sum_val)
        result.append(row)
    
    return result

def print_matrices_side_by_side(A, B, nameA="A", nameB="Результат"):
    """Функция для вывода двух матриц рядом"""
    print(f"\n{nameA} и {nameB} рядом:")
    
    # Находим максимальную длину строк для красивого вывода
    max_width = 0
    for matrix in [A, B]:
        for row in matrix:
            for val in row:
                max_width = max(max_width, len(f"{val:.2f}"))
    
    # Выводим матрицы рядом
    for i in range(max(len(A), len(B))):
        line = ""
        
        # Первая матрица
        if i < len(A):
            line += "["
            for j, val in enumerate(A[i]):
                line += f"{val:>{max_width}.2f}"
                if j < len(A[i]) - 1:
                    line += " "
            line += "]"
        else:
            line += " " * (max_width * len(A[0]) + len(A[0]) + 1) if A else ""
        
        line += "    "  # Разделитель между матрицами
        
        # Вторая матрица
        if i < len(B):
            line += "["
            for j, val in enumerate(B[i]):
                line += f"{val:>{max_width}.2f}"
                if j < len(B[i]) - 1:
                    line += " "
            line += "]"
        
        print(line)

def main():
    print("Программа для умножения матриц S * J * S1 и сравнения с A")
    print("=" * 50)
    
    try:
        # Ввод матриц
        A = input_matrix("A")
        S = input_matrix("S")
        J = input_matrix("J")
        S1 = input_matrix("S1")
        
        # Проверка совместимости размеров для умножения S * J * S1
        if len(S[0]) != len(J):
            raise ValueError("Количество столбцов S должно совпадать с количеством строк J")
        
        if len(J[0]) != len(S1):
            raise ValueError("Количество столбцов J должно совпадать с количеством строк S1")
        
        # Умножение матриц: S * J * S1
        print("\nВыполняем умножение матриц S * J * S1...")
        temp_result = multiply_matrices(S, J)
        final_result = multiply_matrices(temp_result, S1)
        
        # Проверка совпадения размеров A и результата
        if len(A) != len(final_result) or len(A[0]) != len(final_result[0]):
            print("Внимание: матрица A и результат имеют разные размеры!")
        
        # Вывод результатов
        print_matrices_side_by_side(A, final_result)
        
        # Дополнительная информация
        print(f"\nРазмер A: {len(A)}x{len(A[0])}")
        print(f"Размер результата S*J*S1: {len(final_result)}x{len(final_result[0])}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
