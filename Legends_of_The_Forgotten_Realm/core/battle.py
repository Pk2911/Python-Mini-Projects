import random


class Battle:

    def __init__(self, player, enemy, database):

        self.player = player
        self.enemy = enemy
        self.database = database

    # ==========================================
    # Display
    # ==========================================

    def show_status(self):

        print("\n========================================")

        print(
            f"Player HP : "
            f"{self.player.hp}/{self.player.max_hp}"
        )

        print(
            f"{self.enemy.name} HP : "
            f"{self.enemy.hp}/{self.enemy.max_hp}"
        )

        print("========================================")

    # ==========================================
    # Player Attack
    # ==========================================

    def player_attack(self):

        damage, critical_hit = self.player.basic_attack()

        damage = max(1, damage - self.enemy.defense)

        self.enemy.hp = max(0, self.enemy.hp - damage)

        if critical_hit:

            print("\n🔥 Critical Hit!")

        print(f"You dealt {damage} damage!")

    # ==========================================
    # Enemy Attack
    # ==========================================

    def enemy_attack(self):

        damage = max(
            1,
            self.enemy.attack - self.player.defense
        )

        self.player.hp = max(
            0,
            self.player.hp - damage
        )

        print(f"{self.enemy.name} dealt {damage} damage!")

    # ==========================================
    # Defend
    # ==========================================

    def defend(self):

        damage = self.enemy.attack // 2

        damage = max(
            1,
            damage - self.player.defense
        )

        self.player.hp = max(
            0,
            self.player.hp - damage
        )

        print("\nYou defended!")
        print(f"You received {damage} damage.")

    # ==========================================
    # Potion
    # ==========================================

    def potion_menu(self):

        potions = self.player.inventory["potions"]

        if not potions:

            print("\nYou have no potions.")

            return False

        print("\n========== POTIONS ==========")

        for index, potion in enumerate(
            potions,
            start=1
        ):

            print(f"{index}. {potion.name}")

        print("0. Cancel")

        try:

            choice = int(input("\nChoose: "))

        except ValueError:

            print("\nInvalid input.")
            return False

        if choice == 0:

            return False

        return self.player.use_potion(choice - 1)

    # ==========================================
    # Escape
    # ==========================================

    def escape(self):

        chance = random.randint(1, 100)

        if chance <= 40:

            print("\nYou successfully escaped!")

            return True

        print("\nEscape failed!")

        return False

    # ==========================================
    # Rewards
    # ==========================================

    def victory(self):

        print(f"\nYou defeated {self.enemy.name}!")

        self.player.gold += self.enemy.gold
        self.player.gain_experience(
            self.enemy.experience
        )
        self.player.enemies_defeated += 1

        print(f"Gold Earned : {self.enemy.gold}")
        print(f"EXP Earned  : {self.enemy.experience}")

        self.drop_loot()

        if self.enemy.__class__.__name__ == "Boss":

            print("\n👑 Boss Defeated!")

            self.player.bosses_defeated += 1

            if self.player.highest_region_unlocked < 10:

                self.player.highest_region_unlocked += 1

                print(
                    f"New Region Unlocked! "
                    f"Region {self.player.highest_region_unlocked}"
                )

            if self.enemy.enemy_id == "BOSS010":

                print("\n🎉 CONGRATULATIONS!")
                print("You defeated the Ancient Demon King!")
                print("You have completed Legends of the Forgotten Realm!")

    # ==========================================
    # Battle Loop
    # ==========================================

    def start(self):

        print(f"\nA wild {self.enemy.name} appeared!")

        while self.player.is_alive and self.enemy.is_alive:

            self.show_status()

            print("\n1. Attack")
            print("2. Defend")
            print("3. Use Potion")
            print("4. Escape")

            choice = input("\nChoose: ")

            if choice == "1":

                self.player_attack()

            elif choice == "2":

                self.defend()

            elif choice == "3":

                self.potion_menu()

            elif choice == "4":

                if self.escape():

                    return

            else:

                print("\nInvalid choice.")
                continue

            if not self.enemy.is_alive:

                break

            self.enemy_attack()

        if self.player.is_alive:

            self.victory()

        else:

            print("\nYou were defeated...")

    def drop_loot(self):

        roll = random.randint(1, 100)

        if roll > self.enemy.drop_chance:

            print("\nNo loot dropped.")

            return

        if self.enemy.loot_type == "Weapon":

            item = self.database.random_weapon(
                self.player.level
            )

        elif self.enemy.loot_type == "Armor":

            item = self.database.random_armor(
                self.player.level
            )

        else:

            item = self.database.random_potion()

        self.player.add_item(item)

        print(f"\n🎁 Loot Found!")
        print(f"You obtained: {item.name}")