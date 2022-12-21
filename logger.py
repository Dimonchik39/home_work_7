from datetime import datetime as dt


def calc_logger(data):
    '''
    Функция записи логов в файл
    '''
    time = dt.now().strftime('%d.%m.%Y.%H.%M')
    with open('cal_log.log', 'a') as file:
        file.write('\n{};Результат: {}'
            .format(time, data))