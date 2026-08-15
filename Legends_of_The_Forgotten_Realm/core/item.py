from abc import ABC


class Item(ABC):
    """
    Base class for every item in the game.
    """

    def __init__(
        self,
        item_id: str,
        name: str,
        rarity,
        price: int,
        required_level: int
    ):

        self.item_id = item_id
        self.name = name
        self.rarity = rarity
        self.price = price
        self.required_level = required_level

    def __str__(self):

        return f"{self.name} ({self.rarity.value})"