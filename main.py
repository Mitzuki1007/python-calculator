import math


# Проверка и преобразование числа
def parse_number(value):
    try:
        number = float(value)
    except ValueError:
        raise ValueError("Необходимо ввести число.")

    if not math.isfinite(number):
        raise ValueError("Число должно быть конечным.")

    return number


# Ввод одного числа
def read_number(message):
    while True:
        value = input(message).strip()

        try:
            return parse_number(value)
        except ValueError as error:
            print(f"Ошибка: {error}")


# Ввод списка чисел
def read_numbers():
    while True:
        value = input(
            "Введите числа через пробел или запятую: "
        ).strip()

        if not value:
            print("Ошибка: список не может быть пустым.")
            continue

        values = value.replace(",", " ").replace(";", " ").split()

        try:
            return [parse_number(item) for item in values]
        except ValueError as error:
            print(f"Ошибка: {error}. Повторите ввод.")


# Математические операции
def addition(a, b):
    """Сложение двух чисел."""
    return a + b


def subtraction(a, b):
    """Вычитание двух чисел."""
    return a - b


def multiplication(a, b):
    """Умножение двух чисел."""
    return a * b


def division(a, b):
    """Деление двух чисел."""
    if b == 0:
        raise ZeroDivisionError("Делить на ноль нельзя.")

    return a / b


def arithmetic_mean(numbers):
    """Вычисление среднего арифметического."""
    if not numbers:
        raise ValueError("Список чисел пуст.")

    return math.fsum(numbers) / len(numbers)


# Проверка результата вычислений
def validate_result(result):
    if not math.isfinite(result):
        raise OverflowError("Результат слишком велик.")

    return result


# Отображение меню
def show_menu():
    print("\n========== КАЛЬКУЛирен ==========")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Среднее арифметическое")
    print("6. Помощь")
    print("0. Выход")
    print("=================================")

# Отображение справочной информации
def show_help():
    print("\n========== ПОМОЩЬ ==========")
    print("1. Сложение — сложение двух чисел.")
    print("2. Вычитание — вычитание второго числа из первого.")
    print("3. Умножение — умножение двух чисел.")
    print("4. Деление — деление первого числа на второе.")
    print("   Деление на ноль запрещено.")
    print("5. Среднее арифметическое — вычисление среднего")
    print("   значения списка введённых чисел.")
    print("   Числа можно вводить через пробел, запятую или точку с запятой.")
    print("6. Помощь — отображение этой справки.")
    print("0. Выход — завершение работы калькулятора.")
    print("============================")

# Основной цикл калькулятора
def main():
    operations = {
        "1": addition,
        "2": subtraction,
        "3": multiplication,
        "4": division
    }

    print("Добро пожаловать в калькулятор!")

    while True:
        show_menu()

        choice = input("Выберите пункт меню: ").strip()

        if choice == "0":
            print("Спасибо за использование калькулятора! Би Би.")
            break

        if choice == "6":
            show_help()
            continue

        try:
            if choice in operations:
                a = read_number("Введите первое число: ")
                b = read_number("Введите второе число: ")

                result = operations[choice](a, b)

            elif choice == "5":
                numbers = read_numbers()
                result = arithmetic_mean(numbers)

            else:
                print("Ошибка: неверный пункт меню.")
                continue

            result = validate_result(result)
            print(f"Результат: {result}")

        except ZeroDivisionError as error:
            print(f"Ошибка: {error}")

        except ValueError as error:
            print(f"Ошибка: {error}")

        except OverflowError as error:
            print(f"Ошибка: {error}")


# Запуск программы
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nСпасибо за использование калькулятора! Би Би.")