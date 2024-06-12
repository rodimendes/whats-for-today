from main_code.power_of import power_of_two


def test_power_of_two():
    assert power_of_two(1) == 1
    assert power_of_two(3) == 9
    assert power_of_two(4) == 16
    assert power_of_two(5) == 25
    assert power_of_two(6) == 36