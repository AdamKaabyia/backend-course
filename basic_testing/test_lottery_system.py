import pytest
from lottery_system import *


@pytest.fixture
def setup_raffle():
    raffle = Raffle(max_people=10, max_tickets=100, ticket_price=10)
    return raffle


def test_pick_one_name():
    names = ["Alice", "Bob", "Charlie"]
    assert pick_one_name(names) in names


def test_pick_n_names():
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    selected_names = pick_n_names(names, 3)
    assert len(selected_names) == 3
    assert all(name in names for name in selected_names)
    assert len(set(selected_names)) == len(selected_names)  # Ensure uniqueness


def test_add_person(setup_raffle):
    raffle = setup_raffle
    response = raffle.add_person("Frank")
    assert response == "Frank added to the raffle."
    assert "Frank" in raffle.participants
    assert raffle.participants["Frank"] == 0


def test_buy_tickets(setup_raffle):
    raffle = setup_raffle
    raffle.add_person("Gina")
    response = raffle.buy_tickets("Gina", 5)
    assert response == "5 tickets purchased by Gina."
    assert raffle.total_earnings == 50
    assert raffle.participants["Gina"] == 5


def test_select_winner(setup_raffle):
    raffle = setup_raffle
    raffle.add_person("Hank")
    raffle.buy_tickets("Hank", 1)
    winner_announcement = raffle.select_winner()
    assert "The winner is Hank." in winner_announcement


@pytest.mark.parametrize("max_people, max_tickets, ticket_price, expected_earnings", [
    (10, 100, 10, 0),  # Initial state
    (10, 100, 20, 100)  # After buying tickets
])
def test_total_earnings(setup_raffle, max_people, max_tickets, ticket_price, expected_earnings):
    raffle = Raffle(max_people, max_tickets, ticket_price)
    if expected_earnings > 0:
        raffle.add_person("Ivy")
        raffle.buy_tickets("Ivy", 5)
    assert raffle.total_earnings == expected_earnings
