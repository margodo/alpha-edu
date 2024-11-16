
class Category:
    def __init__(self, name, min_age: int):
        # name: название категории (например, "Еда", "Развлечения")
        self.name = name
        self.min_age = min_age

    #* Метод для строкового представления категории
    #? Позволяет нам получать НОРМАЛЬНЫЙ ПОКАЗ от прямого принта Category
    # #! Функция ВИЗИТКА для класса
    def __str__(self):
        return f'Category name: {self.name} - Min age000: {self.min_age}'
    