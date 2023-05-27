# -*- coding: utf-8 -*-
"""innoDom_lesson_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c6664lcuQYYnL0AJn2ky4RebXC58ORW1

# **Циклы**

Что у нас за циклы такие в целом. Зачем они нам нужны?

Самый банальный пример: представьте, что у вас стоит задача выводить какое-то значение определённое количество раз. Вместо того, чтобы писать это значение много раз подряд на каждой строке - можно запихнуть вывод этого значения в цикл с определённым количеством длинны (функция range()) и запустить этот цикл.
Или же вам нужно пройтись по каждому элементу в каком-то объекте и что-то сделать с этим элементом.

Для таких штук у нас с вами существуют циклы, чтобы вам, как разработчикам не пришлось делать это всё ручками десятки\сотни\тысячи раз.

Наши с вами циклы позволяют выполнять повторяющиеся операции или блоки кода. Они позволяют автоматизировать задачи, которые требуют повторного выполнения одного и того же действия. Вместо того, чтобы писать одну и ту же команду несколько раз, мы можем использовать циклы, чтобы выполнить эту команду множество раз, сокращая тем самым объем кода и повышая эффективность программы.
"""

# for (var i = 0, i <= 10, i++) { # JS
#     console.log("Hello World!")
# }
# for <локальная переменная> in <итерируемый объект>:
    #<блок кода>
for i in range(1, 11):
  print(f"Hello, World! ------- {i}")

"""**Немного общих понятий:**

`Цикл`- это процесс повторения какого-либо действия или обход по какомунибудь итерированному объекту.

`Итерируемый объект` – это объект, у которого можно брать элементы по одному (строки, списки, кортежи, множества, словари и др).

`Итерация` - это шаг или организация обработки данных, таким образом, когда действие происходит многократно.

**Области применения наших циклов:**

* `Обработка итерируемых объектов:` Циклы позволяют проходить по элементам итерируемых объектов, таких как списки, кортежи, строки и словари, и выполнять некоторые действия для каждого элемента.
"""

string = "qwertyui"

# для буквы в строке:
for letter in string:
  print(f"The iteration number: {string.index(letter) + 1}, the 'letter' value: {letter}")

# отделить все символы от букв
some_string = "njk23@&#^masndi0u132wa}dda<nuj*>?gb?gasd?"

only_symbols = []
onlny_letters = []

for symbol in some_string:
  if symbol.isalpha():
    onlny_letters.append(symbol)
  else:
    only_symbols.append(symbol)

print("".join(only_symbols))
print("".join(onlny_letters))

"""* `Выполнение блока кода заданное количество раз:` Циклы могут быть использованы для выполнения определенного блока кода заданное количество раз. Например, когда нам нужно повторить операцию 10 раз или пока не будет выполнено определенное условие."""

# построить треугольник
spec_symbol = "*"

for i in range(1, 6):
  print(spec_symbol * i)

# построить пирамидку
spec_symbol = "*"

for i in range(5):
    print(' ' * (5 - i - 1) + spec_symbol * (2 * i + 1))

some_value = 5

for i in range(1, 6):
  print(some_value ** i)

"""* `Обработка данных:` Циклы позволяют нам обрабатывать данные, вводимые пользователем, из файла или полученные из другого источника."""

# посчитать сумму чисел или выйти при вводе любой боквы\строки
summary = 0 # 5 10 15

while True: # пока условие истино
  user_input = input("Enter some value: ")
  if user_input.isalpha():
    break
  summary += int(user_input)

print(f"The sum of the user's inputs = {summary}")

"""**Разновидности циклов и их отличия**

В целом у нас таки два вида циклов:
* `for`:
  * Срабатывающий **определенное** количество раз
  * Есть параметром
  * Известное количество итераций


* `while`:
  * работает по какому-то условию
  * неизвестное количество итераций (пока условие верно цикл будет выполняться)

# **FOR**

Наш цикл **for** работает с итерируемыми объектами.
Для того, чтобы создать наш с вами цикл, используется следующая конструкция:
"""

for i in <iterable_object>:
  "your code block"

"""Где:
* `for` - определение того, что сейчас будет цикл
* `i` - локальная переменная, которая создаётся для хранения значения из объекта на каждой итерации. Каждую след итерацию в этой переменной храниться обновлённое значение.
* `in` - говорит нашему циклу, по какому объекту мы будем проходиться этим самым циклом (в рамках какого объекта будет работать цикл)
* `<iterable_object>` - объект, по которому мы будем проходиться и что-то с ним делать.
* `"your code block"` - блок кода, в котором будут происходить какие-то манипуляции со значениями из объекта

Наша локальная переменная `i` в рамках нашего цикла может обзываться как угодно. Общепринято называть эту переменную логически подвязаной к нашему итерируемому объекту
"""

