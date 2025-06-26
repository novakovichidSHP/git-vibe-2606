import math

def solve_quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return f"Два корня: x1 = {x1}, x2 = {x2}"
    elif d == 0:
        x = -b / (2 * a)
        return f"Один корень: x = {x}"
    else:
        return "Корней нет (дискриминант < 0)"

def main():
    print("Решение квадратного уравнения ax^2 + bx + c = 0")
    try:
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))
        if a == 0:
            print("Коэффициент a не должен быть равен 0!")
            return
        result = solve_quadratic(a, b, c)
        print(result)
    except ValueError:
        print("Ошибка ввода! Введите числовые значения.")

if __name__ == "__main__":
    main() 