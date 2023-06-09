# -*- coding: utf-8 -*-
"""innoDom_lesson_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18sgf9VmKWsqwVrBuOZhZ0WqCBTbxd980

# **Операторы сравнения**

**Операторами сравнения** называются операторы, которые сравнивают между собой два значения и возвращающие результат типа bool ( True \ False ).

Сравнивать между собой мы можем:
* Логический тип ( bool )
* Строки
* Числа
* Переменные на наличие пустоты

Какие операторы сравнения бывают:
* `>` - Проверяет, больше ли левое выражение. Если да - True, если нет - False
* `<` - Проверяет, меньше ли левое выражение. Если да - True, если нет - False
* `>=`- Проверяет, больше или равно левое выражение относительно правого. Если да - True, если нет - False
* `<=` - Проверяет, меньше или равно левое выражение относительно правого. Если да - True, если нет - False
* `==` - Проверяет равны ли выражения. Если да - True, если нет - False
* `!=` - Проверяет равны ли выражения. Если нет - True, если да - False

Разберём примеры со всеми этими операторами:
"""

print(ord("A"), ord("a"))
print(chr(97), chr(65))

print(5 > 3)

True == False

print(.1 > 1.)

print(-10 != -1)

print("abc" > "abcd")

print(["A", "b", "c"] > ["a", "B", "c"])

print(1 in [1, 2, 3])
a = 3
b = a
print(b is a)
print("a" in {"a": 1, "b": 2, "c": 3})

print(len((1, 2, [1, 2, 3])) == 3 and 3 in (1, 2, [1, 2, 3]))

print(True > False and False == True)

print(True == 1 or (False > True and False == 0))

"""**Логические операторы:**

**Логические операторы** используются для выполнения логических операций, таких как сравнение значений и комбинирование условий.
Какие операторы у нас имеются:

* `not` - Логический оператор "не"
* `and` - логическое "И". Используется, когда нам нужно проверить несколько значений сразу. Логическое "И" запинается на лжи ( если хоть одно из условий False, вернёт False. Если оба значения False, просто вернёт последнее значение False )
* `or` - Логическое "Или". Так же используется, когда нам нужно проверить несколько значений сразу. Логическое "Или" запинается на правде ( если хоть одно из значений True - вернёт True. Если оба значения True, или False - вернёт последнее значение )

Где мы можем применять эти операторы:

* **Условные операторы:** часто используются в условных операторах, таких как `if`, `elif` и `else`, для проверки условий и принятия решений на основе результата. 

* **Циклы:** также наши операторы могут использоваться в циклах, таких как `while` и `for`, для проверки условий продолжения выполнения цикла.

* **Функции и выражения:** Логические операторы также могут использоваться в функциях и выражениях для создания булевых (логических) значений. Например, операторы `and`, `or` и `not` могут быть использованы для комбинирования и инвертирования булевых значений и выполнения различных операций на основе этих значений.

* **Индексирование и нарезка:** создание булевых массивов для индексирования или нарезки массивов данных. Например, мы можем создать булевый массив, содержащий результаты сравнения элементов другого массива с определенным условием, и затем использовать этот массив для выборки или модификации данных.
"""

print([1, 2, 3] == [1, 2, 3] and 3 in [1, 2, 3])

"""**Операторы принадлежности:**

Операторы принадлежности в Python используются в различных контекстах для проверки условий

* `is` - используется для проверки, указывает ли один объект на тот же участок памяти, что и другой объект. Он сравнивает идентичность объектов, а не их значения.
* `in` - Проверяет, принадлежность элемента `x` к последовательности \ коллекции (Находится ли подстрока в общей строке, находится ли какой-то ключ в словаре и т.д.)
* `not in` - является отрицанием оператора `in`. Он используется для проверки отсутствия элемента в коллекции или последовательности. Он возвращает True, если элемент отсутствует, и False в противном случае.


Операторы `is`, `in` и `not in` позволяют выполнять проверки на идентичность объектов и принадлежность элементов к коллекциям или последовательностям в Python:
"""

