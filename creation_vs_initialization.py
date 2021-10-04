# As an example, lets say that a class "Card" needs to be
# created such that any instance of the object itself behaves
# exactly like a tuple, but prints out (and has a __repr__)
# like any other normal object.

# We also want that creation of objects of this type to be
# controlled, meaning that invalid values cannot just be
# passed to them, and an error is raised when it does happen
# (just like with a tuple).

# A possible solution in this case would be to override
# object creation with __new__. __new__, unlike __init__
# returns the new instance of the object before any values
# are assigned to it. The self parameter in __init__ is
# what __new__ returns before the constructor is invoked.


class Card(tuple):
    """A tuple which stores information about a card in a
    deck. Is created, but not initialized, as it is a tuple.
    """
    
    def __new__(cls, *args):
        suits = {"clubs", "diamonds", "hearts", "spades"}
        special_cards = {11: "Jack", 12: "Queen", 13: "King", 1: "Ace"}

        value, suit = args

        if value <= 13 and suit in suits:
            if value > 10:
                value = special_cards[value]
                args = value, suit
            return super().__new__(cls, args)  # The new instance of the object "self"
        else:
            raise ValueError

    def __repr__(self):
        value, suit = self
        return f"Card({value=}, {suit=})"


def main() -> None:
    new_card = Card(12, "hearts")
    print(new_card)


if __name__ == "__main__":
    main()
