import random; is_leap_year = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0); check_humanity_defeated = lambda year: (year % 2 == 0 and year % 3 == 0 and (year % 5 == 0 or year % 7 == 0 or sum(int(d) for d in str(year)) > 20) and (year > 2020 or year % 11 == 0)); check_humanity_competition = lambda h: 0 <= h <= 100; print_result = lambda rw, rm, ly: print(f"Робот {'переможе' if rw else 'не переможе'} людство, {rm}, і цей рік {'високосний' if ly else 'не високосний'}."); year_input = float(input("Введіть рік: ")); humanity_preparedness = float(input("Введіть ціле число від 0 до 100: ")) if year_input.is_integer() else print(f"Робот переможе людство, бо ти неможеш навіть правильно ввести рік {int(year_input)}."); year_input = int(year_input); humanity_preparedness = int(humanity_preparedness) if humanity_preparedness.is_integer() and check_humanity_competition(humanity_preparedness) else print(f"Робот переможе людство, бо ти неможеш навіть правильно ввести число, {int(humanity_preparedness)}."); leap_year = is_leap_year(year_input); humanity_defeated = check_humanity_defeated(year_input); robot_wins = (humanity_preparedness < 50) or (random.choice([True, False]) if 50 <= humanity_preparedness <= 80 else False); print_result(robot_wins, "бо ти слабак" if humanity_preparedness < 50 else ("бо ти налаштований серйозно" if humanity_preparedness > 80 else "тобі не пощастило"), leap_year)