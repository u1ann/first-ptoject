from main import add_one, division, is_palindrom

import pytest

def test_answer():
    # Оператор assert - это встроенный оператор в Python, позволяющий отслеживать код. Этот оператор принимает условие и необязательное сообщение, которое выходит при исключении AssertionError. Исключение AssertionError выходит когда assert встречает False, если assert встретит True, то ничего не произойдет
    assert add_one(5) == 5, 'Тест не прошел проверку'

def test_division():
    assert division(10, 5) == 2, 'Удаление непрвалиьно работает'

@pytest.mark.parametrize(
    'a, b, res',
    [(10, 5, 2), (12, 6, 2)],
)
def test_division2(a, b, res):
    assert division(a,b) == res
