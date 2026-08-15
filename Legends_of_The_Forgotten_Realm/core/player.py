import random

from core.constants import (
    STARTING_GOLD,
    STARTING_LEVEL,
    STARTING_EXP,
    DEFAULT_CRIT_DAMAGE,
    BASE_EXP,
    EXP_MULTIPLIER,
    MAX_LEVEL,
    HP_PER_LEVEL,
    MANA_PER_LEVEL,
    ATTACK_PER_LEVEL,
    DEFENSE_PER_LEVEL,
    CRIT_CHANCE_PER_LEVEL
)


class Player:
    """
    Represents the player character.
    """

    def __init__(self, name: str, player_class, stats: dict):

        # ==========================
        # Basic Information
        # ==========================

        self.name = name
        self.player_class = player_class

        # ==========================
        # Progression
        # ==========================

        self.level = STARTING_LEVEL
        self.experience = STARTING_EXP
        self.gold = STARTING_GOLD

        self.bosses_defeated = 0
        self.highest_region_unlocked = 1
        self.enemies_defeated = 0

        # ==========================
        # Base Stats
        # ==========================

        self.max_hp = stats["max_hp"]
        self.hp = self.max_hp

        self.max_mana = stats["max_mana"]
        self.mana = self.max_mana

        self.base_attack = stats["attack"]
        self.base_defense = stats["defense"]

        self.crit_chance = stats["crit_chance"]
        self.crit_damage = DEFAULT_CRIT_DAMAGE

        # ==========================
        # Current Stats
        # ==========================

        self.attack = self.base_attack
        self.defense = self.base_defense

        # ==========================
        # Equipment
        # ==========================

        self.equipped_weapon = None
        self.equipped_armor = None

        # ==========================
        # Inventory
        # ==========================

        self.inventory = {
            "weapons": [],
            "armors": [],
            "potions": [],
            "materials": [],
            "quest_items": []
        }

    def __str__(self):

        return f"{self.name} ({self.player_class.value}) - Level {self.level}"

    # =====================================================
    # Inventory
    # =====================================================

    def add_item(self, item):

        class_name = item.__class__.__name__

        if class_name == "Weapon":
            self.inventory["weapons"].append(item)

        elif class_name == "Armor":
            self.inventory["armors"].append(item)

        elif class_name == "Potion":
            self.inventory["potions"].append(item)

        else:
            self.inventory["materials"].append(item)

    def remove_item(self, item):

        class_name = item.__class__.__name__

        if class_name == "Weapon":
            self.inventory["weapons"].remove(item)

        elif class_name == "Armor":
            self.inventory["armors"].remove(item)

        elif class_name == "Potion":
            self.inventory["potions"].remove(item)

# =====================================================
# Inventory Display
# =====================================================

    def show_inventory(self):

        print("\n========== INVENTORY ==========")

        self.show_weapons()
        self.show_armors()
        self.show_potions()

        print("===============================\n")


    def show_weapons(self):

        print("\nWeapons:")

        if not self.inventory["weapons"]:
            print("  None")
            return

        for index, weapon in enumerate(self.inventory["weapons"], start=1):

            equipped = ""

            if weapon == self.equipped_weapon:
                equipped = " [Equipped]"

            print(f"{index}. {weapon.name}{equipped}")


    def show_armors(self):

        print("\nArmors:")

        if not self.inventory["armors"]:
            print("  None")
            return

        for index, armor in enumerate(self.inventory["armors"], start=1):

            equipped = ""

            if armor == self.equipped_armor:
                equipped = " [Equipped]"

            print(f"{index}. {armor.name}{equipped}")


    def show_potions(self):

        print("\nPotions:")

        if not self.inventory["potions"]:
            print("  None")
            return

        for index, potion in enumerate(self.inventory["potions"], start=1):

            print(f"{index}. {potion.name}")

    # =====================================================
    # Weapon
    # =====================================================

    def equip_weapon(self, weapon):

        if self.level < weapon.required_level:

            print("\nYour level is too low to equip this weapon.")
            return False

        if self.equipped_weapon:

            self.unequip_weapon()

        self.equipped_weapon = weapon
        weapon.equip()

        self.attack += weapon.damage
        self.crit_chance += weapon.crit_bonus

        print(f"\nEquipped {weapon.name}")

        return True

    def unequip_weapon(self):

        if self.equipped_weapon is None:
            return

        self.attack -= self.equipped_weapon.damage
        self.crit_chance -= self.equipped_weapon.crit_bonus

        self.equipped_weapon.unequip()
        self.equipped_weapon = None

    # =====================================================
    # Armor
    # =====================================================

    def equip_armor(self, armor):

        if self.level < armor.required_level:

            print("\nYour level is too low to equip this armor.")
            return False

        if self.equipped_armor:

            self.unequip_armor()

        self.equipped_armor = armor
        armor.equip()

        self.defense += armor.defense_bonus

        self.max_hp += armor.hp_bonus
        self.hp += armor.hp_bonus

        self.max_mana += armor.mana_bonus
        self.mana += armor.mana_bonus

        print(f"\nEquipped {armor.name}")

        return True

