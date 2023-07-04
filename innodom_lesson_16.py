# -*- coding: utf-8 -*-
"""innoDom_lesson_16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MU6NShsypNg6WUs5aGBTW3scz3HZY64D

# **Принципы ООП: Инкапсуляция, Наследование, Множественное наследование**

**Наследование:**

Наследование в Python является одним из основных понятий объектно-ориентированного программирования (ООП). Оно позволяет создавать новые классы, наследующие свойства и методы от уже существующих классов.

Класс, от которого происходит наследование, называется базовым классом или родительским классом, а класс, который наследует свойства, называется производным классом или дочерним классом.

Когда производный класс наследует свойства и методы от базового класса, он может использовать их как свои собственные, добавлять новые или изменять существующие. Это позволяет существенно упростить разработку и поддержку кода, так как можно переиспользовать уже существующую функциональность.
"""

class Animal:
    def __init__(self):
        self.paws = 4
        self.tail = True
        self.ears = 2
        self.wool = True

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def say_mew(self):
        print(f"Your pet {self.name} say 'Meaw'!")


    def __str__(self):
        return f"""
        Cat's name: {self.name}
        Cat's age: {self.age}
        Cat's paws: {self.paws}
        Cat with tail? - {self.tail}
        Cat's ears: {self.ears}
        Cat have wool? - {self.wool}
        """

fluffy = Cat("Fluffy", 2)

print(fluffy)

class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus


    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus


    def __str__(self):
        return f"""
        {self.__class__.__name__} {self.name} getting salary {self.salary} per month
        His salary bonus = {self.bonus}
        Total bonus = {self.calculate_total_bonus()}
        """

class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 14.7)

    def cleaning()


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 25)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 150000, 99.99)

    def calculate_total_bonus(self):
        print("ПОТОМУ ЧТО Я ГЛАВНЫЙ!!!!!!!!")
        return self.salary // 100 * self.bonus

cleaner = Cleaner("Mike")
manager = Manager("Linda")
ceo = CEO("John")

print("-" * 45)
print(cleaner)
print("-" * 45)
print(manager)
print("-" * 45)
print(ceo)

class Engine:
    pass

class Wheel:
    pass

class Car(Engine):
    def __init__(self):
        self.enging = Engine()
        self.wheels = [Wheel()] * 4

e = Engine()

print(e)

print(dir(e))

help("keywords")

"""`Класс-родитель` – Animal, такие классы положено
называть суперклассом или базовым классом.

`Класс-потомок` – Cat, наследует все методы, а
свойства может наследовать только если в
конструкторе потомка определим с помощью
функции `super` переменные, которые можем
наследовать.

**Множественное наследование:**

Множественное наследование позволяет
наследовать класс от двух и более
родителей.
Такой вид наследования позволяет
создавать и проектировать сложные
структуры классов, связанных между
собой, но его использование должно быть
продуманным и аккуратным.
"""

class A:

    def __init__(self, name):
        self.name = name

    def print_method_a(self):
        print("Hello from class A from method a")


class B:
    def print_method_b(self):
        print("Hello from class B from method b")


class C(A, B):
    def print_method_c(self):
        print("Hello from class C from method c")

"""Если в классах-родителях методы
называются одинаково, тогда вызывается
метод первого передаваемого в скобках
класса.
"""

class A:

    def __init__(self, name):
        self.name = name

    def print_method(self):
        print("Hello from class A from method a")


class B:
    def print_method(self):
        print("Hello from class B from method b")


class C(B, A):
    def print_method_c(self):
        print("Hello from class C from method c")
        self.b = B.print_method()
        self.a = A.print_method()
        print(self.b, self.a, sep="\n")

c = C("Alex")

c.print_method()

"""Так же мы можем использовать наследование для переопределения работы каких-то методов:"""

class MyList(list):
    def __str__(self):
        return super().__str__().replace(", ", " | ")

class Engine: # Engine(object)
    pass

e = Engine()

print(dir(e))

"""Из примера выше, как вы могли обнаружить, все классы в Python наследуются от такой сущности, как `object`.

**Инкапсуляция**

Ещё один принцип ООП, который позволяет скрыть атрибуты либо методы
от общего использования в классе.
Инкапсуляция позволяет использовать такие методы и атрибуты только
при реализации класса. Это делается для методов и свойств, которые
нужны в использовании только внутри класса.

Поля либо методы скрываются, когда
перед названием стоит два нижних
подчеркивания.

! К скрытым методам либо полям
нельзя обратится вне класса.
"""

class MyClass:
    def __init__(self):
        self.__private_attribute = "hello"
        self._protected_attribute = "it's me"


    def __private_method(self):
        print("Hello from the private method")


    def public_method(self):
        print("Hello from the public method")
        self.__private_method()
        print(self.__private_attribute)

m = MyClass()

m._protected_attribute

