from typing import Optional
from constants import ABILITIES

def give_int(input_number:  str,
            min_num: Optional[int] = None,
            max_num: Optional[int] = None) -> int:
    '''
    Функция ввода числа
    '''
    while True:
        try:
            num = int(input(input_number)) 
            if min_num and num < min_num:
                print(f'Введите число больше или равно: {min_num}')
                continue  
            if max_num and num > max_num:
                print(f'Введите число меньше или равно: {max_num}')
                continue 
            return num
        except ValueError:
            print('Вы ввели не число. Введите число.')

def menu_select():
    '''
    Функция выбора меню
    '''
    start_text = 'Выберите режим калькулятора: '
    
    for i, item in list(enumerate(ABILITIES, start = 1)):
        print(i, item, end= '\n')
    choise = give_int(start_text, 1, 3)
    return choise

def give_int_2(input_number) -> float:
    '''
    Функция ввода числа
    '''
    while True:
        try:
            num = float(input(input_number))  
            return num
        except ValueError:
            print('Вы ввели не число. Введите число.')
