from core.consumable import Consumable


class Potion(Consumable):
    """
    Represents a consumable potion.
    """

    def __init__(
        self,
        item_id: str,
        name: str,
        rarity,
        potion_type: str,
        value: int,
        duration: int,
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

        self.potion_type = potion_type
        self.value = value
        self.duration = duration

    def __str__(self):

        return (
            f"{self.name}\n"
            f"Type     : {self.potion_type}\n"
            f"Value    : {self.value}\n"
            f"Duration : {self.duration}\n"
            f"Rank     : {self.rarity.value}"
        )