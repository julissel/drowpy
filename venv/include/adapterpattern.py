# Пример использования адаптера
import re
from abc import ABC, abstractmethod
#from System import *


class System:
    # Класс, представляющий систему

    def __init__(self, text):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor):
        # Метод, требующий на вход класс-обработчик
        result = processor.process_text(self.text)
        print(*result, sep='\n')


class TextProcessor(ABC):
    # Абстрактный интерфейс обработчика

    @abstractmethod
    def process_text(self, text):
        pass


class WordCounter:
    # Обработчик, несовместимый с основной системой

    def count_words(self, text):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        # частота встречи конкретного слова
        return self.__words.get(word, 0)

    def get_all_words(self):
        # частотный словарь всех встреченых слов
        return self.__words.copy()


class WordCounterAdapter(TextProcessor):
    # Адаптер к обработчику

    def __init__(self, adaptee):
        # В конструкторе указывается, к какому объекту следует подключить адаптер
        self.adaptee = adaptee

    def process_text(self, text):
        # Реализация интерфейса обработчика, требуемого системой
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words().keys()
        return sorted(words,
                      key=lambda x: self.adaptee.get_count(x),
                      reverse=True)


text = '''
Подружился как-то мужик с медведем. Вот и вздумали они вместе репу сеять. Посеяли и начали уговариваться,
кому что брать. Мужик и говорит:
- Я возьму себе корешки, а тебе Мишка достанутся вершки.
Выросла у них хорошая репа. Собрали они урожай. Мужик взял себе корешки, а Мише отдал вершки.
Видит медведь, что прогадал. Одни листья получил и говорит мужику:
- Ты, брат, меня надул. Ну, смотри, когда будем в другой раз сеять, ты уж меня так не проведешь.
На другой год говорит мужик медведю:
- Давай, Миша, опять вместе сеять.
- Давай, только теперь ты себе бери вершки, а мне отдавай корешки – уговаривается Миша.
- Ладно! – говорит мужик. – Пусть будет по-твоему.
И посеяли пшеницу.Добрая пшеница уродилась. Мужик взял себе вершки, а Мише отдал корешки.
Намолотил мужик пшеницы, намолол муки, напек пирогов, а медведь опять ни с чем. Сидит над ворохом сухих стеблей.
Вот с тех пор перестали медведь с мужиком дружбу водить.
'''

# передаем текст в си-му
system = System(text)
# создаем обработчик
counter = WordCounter()
# создаем адаптер, в который в качестве адаптируемого объекта, передаем объявленный ранее счетчик
adapter = WordCounterAdapter(counter)
# передаем обработчик в систему
system.get_processed_text(adapter)
