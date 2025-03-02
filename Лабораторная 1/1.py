import doctest
from typing import List, Dict, Optional, Union, Set


class Book:
    def __init__(self, title: str, pages: int, author: str):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param pages: Количество страниц
        :param author: Автор книги

        Примеры:
        >>> book = Book("Война и мир", 1225, "Лев Толстой")
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть строкой")
        if not author.strip():
            raise ValueError("Имя автора не может быть пустым")
        self.author = author

    def read_pages(self, num_pages: int) -> bool:
        """
        Прочитать указанное количество страниц книги

        :param num_pages: Количество страниц для прочтения
        :return: True, если страницы успешно прочитаны, иначе False

        Примеры:
        >>> book = Book("Война и мир", 1225, "Лев Толстой")
        >>> book.read_pages(50)
        True
        """
        ...

    def get_reading_time(self, reading_speed: int) -> float:
        """
        Рассчитать примерное время чтения книги

        :param reading_speed: Скорость чтения (страниц в час)
        :return: Время в часах, необходимое для прочтения книги

        Примеры:
        >>> book = Book("Война и мир", 1225, "Лев Толстой")
        >>> book.get_reading_time(50)
        24.5
        """
        ...

    def add_bookmark(self, page: int) -> None:
        """
        Добавить закладку на указанную страницу

        :param page: Номер страницы для закладки
        :raise ValueError: Если номер страницы выходит за пределы книги

        Примеры:
        >>> book = Book("Война и мир", 1225, "Лев Толстой")
        >>> book.add_bookmark(100)
        """
        ...


class SocialNetwork:
    def __init__(self, name: str, active_users: int, max_message_length: Optional[int] = None):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название социальной сети
        :param active_users: Количество активных пользователей
        :param max_message_length: Максимальная длина сообщения (None если нет ограничений)

        Примеры:
        >>> network = SocialNetwork("MyNetwork", 1000000, 280)
        """
        if not isinstance(name, str):
            raise TypeError("Название сети должно быть строкой")
        if not name.strip():
            raise ValueError("Название сети не может быть пустым")
        self.name = name

        if not isinstance(active_users, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if active_users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        self.active_users = active_users

        if max_message_length is not None:
            if not isinstance(max_message_length, int):
                raise TypeError("Максимальная длина сообщения должна быть целым числом")
            if max_message_length <= 0:
                raise ValueError("Максимальная длина сообщения должна быть положительным числом")
        self.max_message_length = max_message_length

    def post_message(self, message: str) -> bool:
        """
        Опубликовать сообщение в социальной сети

        :param message: Текст сообщения
        :return: True, если сообщение опубликовано успешно, иначе False

        Примеры:
        >>> network = SocialNetwork("MyNetwork", 1000000, 280)
        >>> network.post_message("Привет, мир!")
        True
        """
        ...

    def get_trending_topics(self, limit: int = 10) -> List[str]:
        """
        Получить список популярных тем

        :param limit: Максимальное количество тем для возврата
        :return: Список популярных тем

        Примеры:
        >>> network = SocialNetwork("MyNetwork", 1000000, 280)
        >>> network.get_trending_topics(5)
        ['Технологии', 'Спорт', 'Политика', 'Кино', 'Музыка']
        """
        ...

    def get_user_engagement(self, days: int) -> Dict[str, float]:
        """
        Получить статистику вовлеченности пользователей

        :param days: Количество дней для анализа
        :return: Словарь с метриками вовлеченности

        Примеры:
        >>> network = SocialNetwork("MyNetwork", 1000000, 280)
        >>> network.get_user_engagement(7)
        {'daily_active': 800000, 'posts_per_user': 2.3, 'average_time': 45.5}
        """
        ...


class DataStructure:
    def __init__(self, structure_type: str, max_size: Optional[int] = None, is_ordered: bool = True):
        """
        Создание и подготовка к работе объекта "Структура данных"

        :param structure_type: Тип структуры данных (стек, очередь, дерево и т.д.)
        :param max_size: Максимальный размер структуры (None если не ограничен)
        :param is_ordered: Упорядочена ли структура

        Примеры:
        >>> stack = DataStructure("stack", 100, True)
        """
        valid_types = {"stack", "queue", "tree", "graph", "hash_table", "list", "array"}
        if not isinstance(structure_type, str):
            raise TypeError("Тип структуры должен быть строкой")
        if structure_type.lower() not in valid_types:
            raise ValueError(f"Тип структуры должен быть одним из: {', '.join(valid_types)}")
        self.structure_type = structure_type.lower()

        if max_size is not None:
            if not isinstance(max_size, int):
                raise TypeError("Максимальный размер должен быть целым числом")
            if max_size <= 0:
                raise ValueError("Максимальный размер должен быть положительным числом")
        self.max_size = max_size

        if not isinstance(is_ordered, bool):
            raise TypeError("Параметр упорядоченности должен быть булевым значением")
        self.is_ordered = is_ordered

        self.elements = []

    def add_element(self, element: Union[int, str, float, dict]) -> bool:
        """
        Добавить элемент в структуру данных

        :param element: Элемент для добавления
        :return: True, если элемент добавлен успешно, иначе False

        Примеры:
        >>> stack = DataStructure("stack", 100, True)
        >>> stack.add_element(42)
        True
        """
        ...

    def remove_element(self) -> Optional[Union[int, str, float, dict]]:
        """
        Удалить элемент из структуры данных

        :return: Удаленный элемент или None, если структура пуста

        Примеры:
        >>> stack = DataStructure("stack", 100, True)
        >>> stack.add_element(42)
        True
        >>> stack.remove_element()
        42
        """
        ...

    def get_size(self) -> int:
        """
        Получить текущий размер структуры данных

        :return: Количество элементов в структуре

        Примеры:
        >>> stack = DataStructure("stack", 100, True)
        >>> stack.add_element(42)
        True
        >>> stack.get_size()
        1
        """
        ...


if __name__ == "__main__":
    doctest.testmod()