a = 15
b = a
b = 10

print(a)
print(id(a))

print(b)
print(id(b))

print(b is a)

b = 10

str_1 = "qwerty"

print("rty" in str_1)

# []
# ()
# {"":""}

# list_1 = ["1", [1, 2, 3], 45]

# print(2 not in list_1)
# tuple_1 = (1, 2, "4", "abc", (1, 2, 3))
# print("abc" in tuple_1)
dict_1 = {
    "a": 1,
    "b": 2,
    "c": 3,
}
print("a" in dict_1 and dict_1.get("a") == 1)

"""# **Операторы ветвлений**

**Операторы ветвлений** используются для принятия решений в программе на основе условий. Они позволяют программе выполнить определенные блоки кода только при выполнении определенных условий, что делает программу более гибкой и адаптивной.


Они могут встречаться в различных областях разработки, вот несколько примеров:

* **Управление потоком программы**: Операторы ветвления позволяют контролировать поток выполнения программы, определяя, какие части кода будут выполнены в зависимости от условий. Например, в зависимости от значения переменной можно выполнить определенные действия или перейти к другому блоку кода.

* **Обработка ошибок**: Так же можно использовать наши операторы для обработки исключений и ошибок в программе. Они позволяют определить, какая часть кода будет выполнена при возникновении определенной ошибки, и принять соответствующие меры для ее обработки.

* **Валидация пользовательского ввода**: проверка и валидация введенных пользователем данных. Например, мы можем проверить, является ли введенное значение числом или строкой, и выполнить различные действия в зависимости от результата.


По ветвлениям мы можем выделить две основные группы наших операторов:

* Условные операторы
* Обработчики ошибок

Давайте по порядку

**Условные операторы:**

* `if` - позволяет выполнить определенный набор инструкций в зависимости от некоторого условия. Если условие верно, выполняется блок кода, который определён внутри этого условия. Иначе этот блок кода пропустится.

Как это работает:

```
if условие:
    инструкция_1
    инструкция_2
    ...
    инструкция_n
```

После оператора `if` записывается выражение. Если это выражение истинно, то выполняются инструкции, определяемые данным оператором. Выражение является истинным, если его результатом является число не равное нулю, непустой объект, либо логическое True. После выражения нужно поставить двоеточие “:”
"""

user_input = int(input("Enter the number: "))

if user_input and user_input <= 10:
  print(user_input * 2)

"""* `if – else` - Используется для выполнения одного блока кода, если условие истинно, и другого блока кода, если условие ложно.

Бывают случаи, когда необходимо предусмотреть альтернативный вариант выполнения программы. Т.е. при истинном условии нужно выполнить один набор инструкций, при ложном – другой. Для этого используется конструкция `if – else`.

```
if выражение:
    инструкция_1
    инструкция_2
    ...
    инструкция_n
else:
    инструкция_a
    инструкция_b
    ...
    инструкция_x
```

Условие такого вида можно записать в строчку, в таком случае оно будет представлять собой [тернарное выражение](https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%80%D0%BD%D0%B0%D1%80%D0%BD%D0%B0%D1%8F_%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0%D1%8F_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F).

```
b = True if 15 > 10 else False
print(b)
```
"""

user_input_1 = int(input("Enter the number: "))

if user_input_1 and user_input_1 <= 10:
  print(user_input_1 ** 2)
else:
  print("Something went wrong")

b = "a" if 15 < 10 else "b" # тернарный оператор
print(b)

"""* `if – elif – else` - Можно использовать для реализации выбора из нескольких альтернатив

```
a = int(input("введите число:"))
if a < 0:
   print("Neg")
elif a == 0:
   print("Zero")
else:
   print("Pos")
```
"""

a = int(input("введите число:"))
if a < 0:
   print("Neg")
elif a == 0:
   print("Zero")
else:
   print("Pos")

user_name = input("Enter your username: ")
user_password = input("Enter your password: ")

