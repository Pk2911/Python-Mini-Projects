class Shop:

    def __init__(self, database):

        self.database = database

    # ==========================================
    # Main Menu
    # ==========================================

    def open_shop(self, player):

        while True:

            print("\n========== SHOP ==========")
            print(f"Gold : {player.gold}")

            print("\n1. Weapons")
            print("2. Armors")
            print("3. Potions")
            print("0. Exit")

            choice = input("\nChoose: ")

            if choice == "1":

                self.weapon_shop(player)

            elif choice == "2":

                self.armor_shop(player)

            elif choice == "3":

                self.potion_shop(player)

            elif choice == "0":

                break

            else:

                print("\nInvalid option.")

    # ==========================================
    # Weapons
    # ==========================================

    def weapon_shop(self, player):

        weapons = self.database.get_all_weapons()

        while True:

            print("\n========== WEAPONS ==========")

            for index, weapon in enumerate(
                weapons,
                start=1
            ):

                print(
                    f"{index}. "
                    f"{weapon.name}"
                    f" | ATK +{weapon.damage}"
                    f" | {weapon.price} Gold"
                )

            print("0. Back")

            try:

                choice = int(input("\nBuy: "))

            except ValueError:

                print("\nInvalid input.")
                continue

            if choice == 0:

                break

            if choice < 1 or choice > len(weapons):

                print("\nInvalid choice.")
                continue

            weapon = weapons[choice - 1]

            if not player.spend_gold(weapon.price):

                print("\nNot enough gold.")
                continue

            player.add_item(weapon)

            print(f"\nPurchased {weapon.name}!")

    # ==========================================
    # Armors
    # ==========================================

    def armor_shop(self, player):

        armors = self.database.get_all_armors()

        while True:

            print("\n========== ARMORS ==========")

            for index, armor in enumerate(
                armors,
                start=1
            ):

                print(
                    f"{index}. "
                    f"{armor.name}"
                    f" | DEF +{armor.defense_bonus}"
                    f" | {armor.price} Gold"
                )

            print("0. Back")

            try:

                choice = int(input("\nBuy: "))

            except ValueError:

                print("\nInvalid input.")
                continue

            if choice == 0:

                break

            if choice < 1 or choice > len(armors):

                print("\nInvalid choice.")
                continue

            armor = armors[choice - 1]

            if not player.spend_gold(armor.price):

                print("\nNot enough gold.")
                continue

            player.add_item(armor)

            print(f"\nPurchased {armor.name}!")

    # ==========================================
    # Potions
    # ==========================================

    def potion_shop(self, player):

        potions = self.database.get_all_potions()

        while True:

            print("\n========== POTIONS ==========")

            for index, potion in enumerate(
                potions,
                start=1
            ):

                print(
                    f"{index}. "
                    f"{potion.name}"
                    f" | {potion.price} Gold"
                )

            print("0. Back")

            try:

                choice = int(input("\nBuy: "))

            except ValueError:

                print("\nInvalid input.")
                continue

            if choice == 0:

                break

            if choice < 1 or choice > len(potions):

                print("\nInvalid choice.")
                continue

            potion = potions[choice - 1]

            if not player.spend_gold(potion.price):

                print("\nNot enough gold.")
                continue

            player.add_item(potion)

            print(f"\nPurchased {potion.name}!")