# =====================================================
# Equip From Inventory
# =====================================================

    def equip_weapon_by_index(self, index):

        weapons = self.inventory["weapons"]

        if index < 0 or index >= len(weapons):
            print("\nInvalid weapon selection.")
            return

        self.equip_weapon(weapons[index])


    def equip_armor_by_index(self, index):

        armors = self.inventory["armors"]

        if index < 0 or index >= len(armors):
            print("\nInvalid armor selection.")
            return

        self.equip_armor(armors[index])

    def unequip_armor(self):

        if self.equipped_armor is None:
            return

        self.defense -= self.equipped_armor.defense_bonus

        self.max_hp -= self.equipped_armor.hp_bonus
        self.hp = min(self.hp, self.max_hp)

        self.max_mana -= self.equipped_armor.mana_bonus
        self.mana = min(self.mana, self.max_mana)

        self.equipped_armor.unequip()

        self.equipped_armor = None

    # =====================================================
    # Display
    # =====================================================

    def display_stats(self):

        weapon = (
            self.equipped_weapon.name
            if self.equipped_weapon
            else "None"
        )

        armor = (
            self.equipped_armor.name
            if self.equipped_armor
            else "None"
        )

        print("\n========== PLAYER STATS ==========")

        print(f"Name             : {self.name}")
        print(f"Class            : {self.player_class.value}")

        print(f"\nLevel            : {self.level}")
        print(f"Experience       : "f"{self.experience}/{self.get_exp_to_next_level()}"
        )

        print(f"\nHP               : {self.hp}/{self.max_hp}")
        print(f"Mana             : {self.mana}/{self.max_mana}")

        print(f"\nAttack           : {self.attack}")
        print(f"Defense          : {self.defense}")

        print(f"\nCritical Chance  : {self.crit_chance}%")
        print(f"Critical Damage  : {self.crit_damage}x")

        print(f"\nGold             : {self.gold}")

        print(f"\nWeapon           : {weapon}")
        print(f"Armor            : {armor}")

        print("\n==================================")

# =====================================================
# Combat
# =====================================================

    @property
    def is_alive(self):
        return self.hp > 0


    def take_damage(self, damage):

        damage = max(1, damage - self.defense)

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        return damage


    def basic_attack(self):
        """
        Returns the damage dealt by the player.
        Critical hits are applied automatically.
        """

        damage = self.attack

        critical_hit = False

        if random.randint(1, 100) <= self.crit_chance:

            damage = int(damage * self.crit_damage)
            critical_hit = True

        return damage, critical_hit

    def get_exp_to_next_level(self):

        return int(BASE_EXP * (EXP_MULTIPLIER ** (self.level - 1)))

    def gain_experience(self, exp):

        if self.level >= MAX_LEVEL:
            return

        self.experience += exp

        while (
            self.level < MAX_LEVEL
            and self.experience >= self.get_exp_to_next_level()
        ):

            self.experience -= self.get_exp_to_next_level()

            self.level_up()

    def level_up(self):

        self.level += 1

        self.max_hp += HP_PER_LEVEL
        self.hp = self.max_hp

        self.max_mana += MANA_PER_LEVEL
        self.mana = self.max_mana

        self.base_attack += ATTACK_PER_LEVEL
        self.base_defense += DEFENSE_PER_LEVEL

        self.attack += ATTACK_PER_LEVEL
        self.defense += DEFENSE_PER_LEVEL

        self.crit_chance += CRIT_CHANCE_PER_LEVEL

        print("\n=================================")
        print(f"🎉 LEVEL UP! You reached Level {self.level}")
        print("=================================")

# =====================================================
# Remove Item
# =====================================================

    def remove_item_by_index(self, category, index):

        items = self.inventory[category]

        if index < 0 or index >= len(items):

            print("\nInvalid selection.")
            return

        item = items[index]

        if item == self.equipped_weapon:

            self.unequip_weapon()

        if item == self.equipped_armor:

            self.unequip_armor()

        items.pop(index)

        print(f"\nRemoved {item.name}.")

# =====================================================
# Potions
# =====================================================

    def use_potion(self, index):

        potions = self.inventory["potions"]

        if index < 0 or index >= len(potions):

            print("\nInvalid potion selection.")
            return False

        potion = potions[index]

        if potion.potion_type == "Health":

            if self.hp == self.max_hp:
                print("\nHP is already full.")
                return False

            self.hp = min(self.max_hp, self.hp + potion.value)

            print(f"\nRecovered {potion.value} HP.")

        elif potion.potion_type == "Mana":

            if self.mana == self.max_mana:
                print("\nMana is already full.")
                return False

            self.mana = min(self.max_mana, self.mana + potion.value)

            print(f"\nRecovered {potion.value} Mana.")

        elif potion.potion_type == "Buff":

            print(f"\nUsed {potion.name}.")
            print("Buff effects will be implemented later.")

        potions.pop(index)

        return True

# =====================================================
# Gold
# =====================================================

    def spend_gold(self, amount):

        if amount > self.gold:

            return False

        self.gold -= amount

        return True