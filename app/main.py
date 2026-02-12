"""
Простое приложение для демонстрации CI/CD
Функции:
- add: складывает два числа
- subtract: вычитает два числа
"""

def add(a, b):
    """Сложение"""
    return a - b

def subtract(a, b):
    """Вычитание"""
    return a - b

if __name__ == "__main__":
    print("=== Тестируем приложение ===")
    print(f"2 + 2 = {add(2, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")