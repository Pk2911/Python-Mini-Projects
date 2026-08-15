import json
import copy

import random
from core.factory import Factory
from core.constants import DATA_DIRECTORY

class GameDatabase:
    """
    Loads and stores all game data.
    """

    def __init__(self):

        self.weapons = []
        self.armors = []
        self.potions = []
        self.enemies = []
        self.bosses = []

        self.load_all()

    def load_json(self, filename):

        with open(DATA_DIRECTORY / filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def load_all(self):

        self.weapons = [
            Factory.create_weapon(data)
            for data in self.load_json("weapons.json")
        ]

        self.armors = [
            Factory.create_armor(data)
            for data in self.load_json("armors.json")
        ]

        self.potions = [
        Factory.create_potion(data)
        for data in self.load_json("potions.json")
    ]

        self.enemies = [
        Factory.create_enemy(data)
        for data in self.load_json("enemies.json")
    ]

        self.bosses = [
        Factory.create_boss(data)
        for data in self.load_json("bosses.json")
    ]
        
    def get_weapon(self, weapon_id):

        for weapon in self.weapons:

            if weapon.item_id == weapon_id:
                return copy.deepcopy(weapon)

        return None

    def get_armor(self, armor_id):

        for armor in self.armors:

            if armor.item_id == armor_id:
                return copy.deepcopy(armor)

        return None

    def get_potion(self, potion_id):

        for potion in self.potions:

            if potion.item_id == potion_id:
                return copy.deepcopy(potion)

        return None


    def get_all_weapons(self):

        return self.weapons


    def get_all_armors(self):

        return self.armors


    def get_all_potions(self):

        return self.potions

    def random_weapon(self, player_level):

        weapons = [
            weapon
            for weapon in self.weapons
            if weapon.required_level <= player_level
        ]

        return copy.deepcopy(random.choice(weapons))

    def random_armor(self, player_level):

        armors = [
            armor
            for armor in self.armors
            if armor.required_level <= player_level
        ]

        return copy.deepcopy(random.choice(armors))

    def random_potion(self):

        return copy.deepcopy(random.choice(self.potions))

    def get_enemy(self, enemy_id):

        for enemy in self.enemies:

            if enemy.enemy_id == enemy_id:

                return copy.deepcopy(enemy)

        return None


    def get_boss(self, boss_id):

        for boss in self.bosses:

            if boss.enemy_id == boss_id:
                return copy.deepcopy(boss)

        return None