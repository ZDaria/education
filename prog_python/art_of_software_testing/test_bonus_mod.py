import pytest
from prog_python.art_of_software_testing.bonus_mod import bonus
from prog_python.art_of_software_testing.test_values import \
    valid_employee_tab, \
    valid_department_tab, empty_employee_tab, empty_department_tab, \
    empty_leading_employee_tab, one_record_employee_tab, \
    one_record_department_tab, \
    same_sales_department_tab, same_sales_employee_tab, \
    leader_first_record_department_tab,\
    leader_employee_tab

""" This tests validate bonus_mod."""


@pytest.mark.parametrize('employee_tab, department_tab',
                         [(valid_employee_tab, valid_department_tab)])
def test_valid_values(employee_tab, department_tab):
    error_code, employee_tab_new = bonus(employee_tab, department_tab)
    assert error_code == 0


@pytest.mark.parametrize('employee_tab, department_tab',
                         [(empty_employee_tab, valid_department_tab),
                          (valid_employee_tab, empty_department_tab)])
def test_empty_tabs(employee_tab, department_tab):
    error_code, employee_tab_new = bonus(employee_tab, department_tab)
    assert error_code == 1


@pytest.mark.parametrize('employee_tab, department_tab',
                         [(empty_leading_employee_tab, valid_department_tab)])
def test_empty_leading_department(employee_tab, department_tab):
    error_code, employee_tab_new = bonus(employee_tab, department_tab)
    assert error_code == 2


@pytest.mark.parametrize('employee_tab, department_tab',
                         [(one_record_employee_tab,
                           one_record_department_tab)])
def test_one_record_tabs(employee_tab, department_tab):
    error_code, employee_tab_new = bonus(employee_tab, department_tab)
    assert error_code == 0


@pytest.mark.parametrize('employee_tab, department_tab',
                         [(same_sales_employee_tab,
                           same_sales_department_tab)])
def test_same_sales_department_tab(employee_tab, department_tab):
    error_code, employee_tab_new = bonus(employee_tab, department_tab)
    assert employee_tab_new["Anna"]["salary"] == 10200
    assert employee_tab_new["Alex"]["salary"] == 11200
    assert employee_tab_new["Bob"]["salary"] == 15100
    assert employee_tab_new["Bern"]["salary"] == 9200
    assert error_code == 0


@pytest.mark.parametrize('employee_tab, department_tab',
                         [(leader_employee_tab,
                           leader_first_record_department_tab)])
def test_leader_first_record_department_tab(employee_tab, department_tab):
    error_code, employee_tab_new = bonus(employee_tab, department_tab)
    assert employee_tab_new["Anna"]["salary"] == 10100
    assert employee_tab_new["Alex"]["salary"] == 11200
    assert employee_tab_new["Bob"]["salary"] == 15000
    assert employee_tab_new["Bern"]["salary"] == 9000
    assert employee_tab_new["Alisha"]["salary"] == 12500
    assert error_code == 0