if user_name and user_password:
  if len(user_password) > 10 and user_password.isalnum():
    print(f"Hello, {user_name}! You're in system!")
  elif user_password.isalpha() or user_password.isdecimal():
    print("Your password is too weak")
  elif len(user_password) <= 10:
    print("Your password is too short")
  else:
    print("Your password must contains only a letters and numbers")
elif user_name:
  print("The 'password' field must specified, please provide your password")
elif user_password:
  print("The 'username' field must specified, please provide your username")
else:
  print("You don't enter anything, please provide your 'sign in' info")

"""**Обработчики исключений**

Исключениями (exceptions) в языках программирования называют
проблемы, возникающие в ходе выполнения программы. Типичным
примером исключения является деление на ноль, попытка вычислений между разными типами данных, невозможность считать данные из устройства, отсутствие доступной памяти, доступ к закрытой области памяти и т.п.

Для обработки таких ситуаций, как правило, предусматривается
специальный механизм, который как раз и называется **обработка исключений**.


Такая конструкция определяется как `try - expect`
"""

a = [1, 2, 3]

try:
  print(a / 8)
except TypeError:
  print("На ноль делить нельзя, тапочек!!!!!!!!!!!")

"""Рассмотрим иерархию встроенных в python исключений, хотя иногда вам могут встретиться и другие, так как программисты могут создавать собственные исключения. Данный список актуален для python `3.3` и выше, в более ранних версиях есть незначительные изменения:


* `BaseException` - базовое исключение, от которого берут начало все остальные.
  * `SystemExit` - исключение, порождаемое функцией `sys.exit` при выходе из программы.
  * `KeyboardInterrupt` - порождается при прерывании программы пользователем (обычно сочетанием клавиш `Ctrl+C`).
  * `GeneratorExit` - порождается при вызове метода close объекта generator.
  * `Exception` - а вот тут уже заканчиваются полностью системные исключения (которые лучше не трогать) и начинаются обыкновенные, с которыми можно работать.
    * `StopIteration` - порождается встроенной функцией next, если в итераторе больше нет элементов.
    * `ArithmeticError` - арифметическая ошибка.
      * `FloatingPointError` - порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.
      * `OverflowError` - возникает, когда результат арифметической операции слишком велик для представления. Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа), но может возникать в некоторых других случаях.
      * `ZeroDivisionError` - деление на ноль.
    * `AssertionError` - выражение в функции assert ложно.
    * `AttributeError` - объект не имеет данного атрибута (значения или метода).
    * `BufferError` - операция, связанная с буфером, не может быть выполнена.
    * `EOFError` - функция наткнулась на конец файла и не смогла прочитать то, что хотела.
    * `ImportError` - не удалось импортирование модуля или его атрибута.
    * `LookupError` - некорректный индекс или ключ.
      * `IndexError` - индекс не входит в диапазон элементов.
      * `KeyError` - несуществующий ключ (в словаре, множестве или другом объекте).
    * `MemoryError` - недостаточно памяти.
    * `NameError` - не найдено переменной с таким именем.
      * `UnboundLocalError` - сделана ссылка на локальную переменную в функции, но переменная не определена ранее.
    * `OSError` - ошибка, связанная с системой.
      * `BlockingIOError`
      * `ChildProcessError` - неудача при операции с дочерним процессом.
      * `ConnectionError` - базовый класс для исключений, связанных с подключениями.
        * `BrokenPipeError`
        * `ConnectionAbortedError`
        * `ConnectionRefusedError`
        * `ConnectionResetError`
      * `FileExistsError` - попытка создания файла или директории, которая уже существует.
      * `FileNotFoundError` - файл или директория не существует.
      * `InterruptedError` - системный вызов прерван входящим сигналом.
      * `IsADirectoryError` - ожидался файл, но это директория.
      * `NotADirectoryError` - ожидалась директория, но это файл.
      * `PermissionError` - не хватает прав доступа.
      * `ProcessLookupError` - указанного процесса не существует.
      * `TimeoutError` - закончилось время ожидания.
    * `ReferenceError` - попытка доступа к атрибуту со слабой ссылкой.
    * `RuntimeError` - возникает, когда исключение не попадает ни под одну из других категорий.
    * `NotImplementedError` - возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
    * `SyntaxError` - синтаксическая ошибка.
      * `IndentationError` - неправильные отступы.
        * `TabError` - смешивание в отступах табуляции и пробелов.
    * `SystemError` - внутренняя ошибка.
    * `TypeError` - операция применена к объекту несоответствующего типа.
    * `ValueError` - функция получает аргумент правильного типа, но некорректного значения.
    * `UnicodeError` - ошибка, связанная с кодированием / раскодированием unicode в строках.
      * `UnicodeEncodeError` - исключение, связанное с кодированием unicode.
      * `UnicodeDecodeError` - исключение, связанное с декодированием unicode.
      * `UnicodeTranslateError` - исключение, связанное с переводом unicode.
    * `Warning` - предупреждение.

Как это всё может выглядить и каков порядок?


```
>>> try:
...     k = 1 / 0
... except ZeroDivisionError:
...     print("You can't divide numbers by zero")
...
>>> You can't divide numbers by zero
```

В блоке `try` мы выполняем инструкцию, которая может породить исключение, а в блоке `except` мы перехватываем их. При этом перехватываются как само исключение, так и его потомки. Например, перехватывая `ArithmeticError`, мы также перехватываем `FloatingPointError`, `OverflowError` и `ZeroDivisionError`

Также возможна инструкция `except` без аргументов, которая перехватывает вообще всё (и прерывание с клавиатуры, и системный выход и т. д.). Но в такой форме инструкция `except` практически не используется, потому что у вас не будет никакой конкретики какой конкретно природы ошибку поймал ваш обработчик. Вместо этого используется `except Exception`. Однако чаще всего перехватывают исключения по одному, для упрощения отладки (вдруг вы ещё другую ошибку сделаете, а `except` её перехватит)
"""

