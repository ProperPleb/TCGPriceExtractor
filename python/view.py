from cardmanager import CardManager
from rest import Rest
from card import Card


def display():
    rest = Rest()
    manager = CardManager(rest=rest)
    manager.populate_deck()
    print("Total: " + str(manager.calculate_total_price()))
    manager.write_to_excel("complete.xlsx")
