class Stadium:
    def __init__(self, name, date, country, city, capacity):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def data_input(self):
        self.name = input("Введите название стадиона: ")
        self.date = input("Введите дату открытия: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость: "))

    def data_output(self):
        print("Стадион".center(35, "-"))
        print(f"Название стадиона: {self.name}")
        print(f"Дата выпуска: {self.date}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity}")
    
    def output_name(self):
        print(f"Название стадиона: {self.name}".center(35, "-"))
    
    def output_date(self):
        print(f"Дата выпуска: {self.date}".center(35, "-"))

    def output_country(self):
        print(f"Страна: {self.country}".center(35, "-"))
    
    def output_city(self):
        print(f"Город: {self.city}".center(35, "-"))

    def output_capacity(self):
        print(f"Вместимость: {self.capacity}".center(35, "-"))


stadium = Stadium("Камп Ноу", "24/09/1957", "Испания", "Барселона", 99_354)
while True:
    try:
        print("1. Добавить стадион")
        print("2. Отобразить всю информацию о стадионе")
        print("3. Отобразить название стадиона")
        print("4. Отобразить дату выпуска")
        print("5. Отобразить страну")
        print("6. Отобразить город")
        print("7. Отобразить вместимость")
        print("8. Выход")
        choice = int(input("Выберите номер пункта: "))
        if 0 < choice < 9:
            if choice == 1:
                stadium.data_input()
            elif choice == 2:
                stadium.data_output()
            elif choice == 3:
                stadium.output_name()
            elif choice == 4:
                stadium.output_date()
            elif choice == 5:
                stadium.output_country()
            elif choice == 6:
                stadium.output_city()
            elif choice == 7:
                stadium.output_capacity()
            elif choice == 8:
                break
        else:
            print("Ошибка! Диапазон от 1 до 8".center(35, "-"))
    except ValueError:
        print("Ошибка! Введите цифру".center(35, "-"))