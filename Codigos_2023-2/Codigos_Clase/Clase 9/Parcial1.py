def base_salary(employee_position, salary_base):
    global salario
    if employee_position == "MANAGER":
        salario = salary_base * 0.05 
    elif employee_position == "SECRETARIES":
        salario = salary_base * 0.03
    elif employee_position == "COUNTER":
        salario = salary_base * 0.02
    elif employee_position == "OPERATOR":
        salario = salary_base * 0.015
    elif employee_position == "VIGILANT":
        salario = salary_base * 0.01
    else:
        print("Incorrect charge")
        return 0  


def net_salary(base_salary, share):
    health_employee = base_salary * 0.04
    pension_employee = base_salary * 0.25 * 0.16

    net_salary = base_salary - salario - health_employee - pension_employee - share
    return net_salary


if __name__ == "__main__":
    while True:
        try:
            name = "Alejandro"
            employee_position = "Manager".upper()
            salary_base = 6_000_000
            share = 155_000

            base_salary_value = base_salary(employee_position, salary_base)
            if base_salary_value == 0:
                continue  

            net_salary1 = net_salary(salary_base, share)
            if net_salary1 < 0:
                raise ValueError
            else:
                print("Name of the employee: ", name)
                print("Employee position: ", employee_position)
                print(f"Your monthly net salary is: {net_salary1}")
                break
        except ValueError:
            print("Error, the net salary is negative")
            continue
