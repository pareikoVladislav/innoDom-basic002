# 1.1 Жадный алгоритм
# money_variants = {
#     100: 0,
#     50: 0,
#     20: 0,
#     10: 0,
#     5: 0,
#     2: 0,
#     1: 0,
# }
#
# user_withdraw = int(input("How much you want withdraw: "))
#
# try:
#     for denomination in money_variants.keys():
#         while denomination <= user_withdraw > 0:
#             user_withdraw -= denomination
#             money_variants[denomination] += 1
# except ValueError as error:
#     print(error)
#
#
# print(money_variants)


# 1.2 Жадный алгоритм (пример рюкзака)
# def bag_knapsack(items: list, max_weight: int) -> int:  #  [(30, 10), (15, 50), (67, 3)]
#     items.sort(key=lambda x: x[0] / x[1], reverse=True)
#     total_price = 0
#     total_weight = 0
#
#     for item in items:
#         if total_weight + item[1] <= max_weight:
#             total_price += item[0]
#             total_weight += item[1]
#
#         else:
#             remaining_weight = max_weight - total_weight  # Вычислить оставшийся вес, который можно взять
#             fraction = remaining_weight / item[1]  # Вычисление доли предмета, которую мы можем добавить
#             total_price += item[0] * fraction  # Добавление доли стоимости предмета к общей стоимости
#             break
#
#     return total_price
#
#
# items_ = [(60, 10), (100, 20), (120, 30)]
# max_weight_ = 50
#
# result = bag_knapsack(items_, max_weight_)
# print(f"Максимальная стоимость предметов: {result}")


# 2. Рекурсивные алгоритмы (бинарный поиск)
# def binary_search(arr: list, target: int, low: int, high: int) -> int:  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#     if low > high:
#         return - 1
#
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return binary_search(arr, target, low, mid - 1)
#     else:
#         return binary_search(arr, target, mid + 1, high)
#
#
# arr_ = [0, 1, 2, 3, 3, 5, 5, 6, 6, 7, 8, 9, 10]  # 0, 7, 6, 2 - подумать шо за дичь
#
# # arr_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target_ = 3
#
# result = binary_search(arr_, target_, 0, len(arr_) - 1)
# print(f"Индекс элемента {target_} = {result}")


# 3.1 Алгоритмы поиска (линейный поиск)
# def linear_algorythm(array: list, target: str) -> int:  # ["", "", "", "", ...]
#     for index, value in enumerate(array):
#         if value == target:
#             return index
#     return - 1
#
#
# some_list = ["mammy", "daddy", "qwerty", "lower", "dave", "length", "banana", "orange"]
# target_ = "orange"
#
# result = linear_algorythm(some_list, target_)
# print(f"Индекс элемента '{target_}' = {result}")


# 3.2 Алгоритмы поиска (поиск через хэш таблицы)
# def hash_search(hash_table, key):
#     hash_key = hash(key)
#     index = hash_key % len(hash_table)
#
#     if hash_table[index] is not None and hash_table[index][0] == key:
#         return hash_table[index][1]
#     else:
#         return None
#
#
# my_key = 'peach'
# hash_table_ = [None] * 10
# hash_table_[hash('apple') % 10] = ('apple', 'fruit')
# hash_table_[hash('peach') % 10] = ('peach', 'fruit')
# hash_table_[hash('banana') % 10] = ('banana', 'fruit')
# hash_table_[hash('carrot') % 10] = ('carrot', 'vegetable')
#
# result = hash_search(hash_table_, my_key)
# print(f"Значение по ключу '{my_key}' = '{result}'")


# 4.1 Алгоритмы сортировки (сортировка выборкой)
# def selection_sort(arr: list) -> None:
#     for index, value in enumerate(arr):
#         lowest_value_index = index
#
#         for i in range(index + 1, len(arr)):
#             if arr[i] < arr[lowest_value_index]:
#                 lowest_value_index = i
#
#         arr[index], arr[lowest_value_index] = arr[lowest_value_index], arr[index]
#
#
# random_list = [12, 8, 3, 6, 5, 7, 2, 1, 10, 9, 8]
# selection_sort(random_list)
# print(random_list)


# 4.2 Алгоритмы сортировки (сортировка вставками)
# def insertion_sort(arr: list) -> None:
#     for i in range(1, len(arr)):
#         item_to_insert = arr[i]
#         j = i - 1
#
#         while j >= 0 and arr[j] > item_to_insert:
#             arr[j + 1] = arr[j]
#             j -= 1
#
#         arr[j + 1] = item_to_insert
#
#
# random_list_ = [12, 8, 3, 6, 5, 7, 2, 1, 10, 9, 8]
# insertion_sort(random_list_)
# print(random_list_)


# 4.3 Алгоритмы сортировки (быстрая сортировка)
# def quick_sort(array: list) -> list:
#     if len(array) <= 1:
#         return array
#
#     else:
#         pivot = array[0]
#         less = [x for x in array[1:] if x <= pivot]
#         grater = [x for x in array[1:] if x > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(grater)
#
#
# print(quick_sort([12, 8, 3, 6, 5, 7, 2, 1, 10, 9, 8]))

# 4.4 Алгоритмы сортировки (пузырьковая сортировка)
# def bubble_sort(nums: list) -> None:
#     swapped = True
#
#     while swapped:
#         swapped = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 swapped = True
#
#
# random_list = [32, 1, 75, 70, 42, 56, 74, 91, 101]
# bubble_sort(random_list)
# print(random_list)

# 6 Алгоритмы шифрования (шифр Цезаря)
def cesar_algorythm(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            new_char = chr(ord(char.lower()) + shift)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char

    return result


encrypted_text = cesar_algorythm(input("Enter your secret message: "), 2)
decrypted_text = cesar_algorythm(encrypted_text, -2)

print(encrypted_text)
print("~" * 45)
print(decrypted_text)