"""**Инкапсуляция при наследовании:**

При наследовании, если у родителя есть инкапсулированные аргументы ( и прайват, и протектед ) при попытке переопределения их в классе-наследнике, протектед аргумент может быть перезаписан, но прайват аргумент не перезапишется! Создастся локальная переменная с таким же именем и уже новым значением:
"""

class First:
    def __init__(self):
        self._login = "login"
        self.__password = "qwerty"


class Second(First):
    def __init__(self):
        super().__init__()
        self._login = "my_awesome_logn"
        self.__password = "My n8w PasSwoRd!!!!"

f = First()
s = Second()

print(s._login)
print(s._Second__password)
print(s._First__password)
# print(dir(s))

# Card
# Deck
# Player
# Dealer (Player)
# Game

class Card:
    def __init__(self, rank, suit, template):
        self.rank = rank
        self._suit = suit
        self.template = template
        self._value = self._calculate_value()


    def get_value(self):
        return self._value

    def _calculate_value(self):
        if self.rank in ("J", "Q", "K"):
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)

    def __repr__(self):
        return f"{self.template}"

import random


class Deck:
    def __init__(self):
        self._cards = self._create_standart_deck()


    def shuffle(self):
        random.shuffle(self._cards)

    def deal_card(self):
        return self._cards.pop()

    def count_cards(self):
        return len(self._cards)


    @staticmethod
    def _create_standart_deck():
        card_deck = [
            {
                "rank": "6",
                "suit": "♣️",
                "template": """
                ==============
                # 6 ♣️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        6 ♣️ #
                ==============
                """
            },
            {
                "rank": "6",
                "suit": "♦️",
                "template": """
                ==============
                # 6 ♦️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        6 ♦️ #
                ==============
                """
            },
            {
                "rank": "6",
                "suit": "♥️",
                "template": """
                ==============
                # 6 ♥️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        6 ♥️ #
                ==============
                """
            },
            {
                "rank": "6",
                "suit": "♠️",
                "template": """
                ==============
                # 6 ♠️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        6 ♠️ #
                ==============
                """
            },
            {
                "rank": "7",
                "suit": "♣️",
                "template": """
                ==============
                # 7 ♣️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        7 ♣️ #
                ==============
                """
            },
            {
                "rank": "7",
                "suit": "♦️",
                "template": """
                ==============
                # 7 ♦️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        7 ♦️ #
                ==============
                """
            },
            {
                "rank": "7",
                "suit": "♥️",
                "template": """
                ==============
                # 7 ♥️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        7 ♥️ #
                ==============
                """
            },
            {
                "rank": "7",
                "suit": "♠️",
                "template": """
                ==============
                # 7 ♠️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        7 ♠️ #
                ==============
                """
            },
            {
                "rank": "8",
                "suit": "♣️",
                "template": """
                ==============
                # 8 ♣️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        8 ♣️ #
                ==============
                """
            },
            {
                "rank": "8",
                "suit": "♦️",
                "template": """
                ==============
                # 8 ♦️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        8 ♦️ #
                ==============
                """
            },
            {
                "rank": "8",
                "suit": "♥️",
                "template": """
                ==============
                # 8 ♥️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        8 ♥️ #
                ==============
                """
            },
            {
                "rank": "8",
                "suit": "♠️",
                "template": """
                ==============
                # 8 ♠️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        8 ♠️ #
                ==============
                """
            },
            {
                "rank": "9",
                "suit": "♣️",
                "template": """
                ==============
                # 9 ♣️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        9 ♣️ #
                ==============
                """
            },
            {
                "rank": "9",
                "suit": "♦️",
                "template": """
                ==============
                # 9 ♦️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        9 ♦️ #
                ==============
                """
            },
            {
                "rank": "9",
                "suit": "♥️",
                "template": """
                ==============
                # 9 ♥️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        9 ♥️ #
                ==============
                """
            },
            {
                "rank": "9",
                "suit": "♠️",
                "template": """
                ==============
                # 9 ♠️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        9 ♠️ #
                ==============
                """
            },
            {
                "rank": "10",
                "suit": "♣️",
                "template": """
                ==============
                # 10 ♣️       #
                #            #
                #            #
                #            #
                #            #
                #            #
                #       10 ♣️ #
                ==============
                """
            },
            {
                "rank": "10",
                "suit": "♦️",
                "template": """
                ==============
                # 10 ♦️       #
                #            #
                #            #
                #            #
                #            #
                #            #
                #       10 ♦️ #
                ==============
                """
            },
            {
                "rank": "10",
                "suit": "♥️",
                "template": """
                ==============
                # 10 ♥️       #
                #            #
                #            #
                #            #
                #            #
                #            #
                #       10 ♥️ #
                ==============
                """
            },
            {
                "rank": "10",
                "suit": "♠️",
                "template": """
                ==============
                # 10 ♠️       #
                #            #
                #            #
                #            #
                #            #
                #            #
                #       10 ♠️ #
                ==============
                """
            },
            {
                "rank": "J",
                "suit": "♣️",
                "template": """
                ==============
                # J ♣️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        J ♣️ #
                ==============
                """
            },
            {
                "rank": "J",
                "suit": "♦️",
                "template": """
                ==============
                # J ♦️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        J ♦️ #
                ==============
                """
            },
            {
                "rank": "J",
                "suit": "♥️",
                "template": """
                ==============
                # J ♥️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        J ♥️ #
                ==============
                """
            },
            {
                "rank": "J",
                "suit": "♠️",
                "template": """
                ==============
                # J ♠️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        J ♠️ #
                ==============
                """
            },
            {
                "rank": "Q",
                "suit": "♣️",
                "template": """
                ==============
                # Q ♣️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        Q ♣️ #
                ==============
                """
            },
            {
                "rank": "Q",
                "suit": "♦️",
                "template": """
                ==============
                # Q ♦️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        Q ♦️ #
                ==============
                """
            },
            {
                "rank": "Q",
                "suit": "♥️",
                "template": """
                ==============
                # Q ♥️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        Q ♥️ #
                ==============
                """
            },
            {
                "rank": "Q",
                "suit": "♠️",
                "template": """
                ==============
                # Q ♠️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        Q ♠️ #
                ==============
                """
            },
            {
                "rank": "K",
                "suit": "♣️",
                "template": """
                ==============
                # K ♣️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        K ♣️ #
                ==============
                """
            },
            {
                "rank": "K",
                "suit": "♦️",
                "template": """
                ==============
                # K ♦️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        K ♦️ #
                ==============
                """
            },
            {
                "rank": "K",
                "suit": "♥️",
                "template": """
                ==============
                # K ♥️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        K ♥️ #
                ==============
                """
            },
            {
                "rank": "K",
                "suit": "♠️",
                "template": """
                ==============
                # K ♠️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        K ♠️ #
                ==============
                """
            },
            {
                "rank": "A",
                "suit": "♣️",
                "template": """
                ==============
                # A ♣️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        A ♣️ #
                ==============
                """
            },
            {
                "rank": "A",
                "suit": "♦️",
                "template": """
                ==============
                # A ♦️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        A ♦️ #
                ==============
                """
            },
            {
                "rank": "A",
                "suit": "♥️",
                "template": """
                ==============
                # A ♥️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        A ♥️ #
                ==============
                """
            },
            {
                "rank": "A",
                "suit": "♠️",
                "template": """
                ==============
                # A ♠️        #
                #            #
                #            #
                #            #
                #            #
                #            #
                #        A ♠️ #
                ==============
                """
            }
        ]

        cards = []

        for card_info in card_deck:
            card = Card(**card_info)

            cards.append(card)

        return cards

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        hand_value = 0

        for card in self.hand:
            hand_value += card.get_value()

        return hand_value

    def show_hand(self):
        print(f"{self.name}'s hand: ")
        for card in self.hand:
            print(card.template)

