import csv
from typing import List, Dict, Union

# Тип данных для записи о сотруднике
employee_dict = Dict[str, Union[str, float, int]]


def read_csv(file_path: str) -> List[employee_dict]:
    """Чтение данных из CSV-файла и возврат их в виде списка словарей"""
    employee_list = []
    with open(file_path, mode = 'r', encoding = 'utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            employee_list.append(row)
    return employee_list


def print_hierarchy(employee_list: List[employee_dict]):
    """Функция для вывода иерархии команд"""
    departments = set()
    teams_by_department = {}

    for employee in employee_list:
        department = employee["Департамент"]
        team = employee["Отдел"]

        departments.add(department)
        if department in teams_by_department:
            teams_by_department[department].add(team)
        else:
            teams_by_department[department] = {team}

    print("Иерархия команд:")
    for department in departments:
        print(f"Департамент: {department}")
        for team in teams_by_department.get(department, []):
            print(f"  - Команда: {team}")


def generate_department_report(employee_list: List[employee_dict]):
    """Функция для создания сводного отчета по департаментам"""
    department_report = {}

    for employee in employee_list:
        department = employee["Департамент"]
        salary = int(employee["Оклад"])

        if department in department_report:
            department_report[department]["численность"] += 1
            department_report[department]["зарплаты"].append(salary)
        else:
            department_report[department] = {"численность": 1, "зарплаты": [salary]}

    print("Сводный отчет по департаментам:")
    for department, data in department_report.items():
        min_salary = min(data["зарплаты"])
        max_salary = max(data["зарплаты"])
        avg_salary = sum(data["зарплаты"]) / data["численность"]
        print(f"Департамент: {department}")
        print(f"Численность: {data['численность']}")
        print(f"Вилка зарплат: {min_salary} - {max_salary}")
        print(f"Средняя зарплата: {avg_salary}")
        print()


def save_department_report_to_csv(employee_list: List[employee_dict], output_file: str):
    """Функция для сохранения сводного отчета в CSV-файл"""
    department_report = {}

    for employee in employee_list:
        department = employee["Департамент"]
        salary = int(employee["Оклад"])

        if department in department_report:
            department_report[department]["численность"] += 1
            department_report[department]["зарплаты"].append(salary)
        else:
            department_report[department] = {"численность": 1, "зарплаты": [salary]}

    with open(output_file, mode='w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file, delimiter=';')
        csv_writer.writerow(["Департамент", "Численность", "Мин зарплата", "Макс зарплата", "Средняя зарплата"])
        for department, data in department_report.items():
            min_salary = min(data["зарплаты"])
            max_salary = max(data["зарплаты"])
            avg_salary = sum(data["зарплаты"]) / data["численность"]
            csv_writer.writerow([department, data['численность'], min_salary, max_salary, avg_salary])


def main():
    """Главная функция для выполнения задачи"""
    file_path = "Corp_Summary.csv"
    employee_list = read_csv(file_path)

    while True:
        print("\nМеню:")
        print("1) Вывести иерархию команд")
        print("2) Вывести сводный отчет по департаментам")
        print("3) Сохранить сводный отчет в CSV")
        print("4) Выйти")
        choice = input("Выберите действие (1/2/3/4): ")
        if choice == "1":
            print_hierarchy(employee_list)
        elif choice == "2":
            generate_department_report(employee_list)
        elif choice == "3":
            output_file = input("Введите имя файла для сохранения отчета (например, report.csv): ")
            save_department_report_to_csv(employee_list, output_file)
            print(f"Сводный отчет сохранен в файл {output_file}")
        elif choice == "4":
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите пункт меню (1/2/3/4).")


if __name__ == '__main__':
    main()
