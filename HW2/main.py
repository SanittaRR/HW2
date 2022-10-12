def create_hierarchy(csv_file) -> dict:
    """" Creates a dictionary with all departments and teams related to them """
    d = {}
    with open(csv_file, "r") as f:
        for i in f:
            z = i.strip().split(";")
            if z[1] not in d:
                d[z[1]] = z[2]
            else:
                if z[2] not in d[z[1]]:
                    d[z[1]] = d[z[1]] + ', ' + z[2]
    return d


def show_hierarchy(d):
    """" Displays the hierarchy table """
    print()
    for k, v in d.items():
        print("{:<15} {:<45}".format(k, v))
    print()


def create_consolidated_report(csv_file) -> dict:
    """" Creates a dictionary of a summary report by departments with names, number of people,
     "fork" of salaries in the form of min - max and average salary of workers """
    d = {}
    with open(csv_file, "r") as f:
        next(f)
        for i in f:
            z = i.strip().split(";")
            if z[1] not in d:
                min_salary = max_salary = avg_salary = int(z[5])
                sub_dict = {'Численность': 1, 'Вилка зарплат': [min_salary, max_salary],
                            'Средняя зарплата': avg_salary}
                d[z[1]] = sub_dict
            else:
                avg_salary = (d[z[1]]['Численность'] * d[z[1]]['Средняя зарплата']
                              + int(z[5])) / (d[z[1]]['Численность'] + 1)
                d[z[1]]['Средняя зарплата'] = round(avg_salary, 2)
                d[z[1]]['Численность'] += 1
                if int(z[5]) < d[z[1]]['Вилка зарплат'][0]:
                    d[z[1]]['Вилка зарплат'][0] = int(z[5])
                if int(z[5]) > d[z[1]]['Вилка зарплат'][1]:
                    d[z[1]]['Вилка зарплат'][1] = int(z[5])
    return d


def show_consolidated_report(d: dict):
    """" Displays the consolidated report table """
    print()
    print("{:<15} {:<15} {:<15} {:<15}".format('Департамент', 'Численность', 'Вилка зарплат', 'Средняя зарплата'))
    for k, v in d.items():
        number, vilka, avg = v.values()
        vilka_form = f'{vilka[0]} - {vilka[1]}'
        print("{:<15} {:<15} {:<15} {:<15}".format(k, number, vilka_form, avg))
    print()


def save_consolidated_report(d: dict):
    """" Saves the consolidated report table into csv file """
    with open('final.csv', 'w') as f:
        header = ['Департамент', 'Численность', 'Вилка зарплат', 'Средняя зарплата']
        f.write(','.join(header))
        f.write("\n")
        for k, v in d.items():
            number, vilka, avg = v.values()
            vilka_form = f'{vilka[0]} - {vilka[1]}'
            result = [k, number, vilka_form, avg]
            f.write(','.join(str(e) for e in result))
            f.write("\n")


def make_menu():
    """" Displays the menu with 4 options and opportunity to choose between them """
    while True:
        print("1. Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него")
        print("2. Вывести сводный отчёт по департаментам: название, численность,"
              " \"вилка\" зарплат в виде мин – макс, среднюю зарплату")
        print("3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. "
              "При этом необязательно вызывать сначала команду из п.2")
        print("0. Закрыть меню")

        cmd = input("Выберите пункт: ")

        if cmd == "1":
            show_hierarchy(create_hierarchy("Corp_Summary.csv"))
        elif cmd == "2":
            show_consolidated_report(create_consolidated_report("Corp_Summary.csv"))
        elif cmd == "3":
            save_consolidated_report(create_consolidated_report("Corp_Summary.csv"))
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")


if __name__ == '__main__':
    make_menu()
