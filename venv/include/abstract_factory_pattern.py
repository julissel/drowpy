# Паттерн "Абстрактная фабрика"
from abc import ABC, abstractmethod


class HeroFactory(ABC):
    #  Абстрактная фабрика
    # Обявим методы, которые позволят создать персонажа. Используем механизм 'classmethod'
    @classmethod
    def create_hero(Class, name):
        return Class.Hero(name)

    @classmethod
    def create_spell(Class):
        return Class.Spell()

    @classmethod
    def create_weapon(Class):
        return Class.Weapon()


# Определим конкретные фабрики
# В каждой конкретной фабрике объявим собственные классы героя, оружия и заклинаний,
# которые будут специфичны для класса персонажа

class WarriorFactory(HeroFactory):
    # воин
    class Hero:
        def __init__(self, name):
            self.mame = name
            self.spell = None
            self.weapon = None
            self.armor = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Warrior hits with {self.weapon.hit()}")
            self.weapon.hit()

        def cast(self):
            print(f"Warrior casts {self.spell.cast()}")
            self.spell.cast()

    class Weapon:
        def hit(self):
            return "Claymore"

    class Spell:
        def cast(self):
            return "Power"


class MageFactory(HeroFactory):
    # маг
    class Hero:
        def __init__(self, name):
            self.name = name
            self.spell = None
            self.weapon = None
            self.armor = None

        def add_spell(self, spell):
            self.spell = spell

        def add_weapon(self, weapon):
            self.weapon = weapon

        def hit(self):
            print(f"Mage hits with {self.weapon.hit()}")
            self.weapon.hit()

        def cast(self):
            print(f"Mage casts {self.spell.cast()}")
            self.spell.cast()

    class Weapon:
        def hit(self):
            return "Staff"

    class Spell:
        def cast(self):
            return "Fireball"


class AssassinFactory(HeroFactory):
    # убийца
    class Hero:
        def __init__(self, name):
            self.name = name
            self.spell = None
            self.weapon = None
            self.armor = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Assassin hits with {self.weapon.hit()}")
            self.weapon.hit()

        def cast(self):
            print(f"Assassin casts {self.spell.cast()}")

    class Weapon:
        def hit(self):
            return "Dagger"

    class Spell:
        def cast(self):
            return "Invisibillity"


# Определим функцию, создающую персонажей
def create_hero(factory):
    hero = factory.create_hero("Nagibator")
    weapon = factory.create_weapon()
    spell = factory.create_spell()
    hero.add_weapon(weapon)
    hero.add_spell(spell)
    return hero


# Попробуем создать персонажей различных классов
player = create_hero(WarriorFactory())
player.hit()
player.cast()
print()
player1 = create_hero(MageFactory())
player1.hit()
player1.cast()
print()
player2 = create_hero(AssassinFactory())
player2.hit()
player2.cast()