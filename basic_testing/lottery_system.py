import random


def pick_one_name(names):
    return random.choice(names)


def pick_n_names(names, n):
    return random.sample(names, k=n)


class Raffle:
    def __init__(self, max_people, max_tickets, ticket_price):
        self.max_people = max_people
        self.max_tickets = max_tickets
        self.ticket_price = ticket_price
        self.total_earnings = 0
        self.participants = {}

    def add_person(self, name):
        if name in self.participants:
            return f"{name} is already in the raffle."
        if len(self.participants) < self.max_people:
            self.participants[name] = 0
            return f"{name} added to the raffle."
        else:
            return "Raffle is at max capacity."

    def buy_tickets(self, name, number_of_tickets):
        if name not in self.participants:
            return f"{name} is not a participant in the raffle."
        if self.total_tickets() + number_of_tickets > self.max_tickets:
            return "Not enough tickets available."
        self.participants[name] += number_of_tickets
        self.total_earnings += number_of_tickets * self.ticket_price
        return f"{number_of_tickets} tickets purchased by {name}."

    def total_tickets(self):
        return sum(self.participants.values())

    def select_winner(self):
        if not self.participants:
            return "No participants in the raffle."
        all_tickets = [(name, ticket) for name, tickets in self.participants.items() for ticket in range(tickets)]
        winner = random.choice(all_tickets)[0]
        return f"The winner is {winner}."
