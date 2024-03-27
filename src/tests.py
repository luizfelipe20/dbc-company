import pytest

from src.question1 import Contract, Contracts
from src.question2 import Orders


@pytest.mark.parametrize("renegotiated_contracts, expected_open_contracts, main_contracts", [
    ([3, 5], [8, 6, 4], 3),
    ([7], [5, 3], 2),
    ([1, 2, 3], [5, 8, 6], 3),
])
def test_get_top_n_open_contracts_success(renegotiated_contracts,
                                          expected_open_contracts,
                                          main_contracts):
    _contracts = [
        Contract(1, 1000),
        Contract(2, 500),
        Contract(3, 4000),
        Contract(4, 2000),
        Contract(5, 5000),
        Contract(6, 2500),
        Contract(7, 700),
        Contract(8, 3000),
    ]
    _top_n = main_contracts
    contracts = Contracts()
    open_contracts = contracts.get_top_n_open_contracts(_contracts, renegotiated_contracts, _top_n)

    assert expected_open_contracts == open_contracts

@pytest.mark.parametrize("orders, expected_number_trips", [
    ([70, 30, 10, 90, 50, 40, 30, 90, 10], 5),
    ([70, 30, 10], 2),
    ([70, 30, 10, 90, 50, 40, 30], 4),
])
def test_combine_orders_success(orders, expected_number_trips):
    _orders = orders
    _n_max = 100
    orders = Orders()
    number_trips = orders.combine_orders(_orders, _n_max)

    assert expected_number_trips == number_trips


@pytest.mark.parametrize("orders, expected", [
    (10, "type_error__combine_orders"),
    ([[], []], "type_error__combine_orders"),
    ("", "index_error__combine_orders"),
    ([], "index_error__combine_orders"),
])
def test_combine_orders_invalid_input(orders, expected):
    _orders = orders
    _n_max = 100
    orders = Orders()

    with pytest.raises(Exception) as exc_info:
        orders.combine_orders(_orders, _n_max)

    assert expected in str(exc_info.value)
