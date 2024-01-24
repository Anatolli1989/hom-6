# # Task 1
# def calculate_product(lst):
#     product = 1
#
#     for element in lst:
#         product *= element
#
#     return product
#
#
# # Task 2
# def find_minimum(lst):
#     if not lst:
#         return None
#
#     minimum = lst[0]
#
#     for element in lst:
#         if element < minimum:
#             minimum = element
#
#     return minimum
#
#
# # Task 3
# def count_primes(lst):
#     count = 0
#
#     def is_prime(number):
#         if number < 2:
#             return False
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 return False
#         return True
#
#     for element in lst:
#         if is_prime(element):
#             count += 1
#
#     return count
#
#
# # Task 4
# def remove_from_list(lst, number):
#     count_removed = lst.count(number)
#     for _ in range(count_removed):
#         lst.remove(number)
#
#     return count_removed
#
#
# # Task 5
# def merge_lists(list1, list2):
#     merged_list = list1 + list2
#     return merged_list
#
#
# # Task 6
# def calculate_power_of_list(lst, power):
#     powered_list = [element ** power for element in lst]
#     return powered_list
# # Example of using functions:
# list_product = [2, 3, 5]
# result_product = calculate_product(list_product)
# print("Product of elements in the list:", result_product)
#
# list_minimum = [5, 2, 8, 1, 7]
# result_minimum = find_minimum(list_minimum)
# print("Minimum in the list:", result_minimum)
#
# list_primes = [2, 3, 4, 5, 6, 7, 8, 9]
# result_primes = count_primes(list_primes)
# print("Number of prime numbers in the list:", result_primes)
#
# number_to_remove = 3
# count_removals = remove_from_list(list_product, number_to_remove)
# print(f"Number of elements removed from the list: {count_removals}, new list: {list_product}")
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result_merge = merge_lists(list1, list2)
# print("Result of merging lists:", result_merge)
#
# list_powers = [2, 3, 4]
# power = 2
# result_powers = calculate_power_of_list(list_powers, power)
# print(f"Result of raising to the power of {power}:", result_powers)