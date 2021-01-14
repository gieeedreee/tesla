from tesla.tesla.fabric import Tesla


def test_drive():
    model7 = Tesla('Model7', 'green', True, 0.3)
    travel_range = 100
    result = Tesla.drive(model7, travel_range)
    assert result == "Battery charge level is 69.9%"


def test_is_locked():
    model5 = Tesla('Model5', 'white', True, 0.2)
    result = Tesla.lock(model5)
    assert result == False

