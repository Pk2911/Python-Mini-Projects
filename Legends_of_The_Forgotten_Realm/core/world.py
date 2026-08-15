import random

from core.battle import Battle

class World:

    def __init__(self, database):

        self.database = database
        self.regions = database.load_json("world.json")

    def display_regions(self, player):

        print("\n========== WORLD MAP ==========\n")

        for region in self.regions:

            if region["id"] <= player.highest_region_unlocked:

                print(
                    f"{region['id']}. "
                    f"{region['name']} "
                    f"(Lv {region['min_level']}-{region['max_level']})"
                )

            else:

                print(
                    f"{region['id']}. "
                    f"{region['name']} 🔒"
                )

    def explore(self, player):

        while True:

            self.display_regions(player)

            try:

                choice = int(input("\nChoose Region: "))

            except ValueError:

                print("\nInvalid input.")
                continue

            if choice == 0:

                return

            region = next(
                (
                    r for r in self.regions
                    if r["id"] == choice
                ),
                None
            )

            if region is None:

                print("\nInvalid region.")
                continue

            if region["id"] > player.highest_region_unlocked:

                print("\n🔒 This region is locked!")
                print(
                    f"Defeat the boss of Region {player.highest_region_unlocked} "
                    "to unlock the next region."
                )

                input("\nPress Enter to continue...")
                continue

            enemy_id = random.choice(region["enemy_ids"])

            enemy = self.database.get_enemy(enemy_id)

            battle = Battle(
                player,
                enemy,
                self.database
            )

            print("\n0. Return")

            battle.start()