some_unique_values = {321, 512, 542, 545, 454, 873, 112, 723}

ids_copy = some_unique_values.copy()

for id in ids_copy:
  ids_copy.discard(id)
  ids_copy.add(str(id))

ids_copy

some_unique_values

"""Обход циклом по таким коллекциям, как списки, строки, кортежи и множества очень похож друг на друга. А вот со словарями уже всё более интересно. Там мы можем пройтись циклом просто по словарю. В таком случае по дефолту мы будем проходиться по ключам нашего словаря:"""

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

for elem in my_dict:
  print(elem)

# for key, value in my_dict: получите в лицо ошибку, связанную с распоковкой ваших значений из словаря
#   print(key, value)

"""Так же мы можем проходиться только по ключам:"""

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

for key in my_dict.keys():
  print(key)

"""Только по значениям ключей:"""

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

for value in my_dict.values():
  print(value)

"""И по цельным парам - ключ: значение:"""

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}
#w [('a', 1), ('b', 2), ('c', 3)]
for key, value in my_dict.items():
  print(key, value)

print(my_dict.items())

"""Так же бывают моменты, когда нам не нужно проходиться циклом по какому-то объекту, а просто сделать какое-то действие несколько раз подряд. В таком случае мы можем передавать в цикл просто объект range():"""

for _ in range(1, 11):
  print("Some really needed info")

"""Мы можем так же сделать своего рода имитацию загрузки:"""

# имитация загрузки

import time
import sys

total = 50
delay = 0.2

for i in range(total + 1):
  percent = i * 100 / total
  progress = "#" * i
  sys.stdout.write(f"Loading process: [{progress}] {percent:.1f}%")
  sys.stdout.flush()
  time.sleep(delay)
  sys.stdout.write("\r")

"""# **While**

Некоторые же задачи сложно выполнять просто через цикл for, даже с учётом различных проверок. Для этого существует цикл while.

Как этот цикл устроен, какой цикл и так далее:

Из самого названия можно предположить, что итерация цикла у нас проходит только при выполнении какого-то условия
"""

counter = 0
while counter < 5:
  print("Here we go again")

  counter += 1

"""Как это можно всё прочесть:

* `counter` - специальная переменная счётчик, отвечающая за то, чтобы наш цикл не стал бесконечным
* `while` - ключевое слово цикла
* `<condition>` - спец условие, которое будет проверяться на True перед проходом каждой итерации
* `<body>` - собственно ваш код, который будет выполняться в случае, если ваше условие будет True

Переменная counter не всегда должна быть. В целом наш цикл while должен быть написан так, чтобы в нём предусматривался выход из цикла. Если мы не предусмотрим никаких выходов из цикла, чтобы наше условие не проходило проверку на True - мы получим бесконечный цикл, а это плохо.
"""

# угадай число
import random

number = random.randint(1, 4)
user_input = int(input("Enter tha random value from 1 to 3: "))
counter = 1

while user_input != number:
  print("Число неверное, попробуй ещё раз.")
  user_input = int(input("Enter tha random value from 1 to 3: "))
  counter += 1

print(f"Поздравляю! Вы угадали число {number} за {counter} раз(а)")

"""**Циклы и индексы**

Помимо обхода итеративных объектов через цикл for, можно ещё
использовать обход по индексам
"""

my_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for item in range(0, len(my_list)):
  print(my_list[item])

"""Такие ситуации спасают, когда нужно работать с соседними от индекса `i`элементами в списке."""

my_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for item in range(0, len(my_list) - 1, 1):
  print(my_list[item], my_list[item + 1], sep="\t")

"""Так же благодаря индексам можно обойти цикл в обратном порядке:"""

my_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for item in range(len(my_list) - 1, -1, -1):
  print(my_list[item])

# или использовать метод списка reversed():
for item in reversed(my_list):
  print(item)

"""# **Операторы break и continue**

В любой момент выполнения программы, при определённом условии,
можно пропустить текущую итерацию, для используется оператор
`continue`.
Чтобы закончить выполнение цикла, используется оператор `break`.

Например когда ваша локальная переменная принимает нужное вам значение и дальше вам не нужно выполнять цикл.
"""

