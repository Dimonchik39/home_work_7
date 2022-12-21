import functions as fu
import logger as log

def work_calc():
    x = fu.give_int_2('Введите первое число: ')
    y = fu.give_int_2('Введите второе число: ')
    oper = oper_choice()
    result = sim_cal(x, y, oper)
    expression = (f'{x} {oper} {y} = {result}')
    log.calc_logger(expression)
    print(expression)

def oper_choice():
    text = '''
    Список символов:

    + : сложение
    - : вычитание
    / : деление
    * : умножение

    Выберите символ операции:
    '''
    operation = input(text)
    if operation == '+':
        return operation
    elif operation == '-':
        return operation
    elif operation == '/':
        return operation
    elif operation == '*':
        return operation
    else:
        print('Попробуйте заново. Калькулятор поддерживает: +, -, /, *')
        exit()

def sim_cal(x, y, oper):
    result = None
    try:
        if oper == '+':
            result = (x + y)
        elif oper == '-':
            result = (x - y)
        elif oper == '/':
            result = (x / y)
        elif oper == '*':
            result = (x * y)
    except ZeroDivisionError:
        print('Деление на 0 не поддерживается. Попробуйте заново.')
        exit()

    return result
