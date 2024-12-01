
# Задание 1

def sort_students_by_grade(students):
    return sorted(students, key=lambda x: x[1], reverse=True)

students = [("Света", 52), ("Лена", 228), ("Вика", 220), ("Вераника", 66), ("Рудольф", 546)]
sorted_students = sort_students_by_grade(students)
print(sorted_students)

# Задание 2

def min_elements_of_tuples(tuple1, tuple2):
    return tuple(min(a, b) for a, b in zip(tuple1, tuple2))

tuple1 = (5, 10, 15)
tuple2 = (3, 12, 8)
result = min_elements_of_tuples(tuple1, tuple2)
print(result)

# Задание 3 

def count_unique_elements(numbers):
    return len(set(numbers))

# Пример использования:
numbers = (1, 2, 2, 3, 4, 4, 4, 5)
unique_count = count_unique_elements(numbers)
print(f"Количество уникальных элементов: {unique_count}")

# Задание 4

def filter_even_numbers(numbers):
    return tuple(filter(lambda x: x % 2 == 0, numbers))

# Пример использования:
numbers = (4, 1, 13, 7, 8, 66, 52, 228)
even_numbers = filter_even_numbers(numbers)
print(even_numbers)

# Задание 5

def sum_of_squares(numbers):
    squares = tuple(x ** 2 for x in numbers)
    return squares, sum(squares)

# Пример использования:
numbers = (5, 8, 7, 9)
squares, total_sum = sum_of_squares(numbers)
print(f"Новый кортеж: {squares}")
print(f"Сумма: {total_sum}")