class Dealer(Player):
    def __init__(self, name):
        super().__init__(name)

    def show_partial_hand(self):
        print(f"{self.name}'s partial hand: ")
        if len(self.hand) > 0:
            first_card = self.hand[0]
            print(first_card)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Alex")
        self.dealer = Dealer("Dealer")

    def start_game(self):
        self.deal_initial_cards()
        self.player_turn()
        self.dealer_turn()
        self.check_win()
        self.play_again()

    def deal_initial_cards(self):
        self.deck.shuffle()
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

    def player_turn(self):
        while True:
            self.player.show_hand()
            choice = input("Choice an action: [H]it or [S]tand: ").lower()
            if choice == "h":
                self.player.add_card(self.deck.deal_card())
                if self.player.get_hand_value() > 21:
                    print("Player busts! Dealer wins!!")
                    break
            if choice == "s":
                break

            else:
                print("Invalid chouce! Please, try again.")


    def dealer_turn(self):
        self.dealer.show_partial_hand()
        while self.dealer.get_hand_value() < 17:
            self.dealer.add_card(self.deck.deal_card())

        if self.dealer.get_hand_value() > 21:
            print(f"Dealer busts! Player {self.player.name} wins!!")

    def check_win(self):
        player_hand_value = self.player.get_hand_value()
        dealer_hand_value = self.dealer.get_hand_value()

        if player_hand_value > 21:
            print("Player busts! Dealer wins!!!!!!!!!!!!")
        elif dealer_hand_value > 21:
            print(f"Dealer busts! Player {self.player.name} wins!!!!!!!!!!!!!")
        elif player_hand_value > dealer_hand_value:
            print(f"Player {self.player.name} wins!!!!!!!!!!!!!!!!!!!")
        elif player_hand_value < dealer_hand_value:
            print("Dealer wins!!!!!!!!!!!!!!!!!!!!")
        else:
            print("It's a tie!!!!!!!!!!!")

    def play_again(self):
        choice = input("Do you want to play again? [Y]es or [N]o: ").lower()
        if choice == "y":
            self.player.hand = []
            self.dealer.hand = []
            self.start_game()
        else:
            print("Thank you for playing!!")

game = Game()

game.start_game()
