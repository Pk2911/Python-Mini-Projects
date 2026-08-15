from core.weapon import Weapon
from core.enums import WeaponRarity
from core.armor import Armor
from core.enums import ArmorRarity
from core.potion import Potion
from core.enums import WeaponRarity, ArmorRarity
from core.enemy import Enemy
from core.boss import Boss

class Factory:

    @staticmethod
    def create_weapon(data):

        rarity = WeaponRarity(data["rarity"])

        return Weapon(
            item_id=data["id"],
            name=data["name"],
            rarity=rarity,
            damage=data["damage"],
            crit_bonus=data["crit_bonus"],
            price=data["price"],
            required_level=data["required_level"]
        )

    @staticmethod
    def create_armor(data):

        rarity = ArmorRarity(data["rarity"])

        return Armor(
            item_id=data["id"],
            name=data["name"],
            rarity=rarity,
            defense_bonus=data["defense_bonus"],
            hp_bonus=data["hp_bonus"],
            mana_bonus=data["mana_bonus"],
            crit_resistance=data["crit_resistance"],
            price=data["price"],
            required_level=data["required_level"]
        )

    @staticmethod
    def create_potion(data):

        return Potion(
            item_id=data["id"],
            name=data["name"],
            rarity=WeaponRarity(data["rarity"]),
            potion_type=data["potion_type"],
            value=data["value"],
            duration=data["duration"],
            price=data["price"],
            required_level=data["required_level"]
        )

    @staticmethod
    def create_enemy(data):

        return Enemy(
            enemy_id=data["id"],
            name=data["name"],
            level=data["level"],
            max_hp=data["max_hp"],
            attack=data["attack"],
            defense=data["defense"],
            experience=data["experience"],
            gold=data["gold"],
            drop_chance=data["drop_chance"],
            loot_type=data.get("loot_type", "Weapon")
        )

    @staticmethod
    def create_boss(data):

        return Boss(
            enemy_id=data["id"],
            name=data["name"],
            level=data["level"],
            max_hp=data["max_hp"],
            attack=data["attack"],
            defense=data["defense"],
            experience=data["experience"],
            gold=data["gold"],
            drop_chance=data["drop_chance"],
            loot_type=data.get("loot_type", "Weapon"),
            region=data["region"],
            title=data["title"]
        )