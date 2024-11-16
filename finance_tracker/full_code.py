import datetime

class Category:
    def __init__(self, name):
        # name: название категории (например, "Еда", "Развлечения")
        self.name = name

    #* Метод для строкового представления категории
    #? Позволяет нам получать НОРМАЛЬНЫЙ ПОКАЗ от прямого принта Category
    #! Функция ВИЗИТКА для класса
    def __str__(self):
        return self.name


# Класс Transaction представляет каждую отдельную транзакцию (доход или расход).
class Transaction:
    def __init__(self, amount, category, date=None):
        # amount: сумма транзакции (положительная для дохода, отрицательная для расхода)
        # category: категория транзакции (например, "Еда", "Транспорт" и т.д ЧТО УГОДНО)
        # date: дата транзакции, по умолчанию текущая дата, если не указана
        self.amount = amount
        self.category = category
        self.date = date or datetime.date.today()  # Если дата не передана, используется текущая дата
        
    # Метод для отображения информации о транзакции в удобном виде
    def display(self):
        # Выводим дату, категорию и сумму (с плюсом или минусом в зависимости от типа транзакции)
        if self.amount >= 0:
            sign = "+"
        else:
            sign = "-"
        
        # Get the absolute value of the amount
        amount_str = f"${abs(self.amount)}"
        
        # Construct the string representation
        return f"{self.date} - {self.category}: {sign}{amount_str}"
    

class Account:
    def __init__(self):
        # Изначальный баланс равен 0
        self.balance = 0
        # Список для хранения всех транзакций
        self.transactions = []

    #? Метод для добавления транзакции в список и обновления баланса
    def add_transaction(self, transaction_object): #! ПРИНИМАЕТ объект от класса Transaction 
        self.transactions.append(transaction_object)  # Добавляем транзакцию в список
        self.balance += transaction_object.amount  #! Обновляем баланс на основе суммы транзакции

    # Метод для получения текущего баланса
    def get_balance(self):
        return self.balance

    # Метод для получения всех транзакций
    def get_transactions(self):
        return self.transactions
    
    def __str__(self):
        return str(self.balance)
