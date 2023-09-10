class Book:
    def __init__(self, name, year, maker, genre, author, price):
        self.name = name
        self.year = year
        self.maker = maker
        self.genre = genre
        self.author = author
        self.price = price

    def data_input(self):
        self.name = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.maker = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = float(input("Введите цену: "))

    def data_output(self):
        print("Описание книги".center(35, "-"))
        print(f"Название книги: {self.name}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.maker}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price}")
    
    def output_name(self):
        print(f"Название книги: {self.name}".center(35, "-"))
    
    def output_year(self):
        print(f"Год выпуска: {self.year}".center(35, "-"))

    def output_maker(self):
        print(f"Издатель: {self.maker}".center(35, "-"))
    
    def output_genre(self):
        print(f"Жанр: {self.genre}".center(35, "-"))

    def output_author(self):
        print(f"Автор: {self.author}".center(35, "-"))
    
    def output_price(self):
        print(f"Цена: {self.price}".center(35, "-"))


book = Book("Зелёная миля", 2014, "Ast", "Ужасы", "Стивен Кинг", 450)
while True:
    try:
        print("1. Добавить книгу")
        print("2. Отобразить все описание о книге")
        print("3. Отобразить название книги")
        print("4. Отобразить год выпуска книги")
        print("5. Отобразить издательство книги")
        print("6. Отобразить жанр книги")
        print("7. Отобразить автора книги")
        print("8. Отобразить цену книги")
        print("9. Выход")
        choice = int(input("Выберите номер пункта: "))
        if 0 < choice < 10:
            if choice == 1:
                book.data_input()
            elif choice == 2:
                book.data_output()
            elif choice == 3:
                book.output_name()
            elif choice == 4:
                book.output_year()
            elif choice == 5:
                book.output_maker()
            elif choice == 6:
                book.output_genre()
            elif choice == 7:
                book.output_author()
            elif choice == 8:
                book.output_price()
            elif choice == 9:
                break
        else:
            print("Ошибка! Диапазон от 1 до 9".center(35, "-"))
    except ValueError:
        print("Ошибка! Введите цифру".center(35, "-"))