class Car:
    def __init__(self, name, year, maker, engine_size, color, price):
        self.name = name
        self.year = year
        self.maker = maker
        self.engine_size = engine_size
        self.color = color
        self.price = price

    def data_input(self):
        self.name = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.maker = input("Введите производителя: ")
        self.engine_size = float(input("Введите объём двигателя: "))
        self.color = input("Введите цвет: ")
        self.price = float(input("Введите цену: "))

    def data_output(self):
        print("Характеристики машины".center(35, "-"))
        print(f"Название модели: {self.name}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.maker}")
        print(f"Объём двигателя: {self.engine_size}")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price}")
    
    def output_name(self):
        print(f"Название модели: {self.name}".center(35, "-"))
    
    def output_year(self):
        print(f"Год выпуска: {self.year}".center(35, "-"))

    def output_maker(self):
        print(f"Производитель: {self.maker}".center(35, "-"))
    
    def output_engine_size(self):
        print(f"Объём двигателя: {self.engine_size}".center(35, "-"))

    def output_color(self):
        print(f"Цвет: {self.color}".center(35, "-"))
    
    def output_price(self):
        print(f"Цена: {self.price}".center(35, "-"))


car = Car("Model X", 2023, "Tesla", 3.5, "Black", 4000000)
while True:
    try:
        print("1. Добавить автомобиль")
        print("2. Отобразить все хар-ка автомобиля")
        print("3. Отобразить название автомобиля")
        print("4. Отобразить год выпуска автомобиля")
        print("5. Отобразить производителя автомобиля")
        print("6. Отобразить объём двигателя автомобиля")
        print("7. Отобразить цвет автомобиля")
        print("8. Отобразить цену автомобиля")
        print("9. Выход")
        choice = int(input("Выберите номер пункта: "))
        if 0 < choice < 10:
            if choice == 1:
                car.data_input()
            elif choice == 2:
                car.data_output()
            elif choice == 3:
                car.output_name()
            elif choice == 4:
                car.output_year()
            elif choice == 5:
                car.output_maker()
            elif choice == 6:
                car.output_engine_size()
            elif choice == 7:
                car.output_color()
            elif choice == 8:
                car.output_price()
            elif choice == 9:
                break
        else:
            print("Ошибка! Диапазон от 1 до 9".center(35, "-"))
    except ValueError:
        print("Ошибка! Введите цифру".center(35, "-"))