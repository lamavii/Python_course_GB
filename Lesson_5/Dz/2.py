# 3. Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины: имена str,
# ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии
# в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

name_list = ['Nika', 'Misha', 'Alex']
salary_list = [45000, 23000, 40000]
bonus_list = ['12.5%', '11.3%', '9.8%']

def calculate_bonus(name: str, salary: int, bonus: str) -> dict[str, float]:
      return {name: salary / 100 * float(bonus[:-1]) for name, salary, bonus in zip(name_list, salary_list, bonus_list)}

print(calculate_bonus(name_list, salary_list, bonus_list))