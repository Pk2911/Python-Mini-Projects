from core.equippable import Equippable


class Armor(Equippable):
    """
    Represents an armor that can be equipped by the player.
    """

    def __init__(
        self,
        item_id: str,
        name: str,
        rarity,
        defense_bonus: int,
        hp_bonus: int,
        mana_bonus: int,
        crit_resistance: int,
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

        self.defense_bonus = defense_bonus
        self.hp_bonus = hp_bonus
        self.mana_bonus = mana_bonus
        self.crit_resistance = crit_resistance

    def __str__(self):

        return (
            f"{self.name}\n"
            f"Defense : +{self.defense_bonus}\n"
            f"HP       : +{self.hp_bonus}\n"
            f"Mana     : +{self.mana_bonus}\n"
            f"Crit Res : +{self.crit_resistance}%\n"
            f"Rank     : {self.rarity.value}"
        )