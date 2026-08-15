from core.equippable import Equippable

class Weapon(Equippable):

    def __init__(
        self,
        item_id: str,
        name: str,
        rarity,
        damage: int,
        crit_bonus: int,
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

        self.damage = damage
        self.crit_bonus = crit_bonus

    def __str__(self):

        return (
            f"{self.name}"
            f"\nDamage : {self.damage}"
            f"\nCrit   : +{self.crit_bonus}%"
            f"\nRank   : {self.rarity.value}"
        )