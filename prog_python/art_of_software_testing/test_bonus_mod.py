import pytest
import prog_python.art_of_software_testing.bonus_mod as bonus_mod
from prog_python.art_of_software_testing.test_values import valid_employee_tab, valid_department_tab, \
    empty_employee_tab, valid_department_tab_1


@pytest.mark.parametrize('employee_tab, department_tab', [(valid_employee_tab, valid_department_tab)])
def test_valid_values(employee_tab, department_tab):
    bonus_mod.bonus(employee_tab, department_tab) == 0

@pytest.mark.parametrize('employee_tab, department_tab', [(empty_employee_tab, valid_department_tab_1)])
def test_empty_employee_tab(employee_tab, department_tab):
    bonus_mod.bonus(employee_tab, department_tab) == 0