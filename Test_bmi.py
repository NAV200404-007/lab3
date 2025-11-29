import Lab2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.75, 70)   # BMI ≈ 22.9 → Normal
    assert result == 0

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.70, 85)   # BMI ≈ 29.4 → Over
    assert result == 1

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.75, 45)   # BMI ≈ 14.7 → Under
    assert result == -1
