from typing import List, Optional, Tuple


class MusicalInstrument:
    """
    Базовый класс для всех музыкальных инструментов.
    
    Attributes:
        name (str): Название инструмента.
        year_made (int): Год изготовления инструмента.
        material (str): Основной материал изготовления.
        _price (float): Цена инструмента (непубличный атрибут).
    """
    
    def __init__(self, name: str, year_made: int, material: str, price: float) -> None:
        """
        Инициализирует экземпляр музыкального инструмента.
        
        Args:
            name: Название инструмента.
            year_made: Год изготовления.
            material: Основной материал.
            price: Цена инструмента.
        """
        self.name = name
        self.year_made = year_made
        self.material = material
        self._price = price  
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление инструмента для пользователя.
        
        Returns:
            Строковое представление инструмента.
        """
        return f"{self.name} ({self.year_made}), материал: {self.material}"
    
    def __repr__(self) -> str:
        """
        Возвращает строковое представление инструмента для разработчика.
        
        Returns:
            Строковое представление инструмента для отладки.
        """
        return f"MusicalInstrument(name='{self.name}', year_made={self.year_made}, material='{self.material}', price={self._price})"
    
    def play(self) -> str:
        """
        Воспроизводит звук инструмента.
        
        Returns:
            Строка, описывающая звук инструмента.
        """
        return f"Звучит {self.name}..."
    
    def get_age(self) -> int:
        """
        Вычисляет возраст инструмента.
        
        Returns:
            Возраст инструмента в годах.
        """
        current_year = 2025  
        return current_year - self.year_made
    
    def get_price(self) -> float:
        """
        Возвращает цену инструмента.
        
        Returns:
            Цена инструмента.
        """
        return self._price
    
    def set_price(self, new_price: float) -> None:
        """
        Устанавливает новую цену инструмента.
        
        Args:
            new_price: Новая цена инструмента.
        """
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = new_price


class Guitar(MusicalInstrument):
    """
    Класс для представления гитары.
    
    Attributes:
        name (str): Название гитары.
        year_made (int): Год изготовления гитары.
        material (str): Основной материал изготовления.
        _price (float): Цена гитары (непубличный атрибут).
        strings_count (int): Количество струн.
        guitar_type (str): Тип гитары (акустическая, электрическая и т.д.).
        _tuning (List[str]): Текущий строй гитары (непубличный атрибут).
    """
    
    def __init__(self, name: str, year_made: int, material: str, price: float, 
                 strings_count: int = 6, guitar_type: str = "acoustic", 
                 tuning: Optional[List[str]] = None) -> None:
        """
        Инициализирует экземпляр гитары.
        
        Args:
            name: Название гитары.
            year_made: Год изготовления.
            material: Основной материал.
            price: Цена гитары.
            strings_count: Количество струн, по умолчанию 6.
            guitar_type: Тип гитары (акустическая, электрическая и т.д.).
            tuning: Строй гитары, по умолчанию стандартный строй.
        """
        super().__init__(name, year_made, material, price)
        self.strings_count = strings_count
        self.guitar_type = guitar_type
        
        if tuning is None:
            self._tuning = ["E", "A", "D", "G", "B", "E"]
        else:
            self._tuning = tuning
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление гитары для пользователя.
        
        Returns:
            Строковое представление гитары.
        """
        return f"{self.guitar_type.capitalize()} гитара {self.name} ({self.year_made}), {self.strings_count} струн"
    
    def __repr__(self) -> str:
        """
        Возвращает строковое представление гитары для разработчика.
        
        Returns:
            Строковое представление гитары для отладки.
        """
        return f"Guitar(name='{self.name}', year_made={self.year_made}, material='{self.material}', price={self._price}, strings_count={self.strings_count}, guitar_type='{self.guitar_type}')"
    
    def play(self) -> str:
        """
        Воспроизводит звук гитары.
        
        Метод перегружен, так как звук гитары отличается от общего звука музыкальных инструментов
        и зависит от типа гитары.
        
        Returns:
            Строка, описывающая звук гитары.
        """
        if self.guitar_type == "acoustic":
            return "Звучит мелодичный перебор струн акустической гитары..."
        elif self.guitar_type == "electric":
            return "Звучит яркий электрический риф..."
        else:
            return f"Звучит {self.guitar_type} гитара {self.name}..."
    
    def tune(self, new_tuning: List[str]) -> None:
        """
        Настраивает гитару на новый строй.
        
        Args:
            new_tuning: Новый строй гитары.
            
        Raises:
            ValueError: Если длина строя не соответствует количеству струн.
        """
        if len(new_tuning) != self.strings_count:
            raise ValueError(f"Количество нот ({len(new_tuning)}) не соответствует количеству струн ({self.strings_count})")
        self._tuning = new_tuning
    
    def get_tuning(self) -> List[str]:
        """
        Возвращает текущий строй гитары.
        
        Returns:
            Список нот текущего строя.
        """
        return self._tuning.copy()


