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

while True:
    print('\nБАНКОМАТ\n\
    В банкомате {:.2f} у.е.\n\
    Введите число кратное 50\n\
    Положительное число - внести деньги\n\
    Отрицательное число - снять деньги\n\
    0 - выход из программы'.format(cash))
    # ввод и проверка на корректность ввода
    operate = input('Введите число: ')
    if operate == EXIT_SYMBOL:
        break
    if operate[0] == '-':
        if operate[1:].isnumeric():
            # снятие
            print('СНЯТИЕ')
            operate = operate[1:]
            cash_in=False
        else:
            print('*** Ошибка ввода, повторите еще раз!')
            continue
    else:
        if operate.isnumeric():
            # внесение
            print('ВНЕСЕНИЕ')
            cash_in=True
        else:
            print('*** Ошибка ввода, повторите еще раз!')
            continue
    
    # проверка на кратность 50
    cash_value = int(operate)
    if cash_value % KRATNO:
        print(f'*** Ошибка ввода. Сумма должна быть кратной {KRATNO} у.е.')
        continue

    if cash_in:
        # внесение
        print(f'Сумма к зачислению: {cash_value} у.е.')
        cash += cash_value
        print('Операция зачисления выполнена')
    else:
        # снятие
        # расчет комиссии за снятик
        tax_value = round(cash_value * CASH_OUT_TAX,2)
        if tax_value < CASH_OUT_MIN_TAX_VALUE:
            tax_value = CASH_OUT_MIN_TAX_VALUE
        if tax_value > CASH_OUT_MAX_TAX_VALUE:
            tax_value = CASH_OUT_MAX_TAX_VALUE
        print(f'Сумма к снятию: {cash_value} у.е.\nКомиссия за снятие: {tax_value} у.е.\n')
        print(f'ИТОГО к списанию: {cash_value + tax_value} у.е.')
        if cash_value + tax_value > cash:
            print('Недостаточно средств в банкомате')
        else:
            cash -= (cash_value + tax_value)
            print('Операция снятия выполнена')

    # вычитание налога на богатство
    if cash > CASH_LIMIT:
        limit_tax = round(cash * CASH_LIMIT_TAX, 2)
        print(f'Удержан налог на богатство {limit_tax} у.е.')
        cash -= limit_tax

    # начисление процентов
    operation_count += 1
    if not (operation_count % OPERATION_COUNT_NUM):
        operation_count_inc_value = round((cash * OPERATION_COUNT_INC),2)
        print(f'Начисление процентов: {operation_count_inc_value} у.е.')
        cash += operation_count_inc_value

print('ВЫХОД\nВ банкомате было {:.2f} у.е.\nРабота программы завершена'.format(cash))
