"""
Тесты для приложения
pytest найдёт все функции, начинающиеся с test_
"""

import sys
import os

# Добавляем путь к корневой папке, чтобы импортировать main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import add, subtract

def test_add():
    """Тестируем сложение"""
    print("\n🧪 Тестируем add...")
    assert add(2, 2) == 4
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(100, 1) == 101
    print("✅ add работает")

def test_subtract():
    """Тестируем вычитание"""
    print("\n🧪 Тестируем subtract...")
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5
    assert subtract(10, 20) == -10
    print("✅ subtract работает")

def test_edge_cases():
    """Граничные случаи"""
    print("\n🧪 Тестируем граничные случаи...")
    assert add(999999, 1) == 1000000
    assert subtract(-5, -5) == 0
    print("✅ Граничные случаи работают")