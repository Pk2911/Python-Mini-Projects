from core.item import Item


class Consumable(Item):
    """
    Base class for consumable items.
    """

    def __init__(
        self,
        item_id: str,
        name: str,
        rarity,
        price: int,
        required_level: int
    ):

        super().__init__(
            item_id,
            name,
            rarity,
            price,
            required_level
        )

    def consume(self):
        """
        To be implemented by child classes.
        """
        pass