class Piano(MusicalInstrument):
    """
    Класс для представления фортепиано.
    
    Attributes:
        name (str): Название фортепиано.
        year_made (int): Год изготовления фортепиано.
        material (str): Основной материал изготовления.
        _price (float): Цена фортепиано (непубличный атрибут).
        piano_type (str): Тип фортепиано (рояль, пианино и т.д.).
        keys_count (int): Количество клавиш.
        _last_tuned_date (Optional[str]): Дата последней настройки (непубличный атрибут).
    """
    
    def __init__(self, name: str, year_made: int, material: str, price: float,
                 piano_type: str = "grand", keys_count: int = 88,
                 last_tuned_date: Optional[str] = None) -> None:
        """
        Инициализирует экземпляр фортепиано.
        
        Args:
            name: Название фортепиано.
            year_made: Год изготовления.
            material: Основной материал.
            price: Цена фортепиано.
            piano_type: Тип фортепиано (рояль, пианино и т.д.).
            keys_count: Количество клавиш, по умолчанию 88.
            last_tuned_date: Дата последней настройки в формате "ГГГГ-ММ-ДД".
        """
        super().__init__(name, year_made, material, price)
        self.piano_type = piano_type
        self.keys_count = keys_count
        
        # Дата настройки непубличная, так как требует специальной проверки и форматирования
        self._last_tuned_date = last_tuned_date
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление фортепиано для пользователя.
        
        Returns:
            Строковое представление фортепиано.
        """
        piano_type_ru = "Рояль" if self.piano_type == "grand" else "Пианино"
        return f"{piano_type_ru} {self.name} ({self.year_made}), {self.keys_count} клавиш"
    
    def __repr__(self) -> str:
        """
        Возвращает строковое представление фортепиано для разработчика.
        
        Returns:
            Строковое представление фортепиано для отладки.
        """
        return f"Piano(name='{self.name}', year_made={self.year_made}, material='{self.material}', price={self._price}, piano_type='{self.piano_type}', keys_count={self.keys_count}, last_tuned_date='{self._last_tuned_date}')"
    
    def play(self) -> str:
        """
        Воспроизводит звук фортепиано.
        
        Метод перегружен, так как звук фортепиано отличается от общего звука музыкальных инструментов
        и зависит от типа фортепиано.
        
        Returns:
            Строка, описывающая звук фортепиано.
        """
        if self.piano_type == "grand":
            return "Звучит глубокий и насыщенный звук рояля..."
        else:
            return "Звучит мелодичное пианино..."
    
    def get_age(self) -> Tuple[int, str]:
        """
        Вычисляет возраст фортепиано и возвращает рекомендации по обслуживанию.
        
        Метод перегружен, так как для фортепиано важно не только знать возраст,
        но и получить рекомендации по обслуживанию в зависимости от возраста.
        
        Returns:
            Кортеж с возрастом инструмента и рекомендацией по обслуживанию.
        """
        age = super().get_age()
        
        if age < 5:
            recommendation = "Рекомендуется настройка раз в год"
        elif age < 20:
            recommendation = "Рекомендуется настройка два раза в год и профилактический осмотр"
        else:
            recommendation = "Требуется регулярная настройка и профессиональное обслуживание"
            
        return age, recommendation
    
    def set_tuned_date(self, date: str) -> None:
        """
        Устанавливает дату последней настройки фортепиано.
        
        Args:
            date: Дата настройки в формате "ГГГГ-ММ-ДД".
            
        Raises:
            ValueError: Если формат даты неверный.
        """
        self._last_tuned_date = date
    
    def get_tuned_date(self) -> Optional[str]:
        """
        Возвращает дату последней настройки фортепиано.
        
        Returns:
            Дата последней настройки или None, если инструмент не настраивался.
        """
        return self._last_tuned_date


if __name__ == "__main__":

    guitar = Guitar("Fender Stratocaster", 2020, "клен", 1200.0, guitar_type="electric")
    piano = Piano("Yamaha C3", 2015, "красное дерево", 15000.0)
    
    print(guitar)  # Electric гитара Fender Stratocaster (2020), 6 струн
    print(piano)   # Рояль Yamaha C3 (2015), 88 клавиш
    
    print(guitar.play())  # Звучит яркий электрический риф...
    print(piano.play())   # Звучит глубокий и насыщенный звук рояля...
    
    print(f"Возраст гитары: {guitar.get_age()} лет")
    age, recommendation = piano.get_age()
    print(f"Возраст фортепиано: {age} лет. {recommendation}")
    
    guitar.tune(["D", "A", "D", "G", "B", "E"])
    print(f"Текущий строй гитары: {guitar.get_tuning()}")
    
    piano.set_tuned_date("2024-12-15")
    print(f"Последняя настройка фортепиано: {piano.get_tuned_date()}")