import pytest
from prog_python.art_of_software_testing.bonus_mod import bonus
from prog_python.art_of_software_testing.test_values import valid_employee_tab, \
    valid_department_tab, empty_employee_tab, empty_department_tab, empty_leading_employee_tab


@pytest.mark.parametrize('employee_tab, department_tab', [(valid_employee_tab,
                                                           valid_department_tab)])
def test_valid_values(employee_tab, department_tab):
    assert bonus(employee_tab, department_tab) == 0


@pytest.mark.parametrize('employee_tab, department_tab', [(empty_employee_tab,
                                                           valid_department_tab),
                                                          (valid_employee_tab, empty_department_tab)])
def test_empty_tabs(employee_tab, department_tab):
    assert bonus(employee_tab, department_tab) == 1


@pytest.mark.parametrize('employee_tab, department_tab', [(empty_leading_employee_tab,
                                                           valid_department_tab)])
def test_empty_leading_department(employee_tab, department_tab):
    assert bonus(employee_tab, department_tab) == 2
