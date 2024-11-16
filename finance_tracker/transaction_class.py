import datetime
from category_class import Category
# Класс Transaction представляет каждую отдельную транзакцию (доход или расход).
class Transaction:
    def __init__(self, amount: float, category_test: str, date=None):
        # amount: сумма транзакции (положительная для дохода, отрицательная для расхода)
        # category: категория транзакции (например, "Еда", "Транспорт" и т.д ЧТО УГОДНО)
        # date: дата транзакции, по умолчанию текущая дата, если не указана
        self.amount = amount
        self.category_local = category_test
        self.date = date or datetime.date.today()  # Если дата не передана, используется текущая дата
        
    # Метод для отображения информации о транзакции в удобном виде
    def display(self):
        # Выводим дату, категорию и сумму (с плюсом или минусом в зависимости от типа транзакции)
        if self.amount >= 0:
            sign = "+"
        else:
            sign = "-"
        
        # Get the absolute value of the amount
        amount_str = f"${abs(self.amount)}" #! | -1 |
        
        # Construct the string representation
        return f"{self.date} - {self.category_local}: {sign}{amount_str}"

