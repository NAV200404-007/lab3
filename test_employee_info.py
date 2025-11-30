import employee_info as emp

def test_average_salary():
    result = emp.calculate_average_salary()
    assert result == 60166.666666666664

def test_age_range():
    result = emp.get_employees_by_age_range(30, 40)
    assert len(result) == 2   

def test_department_filter():
    result = emp.get_employees_by_dept("Sales")
    assert len(result) == 2   # John + Peter