try:
  k = 10 / 0
except ZeroDivisionError:
  print("qwerty")
except TypeError:
  5 + 5
except Exception:

"""Ещё две инструкции, относящиеся к нашей проблеме, это `finally` и `else`. `Finally` выполняет блок инструкций **в любом случае**, было ли исключение, или нет (применима, когда нужно непременно что-то сделать, к примеру, закрыть файл). Инструкция `else` выполняется в том случае, если исключения не было."""

try:
  user_input = int(input("Enter any number: "))
  a = user_input ** 2
  print(a)
except Exception:
  print("Переменная 'user_input' - не число. Выходим.")
else:
  print(f"Всё хорошо, результат = {a}")
finally:
  print('Я всегда выполнюсь в конце, пока!')
# Именно в таком порядке: try, группа except, затем else, и только потом finally.

"""# **Домашка**

1. **Калькулятор:**

Пользователь должен ввести тры значения:

1) Одно число

2) Второе число

3) Тип операции между числами


* В зависимости от того, что ввёл пользователь произвести тот, или иной тип мат. операции.
* Отработать предполагаемые ошибки со стороны пользователя (Некорректный ввод \ деление на 0 и т.д.)

2. **Вёдра:**

У вас есть два ведра, ёмкостью в 5 литров и 3 литра.
Так же у вас есть неограниченный запас воды.
Вам нужно отмерить ровно 4 литра.

  * Вы можете наливать воду в оба ведра
  * Вы можете выливать воду из двух этих вёдер
  * Вы можете переливать воду из одного ведра в другое
  * Вы НЕ можете выливать, или переливать воду из вёдер частями.
  Или всё, или ничего.

3. **Улучшите вашу задачу с вёдрами**

Добавьте в задачу обработчики ошибок `try expect`.

Предусмотрите различные варианты ввода информации от "пользователя", чтобы максимально предотвратить сбой вашего кода.
"""

