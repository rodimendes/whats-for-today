from main_code.power_of import power_of


def test_power():
    assert power_of(2) == 4
    assert power_of(3) == 9
    assert power_of(4) == 16
    assert power_of(1) == 1