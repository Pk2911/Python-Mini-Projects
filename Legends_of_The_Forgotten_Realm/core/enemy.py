class Enemy:
    """
    Represents a normal enemy.
    """

    def __init__(
        self,
        enemy_id: str,
        name: str,
        level: int,
        max_hp: int,
        attack: int,
        defense: int,
        experience: int,
        gold: int,
        drop_chance: int,
        loot_type: str
    ):

        self.enemy_id = enemy_id
        self.name = name

        self.level = level

        self.max_hp = max_hp
        self.hp = max_hp

        self.attack = attack
        self.defense = defense

        self.experience = experience
        self.gold = gold

        self.drop_chance = drop_chance
        self.loot_type = loot_type

    @property
    def is_alive(self):
        return self.hp > 0

    def __str__(self):

        return (
            f"{self.name}\n"
            f"Level    : {self.level}\n"
            f"HP       : {self.hp}/{self.max_hp}\n"
            f"Attack   : {self.attack}\n"
            f"Defense  : {self.defense}"
        )