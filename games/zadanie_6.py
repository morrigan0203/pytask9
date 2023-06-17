

from zadanie_2 import deco as d2
from zadanie_3 import deco as d1
from zadanie_4 import count

@count(3)
@d1
@d2
def two_numbers(count_try: int, num: int):
    """Пользователь должен угадать заганное число с нескольких попыток"""
    print(count_try, num)
    for i in range(1, count_try + 1):
        user_input = input('Введите число для отгадывания от 1 до 100 : ')
        if int(user_input) == num:
            print(f'Вы угадали с {i} попытки')
            #break
            return True
    else:
        print('Вы не угадали')
    return False


if __name__ == '__main__':
    help(two_numbers)
    #res = two_numbers(30, 200)

