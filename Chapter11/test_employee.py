# 11-3 Tests WITHOUT fixture

from employee import Employee

def test_give_default_raise():
    emp = Employee("John", "Doe", 50000)
    emp.give_raise()
    assert emp.salary == 55000

def test_give_custom_raise():
    emp = Employee("John", "Doe", 50000)
    emp.give_raise(10000)
    assert emp.salary == 60000




    # 11-3 Tests WITH fixture

import pytest
from employee import Employee

@pytest.fixture
def employee():
    return Employee("John", "Doe", 50000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 55000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.salary == 60000