store_list = ["Milk", "Butter", "Water", "Meat", "Apples", "engine", "Juice"]

for product in store_list:
  if product == "engine":
    print("This is not store product")
    break
  else:
    print(product)

"""И похожая логика работы у нас с оператором `continue`, только он не прерывает работу цикла, а просто пропускает текущую итерацию и сразу идёт на следующую:"""

store_list = ["Milk", "Butter", "Water", "Meat", "engine", "Apples", "Juice"]

for product in store_list:
  if product == "engine":
    print("This is not store product")
    continue
  else:
    print(product)

"""Собственно так же эти операторы работают и с циклом while:"""

counter = 0

while True:
  if counter < 7:
    print("It works")
  else:
    break

  counter += 1

"""# **Операторы else в циклах**

Да, в циклах тоже есть `else`. Он используется для реализации действий в конце цикла, после последней итерации:
"""

for i in range(0, 4):
  print("Hello")
else:
  print("Bye")

some_string = "У в%%А№с вввв@c~ё ппп$$ПО&л%у**Ч**<>и!тс::я}"
symbols = ("%", "№", "@", "~", "$", "&", "*", "<", ">", "!", ":")

for elem in some_string:
  if elem in symbols:
    continue
  if elem == "}":
    break
  else:
    print(elem.lower(), end="")
else:
  print("\nThe cycle was ended")

"""Вы так же можете создавать вложенные циклы, если ваш объект имеет вложенную структуру (список со списками)"""

some_values = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9], [9, 10, 11]]
new_list = []

for value in some_values:
  for num in value:
    new_list.append(num ** 2)

print(new_list)

size = 6  # Размер доски (8х8)

for row in range(size):
    for col in range(size):
        if (row + col) % 2 == 0:
            print("⬛️", end="")  # Черные клетки
        else:
            print("⬜️", end="")  # Белые клетки
    print()  # Переход на новую строку

# обработка заказов из интернет магазина
orders = [
    [1, "2023-05-15", ["Product A", "Product B"], "In Progress"],
    [2, "2023-05-16", ["Product C"], "Completed"],
    [3, "2023-05-17", ["Product D", "Product E", "Product F"], "Pending"]
]

for order in orders:
  order_id = order[0]
  order_date = order[1]
  orders_list = order[2]
  order_status = order[3]

  print(f"Order ID: {order_id}")
  print(f"Order date: {order_date}")
  print(f"Order Items:")
  for item in orders_list:
    print(f" - {item}")
  print(f"Order status: {order_status}")

"""# **Homework**

1. Есть список с объектами в виде учеников:

```
university_students = [
    {
        "name": "Alex",
        "age": 19,
        "sex": "man",
        "facultet": "math"
    },
    {
        "name": "Ban",
        "age": 18,
        "sex": "man",
        "facultet": "math"
    },
    {
        "name": "Chloe",
        "age": 22,
        "sex": "woman",
        "facultet": "physics"
    },
    {
        "name": "Sasha",
        "age": 21,
        "sex": "woman",
        "facultet": "pcyology"
    },
    {
        "name": "Adam",
        "age": 27,
        "sex": "man",
        "facultet": "biology"
    },
    {
        "name": "Lesya",
        "age": 21,
        "sex": "woman",
        "facultet": "pcyology"
    },
    {
        "name": "Linda",
        "age": 23,
        "sex": "woman",
        "facultet": "geography"
    },

]
```
* Вывести всех студентов мужского пола и женского пола отдельно. Посчитать их количество(сколько парней и сколько девушек)
* Вывести всех старше 20-ти лет
* Вывести только тех студентов, кто учится на математическом факультете

2. Факториал числа
* Пользователь должен ввести с клавиатуры положительное, целое число `n` 
* Нужно написать програму, которая будет вычислять факториал(произведение всех целых чисел от 1 до n) этого числа.
* Не забывайте ставить какие-нибудь проверки "на дуркака"(если пользователь хочет ввести строку\ничего\пробел)
* Вывести полученный результат на экран.

3. Последовательность фибоначи
* Пользователь должен ввести с клавиатуры положительное, целое число `n`
* Написать код, который находит n-ое число в последовательности Фибоначчи. ( Последовательность Фибоначчи начинается с чисел 0 и 1, а каждое последующее число получается путем сложения двух предыдущих)
* Не забываем проверки "на дурака"
* Вывести полученный результат на экран.
"""

