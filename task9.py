"""
Напишите программу, в которой описана функция, возвращающая ре-
зультатом второе по величине число в списке, переданном функции в ка-
честве аргумента.
"""

sample_list = [4, 72, 15, 46, 94, 45, 88, 99]


def second_max(any_list):
    sorted_revere_list = sorted(any_list, reverse=True)
    return sorted_revere_list[1]

print(second_max(sample_list))