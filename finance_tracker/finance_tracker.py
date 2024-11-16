import json
from account_class import Account
from category_class import Category
from transaction_class import Transaction
import datetime

class FinanceTracker:
    def __init__(self):
        # Инициализация экземпляра класса Account, который будет хранить все данные
        self.account = Account()

    # Метод для добавления дохода
    def add_income(self, amount, category_name):
        # Создаем категорию для дохода
        category = Category('eda')
        # Создаем транзакцию с положительным значением
        transac = Transaction(34, category)
        # Добавляем транзакцию в учетный запис
        self.account.add_transaction(transac)
        print(f"Доход в размере ${amount} добавлен в категорию {category_name}.")





    # Метод для добавления расхода
    def add_expense(self, amount, category_name):
        # Создаем категорию для расхода
        category = Category(category_name)
        # Создаем транзакцию с отрицательным значением (расход)
        transaction = Transaction(-amount, category)
        # Добавляем транзакцию в учетный запис
        self.account.add_transaction(transaction)
        print(f"Расход в размере ${amount} добавлен в категорию {category_name}.")

    # Метод для отображения текущего баланса
    def view_balance(self):
        balance = self.account.get_balance()
        print(f"Ваш текущий баланс: ${balance}")

    # Метод для просмотра всех транзакций
    def view_transactions(self):
        transactions = self.account.get_transactions()
        if not transactions:
            print("Транзакций не найдено.")
            return
        for transaction in transactions:
            print(transaction.display())  # Отображаем каждую транзакцию

    # Метод для генерации отчета о доходах и расходах
    def generate_report(self):
        print("\nГенерация финансового отчета...")
        income = 0
        expenses = 0
        # Проходим по всем транзакциям, чтобы подсчитать доходы и расходы
        for transaction in self.account.get_transactions():
            if transaction.amount > 0:
                income += transaction.amount  # Суммируем доходы
            else:
                expenses += abs(transaction.amount)  # Суммируем расходы
        balance = self.account.get_balance()

        print(f"\nОбщий доход: ${income}")
        print(f"Общие расходы: ${expenses}")
        print(f"Баланс: ${balance}")

    # Метод для сохранения данных в файл
    def save_data(self, filename="finance_data.json"):
        # Подготовка данных для сохранения
        data = {
            "balance": self.account.get_balance(),
            "transactions": [{
                "amount": t.amount,
                "category": t.category.name,
                "date": str(t.date)
            } for t in self.account.get_transactions()]
        }
        # Сохранение данных в файл в формате JSON
        with open(filename, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Данные сохранены в {filename}.")

    # Метод для загрузки данных из файла
    def load_data(self, filename="finance_data.json"):
        try:
            # Попытка загрузить данные из файла
            with open(filename, "r", encoding='utf-8') as file:
                data = json.load(file)
                self.account.balance = data["balance"]  # Восстановление баланса
                # Восстановление транзакций
                for t_data in data["transactions"]:
                    category = Category(t_data["category"])  # Создание категории
                    date = datetime.datetime.strptime(t_data["date"], "%Y-%m-%d").date()  # Преобразование даты из строки
                    transaction = Transaction(t_data["amount"], category, date)  # Создание транзакции
                    self.account.add_transaction(transaction)  # Добавление транзакции
            print(f"Данные загружены из {filename}.")
        except FileNotFoundError:
            print("Не удалось найти файл данных. Начинаем с пустого списка.")
