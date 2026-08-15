from core.item import Item


class Equippable(Item):
    """
    Base class for all equippable items.
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

        self.is_equipped = False

    def equip(self):

        self.is_equipped = True

    def unequip(self):

        self.is_equipped = False