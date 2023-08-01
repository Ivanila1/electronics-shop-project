import pytest

from src.phone import Phone


def test_Phone():
    # # смартфон iPhone 14, цена 120000, количество товара 5, симкарт 2
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
