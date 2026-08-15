from core.enemy import Enemy


class Boss(Enemy):

    def __init__(
        self,
        enemy_id,
        name,
        level,
        max_hp,
        attack,
        defense,
        experience,
        gold,
        drop_chance,
        loot_type,
        region,
        title
    ):

        super().__init__(
            enemy_id,
            name,
            level,
            max_hp,
            attack,
            defense,
            experience,
            gold,
            drop_chance,
            loot_type
        )

        self.region = region
        self.title = title

    def __str__(self):

        return (
            f"{self.title}\n"
            f"{self.name}\n"
            f"Level {self.level}"
        )