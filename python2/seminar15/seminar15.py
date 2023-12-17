'''
1. Решить 6 задачу из семинара.
    Напишите программу-банкомат
    ** Начальная сумма равна нулю.
    ** Допустимые действия: пополнить, снять, выйти.
    ** Суммы пополнения и снятия кратна 50 у.е.
    ** Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
    ** После каждой третьей операции пополнения или снятия начисляются проценты - 3%.
    ** Нельзя снять больше, чем на счете.
    ** При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной.
    ** Любое действие выводит сумму денег.

'''
import logging
import argparse

def create_logger(loglevel):
    logging.basicConfig(filename='bankomat.log', filemode='a', encoding='utf-8',
                             format=LOGFORMAT, style='{', level=loglevel)
    return logging.getLogger('Программа-банкомат')

cash :float = 0.0
EXIT_SYMBOL = '0'
cash_operation :int = 0
KRATNO = 50
CASH_OUT_TAX = 0.015
CASH_OUT_MIN_TAX_VALUE = 30
CASH_OUT_MAX_TAX_VALUE = 600
CASH_LIMIT = 5000000
CASH_LIMIT_TAX = 0.1
operation_count = 0
OPERATION_COUNT_NUM = 3
OPERATION_COUNT_INC = 0.03
LOGFORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
        'в строке {lineno:03d} функция "{funcName}()" ' \
        'Cообщение: {msg}'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Программа-банкомат')
    parser.add_argument('-l', metavar='loglevel', type=int, help='укажите уровень логирования от 1 до 5:\n'
                        '1 - DEBUG, 2 - INFO, 3 - WARNING, 4 - ERROR, 5 - CRITICAL', default=2)
    parser.add_argument('-c', metavar='start_cash_value', type=float, help='укажите количество наличных в банкомате от 0 до 10000000', default=0)
    args = parser.parse_args()
    if 1 <= args.l <= 5:
        logger = create_logger(int(args.l * 10))
        logger.info(f'Запуск программы с параметрами: {args}')
    else:
        logger = create_logger(logging.ERROR)
        msg=f'Ошибка задания уровня логирования, допустимые значения от 1 до 5, задано значение {args.l}'
        logger.error(msg)
        print(msg)
        exit(1)

    if 0 <= args.c <= 10000000:
        cash = args.c
    else:
        msg=f'Ошибка задания начальной суммы, допустимые значения от 0 до 10000000, задано значение {args.c}'
        logger.error(msg)
        print(msg)
        exit(1)


while True:
    print('\nБАНКОМАТ\n\
    В банкомате {:.2f} у.е.\n\
    Введите число кратное 50\n\
    Положительное число - внести деньги\n\
    Отрицательное число - снять деньги\n\
    0 - выход из программы'.format(cash))
    # ввод и проверка на корректность ввода
    operate = input('Введите число: ')
    logger.debug(f'Введена строка "{operate}"')
    if operate == EXIT_SYMBOL:
        logger.debug(f'Введен символ выхода "{EXIT_SYMBOL}"')
        break
    if operate[0] == '-':
        if operate[1:].isnumeric():
            # снятие
            print('СНЯТИЕ')
            logger.debug('Операция снятия')
            operate = operate[1:]
            cash_in=False
        else:
            print('*** Ошибка ввода, повторите еще раз!')
            logger.warning('Ошибка ввода!')
            continue
    else:
        if operate.isnumeric():
            # внесение
            print('ВНЕСЕНИЕ')
            logger.debug('Операция внесения')
            cash_in=True
        else:
            print('*** Ошибка ввода, повторите еще раз!')
            logger.warning('Ошибка ввода!')
            continue
    
    # проверка на кратность 50
    cash_value = int(operate)
    if cash_value % KRATNO:
        msg = f'*** Ошибка ввода. Сумма должна быть кратной {KRATNO} у.е.'
        logger.warning(msg)
        print(msg)
        continue

    if cash_in:
        # внесение
        cash += cash_value
        msg = f'Выполнена операция зачисления {cash_value} у.е.'
        print(msg)
        logger.info(msg)
    else:
        # снятие
        # расчет комиссии за снятик
        tax_value = round(cash_value * CASH_OUT_TAX,2)
        if tax_value < CASH_OUT_MIN_TAX_VALUE:
            tax_value = CASH_OUT_MIN_TAX_VALUE
        if tax_value > CASH_OUT_MAX_TAX_VALUE:
            tax_value = CASH_OUT_MAX_TAX_VALUE
        msg = f'Сумма к снятию: {cash_value} у.е.\nКомиссия за снятие: {tax_value} у.е.\n'
        logger.debug(msg)
        print(msg)
        msg = f'ИТОГО к списанию: {cash_value + tax_value} у.е.'
        logger.info(msg)
        print(msg)
        if cash_value + tax_value > cash:
            msg = 'Недостаточно средств в банкомате'
            logger.warning(msg)
            print(msg)
        else:
            cash -= (cash_value + tax_value)
            msg = 'Операция снятия выполнена'
            logger.info(msg)
            print(msg)

    # вычитание налога на богатство
    if cash > CASH_LIMIT:
        limit_tax = round(cash * CASH_LIMIT_TAX, 2)
        msg = f'Удержан налог на богатство {limit_tax} у.е.'
        cash -= limit_tax
        logger.info(msg)
        print(msg)

    # начисление процентов
    operation_count += 1
    logger.debug(f'{operation_count}-я операция с момента запуска программы')
    if not (operation_count % OPERATION_COUNT_NUM):
        operation_count_inc_value = round((cash * OPERATION_COUNT_INC),2)
        msg = f'Начисление процентов: {operation_count_inc_value} у.е.'
        cash += operation_count_inc_value
        logger.info(msg)
        print(msg)

msg = 'ВЫХОД\nВ банкомате было {:.2f} у.е.\nРабота программы завершена'.format(cash)
logger.info(msg)
print(msg)
exit(0)
50