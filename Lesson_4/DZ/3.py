# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные
# операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import decimal

decimal.getcontext().prec = 33
MULTIPLICITY = 50
PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
COUNT_PERC = 3
MIN_LIMIT = decimal.Decimal(30)
MAX_LIMIT = decimal.Decimal(600)
PERCENT_RICH = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_AMOUNT = 5000000
CMD_DEPOSIT = '1'
CMD_WITH_DRAW = '2'
CMD_EXIT = '3'

balance = 0
operations = []


def deposit(balance, operations):
    """
    Обрабатывает операцию пополнения счета.
    Принимает текущий баланс и количество операций.
    Возвращает обновленные значения баланса и количества операций.
    """
    amount = 1
    while amount % MULTIPLICITY != 0:
        amount = int(input(f'Введите сумму кратную {MULTIPLICITY}: '))
    operations.append((amount, 'зачисление'))
    return balance + amount, operations


def withdraw(balance, operations):
    """
    Обрабатывает операцию снятия средств со счета.
    Принимает текущий баланс и количество операций.
    Возвращает обновленные значения баланса и количества операций.
    """
    amount = 1
    while amount % MULTIPLICITY != 0:
        amount = int(input(f'Введите сумму кратную {MULTIPLICITY}: '))
    comission = amount * PERCENT
    if comission < MIN_LIMIT:
        comission = MIN_LIMIT
    elif comission > MAX_LIMIT:
        comission = MAX_LIMIT
    if comission + amount > balance:
        print(f'На балансе недостаточно средств')
    else:
        operations.append((amount, 'снятие'))
        return balance - amount - comission, operations


def apply_bonus(balance):
    """
    Применяет бонус к балансу, если выполнено достаточное количество операций.
    Принимает текущий баланс и количество операций.
    Возвращает обновленный баланс.
    """
    if len(operations) % COUNT_PERC == 0:
        bonus_sum = balance * PERCENT_BONUS
        balance += bonus_sum
        print(f'Сумма бонуса {bonus_sum}')
    return balance


def apply_rich_tax(balance):
    """
    Применяет налог на богатство, если баланс превышает заданный порог.
    Принимает текущий баланс.
    Возвращает обновленный баланс.
    """
    if balance > RICHNESS_AMOUNT:
        sum_percent = balance * PERCENT_RICH
        balance -= sum_percent
        print(f'Вычтен налог на богатство в размере {sum_percent}')
    return balance


def get_user_action(balance, operations):
    """
    Получает от пользователя выбранное действие: пополнить, снять или выйти.
    Обрабатывает выбранное действие и возвращает обновленный баланс и список операций.
    """
    action = input(
        f'пополнить - {CMD_DEPOSIT}\n'
        f'снять - {CMD_WITH_DRAW}\n'
        f'выход - {CMD_EXIT}\n'
        f'Введите действие: '
    )

    if action == '1':
        return deposit(balance, operations)
    elif action == '2':
        return withdraw(balance, operations)
    elif action == '3':
        return None, None
    else:
        print('Введена неверная команда')
        return balance, operations


continue_running = True
while continue_running:
    balance = apply_rich_tax(balance)
    balance = apply_bonus(balance)

    balance, operations = get_user_action(balance, operations)

    if balance is None or operations is None:
        continue_running = False

    print(f'Текущая операция {operations}')
    print(f'Текущий баланс {balance}')