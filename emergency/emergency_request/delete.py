# from rest_framework import serializers
#
#
# def validate_snils(value: str) -> str:
#     value = value.replace(' ', '')
#     if not value.isnumeric():
#         raise serializers.ValidationError('СНИЛС может состоять только из цифр')
#     elif len(value) != 11:
#         raise serializers.ValidationError('СНИЛС может состоять только из одиннадцати цифр')
#     for i in range(len(value) - 4):
#         if len(set(value[i:i + 3])) == 1:
#             raise serializers.ValidationError('СНИЛС не может содержать три одинаковые цифры подряд')
#
#     value_sum = sum(int(n) * (9 - i) for i, n in enumerate(value) if i < 9)
#
#     check_number = 0
#     if value_sum < 100:
#         check_number = value_sum
#     elif value_sum in (100, 101):
#         check_number = 0
#     elif value_sum > 101:
#         check_number = value_sum % 101
#         if check_number == 100:
#             check_number = 0
#
#     if check_number != int(value[-2:]):
#         raise serializers.ValidationError('Введён некорректный СНИЛС')
#
#     return check_number = int(value[-2:])
#
#
#
# print(validate_snils('757 274 741 43'))

# @cache sdfs
def fn(*args):
    arr = []
    for i in args:
        if i not in arr:
            arr.append(i)
            print(arr)
        else:
            print(i, 'Уже было')


fn(3, 2, 8, 3, 2, 3, 8, 9)
