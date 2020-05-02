
def bonus(employee_tab, department_tab):
    """
    This module counts bonus for employees.
    The value of bonus depends from they role and salary.
    :param employee_tab: contains employees list with description
    :param department_tab: contains departments with they results
    :return: error code and updated employee tab with
    """
    max_sales = 0
    max_sales_departments = []
    salary_large = 15000
    # bonus for all employee
    bonus_emp = 200
    # bonus for managers and for employee with salary more, than salary_large
    bonus_mgr = 100
    error_code = 4
    """
    If there isn't values in lists module should finished with error code 1
    """
    if employee_tab.__len__() <= 0 or department_tab.__len__() <= 0:
        error_code = 1
    else:
        # get best sales department
        for department in department_tab.items():
            if department[1]["sales"] > max_sales:
                max_sales = department[1]["sales"]
                max_sales_departments = [department[0]]
            elif department[1]["sales"] == max_sales:
                max_sales_departments.append(department[0])
        # get employees referring to best sales department
        for employee in employee_tab.items():
            if employee[1]["dept"] in max_sales_departments:
                error_code = 0
                """
                Payment bonus will depends from code value.
                MGR - employee role is manager
                EMP - ordinary role for employee
                """
                if employee[1]["code"] == "MGR" or employee[1]["salary"] >= salary_large:
                    employee[1]["salary"] += bonus_mgr
                else:
                    employee[1]["salary"] += bonus_emp
        """
        If there isn't employees referring to leading department module should return error code 1.
        In any other case error code will be 0 
        """
        if error_code == 4:
            error_code = 2
    return error_code, employee_tab
