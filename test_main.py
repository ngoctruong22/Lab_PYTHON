import unittest
from main import twoSum


class TestTwoSum(unittest.TestCase):
    # Стандартный тест из примера 
    def test_example1(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_example2(self):
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])

    def test_example3(self):
        self.assertEqual(twoSum([3, 3], 6), [0, 1])

    def test_negative(self):
        # Тест с отрицательными числами
        self.assertEqual(twoSum([-1, -3, -2, -4], -6), [2, 3])

    def test_empty(self):
        # Тест с пустым массивом
        self.assertEqual(twoSum([], 1), None)

    def test_element_type(self):
        # Тест с неправильным типом данных (строка вместо числа)
        self.assertIsNone(twoSum(['a', 2, 4], 6))

    def test_no_answer(self):
        # Тест когда решения не существует
        self.assertEqual(twoSum([1, 2, 3, 4, 5], 10), None)

    def test_one_element(self):
        # Тест с одним элементом в массиве
        self.assertEqual(twoSum([5], 5), None)

    def test_more_than_answer(self):
        # Тест когда есть несколько возможных решений
        # Должен вернуть первое найденное решение
        self.assertEqual(twoSum([2, 2, 2, 2, 2], 4), [0, 1])

# Запуск тестов
if __name__ == '__main__':
    unittest.main()
