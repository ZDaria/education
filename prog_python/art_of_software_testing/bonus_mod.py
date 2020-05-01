
def bonus(employee_tab, department_tab):
    max_sales = ('A', {'sales': 0})
    salary_large = 15000
    bonus_emp = 200
    bonus_mgr = 100
    error_code = 4
    if employee_tab.__len__() <= 0 or department_tab.__len__() <= 0:
        error_code = 1
    else:
        for department in department_tab.items():
            if department[1]["sales"] >= max_sales[1]["sales"]:
                max_sales = department

        for employee in employee_tab.items():
            if employee[1]["dept"] == max_sales[0]:
                error_code = 0
                if employee[1]["code"] == "MGR" or employee[1]["salary"] >= salary_large:
                    employee[1]["salary"] += bonus_mgr
                else:
                    employee[1]["salary"] += bonus_emp
        if error_code == 4:
            error_code = 2
    return error_code
