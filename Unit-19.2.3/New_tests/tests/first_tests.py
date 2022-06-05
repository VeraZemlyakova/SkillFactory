import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):   # Предварительны (подготовительный) метод в котором подключаем тестируемый объект
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):   # положительный тест-метод (проверка умножения)
        assert self.calc.multiply(self, 8, 2) == 16

    def test_multiply_division_correctly(self):   # положительный тест-метод (проверка деления)
        assert self.calc.division(self, 8, 2) == 4

    def test_multiply_subtraction_correctly(self):  # положительный тест-метод (проверка вычитания)
        assert self.calc.subtraction(self, 8, 2) == 6

    def test_multiply_adding_correctly(self):  # положительный тест-метод (проверка сложения)
        assert self.calc.adding(self, 8, 2) == 10


