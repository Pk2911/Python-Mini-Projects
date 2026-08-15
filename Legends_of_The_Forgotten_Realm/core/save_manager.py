import json
from pathlib import Path

from core.constants import SAVE_DIRECTORY
from core.enums import PlayerClass


class SaveManager:

    def __init__(self, database):

        self.database = database
        self.save_path = SAVE_DIRECTORY / "savegame.json"

        SAVE_DIRECTORY.mkdir(parents=True, exist_ok=True)

    def _serialize_inventory_ids(self, items):

        return [getattr(item, "item_id", item) for item in items]

    def save_game(self, player):

        data = {
            "name": player.name,
            "player_class": player.player_class.value,
            "level": player.level,
            "experience": player.experience,
            "gold": player.gold,
            "hp": player.hp,
            "max_hp": player.max_hp,
            "mana": player.mana,
            "max_mana": player.max_mana,
            "attack": player.attack,
            "defense": player.defense,
            "crit_chance": player.crit_chance,
            "crit_damage": player.crit_damage,
            "bosses_defeated": player.bosses_defeated,
            "enemies_defeated": player.enemies_defeated,
            "highest_region_unlocked": player.highest_region_unlocked,
            "equipped_weapon": player.equipped_weapon.item_id if player.equipped_weapon else None,
            "equipped_armor": player.equipped_armor.item_id if player.equipped_armor else None,
            "inventory": {
                "weapons": self._serialize_inventory_ids(player.inventory["weapons"]),
                "armors": self._serialize_inventory_ids(player.inventory["armors"]),
                "potions": self._serialize_inventory_ids(player.inventory["potions"]),
                "materials": self._serialize_inventory_ids(player.inventory["materials"]),
                "quest_items": self._serialize_inventory_ids(player.inventory["quest_items"]),
            }
        }

        with open(self.save_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    def load_game(self):

        if not self.save_path.exists():
            return None

        try:
            with open(self.save_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (json.JSONDecodeError, OSError):
            return None

        if not isinstance(data, dict):
            return None

        try:
            player_class = PlayerClass(data["player_class"])
        except (KeyError, ValueError):
            return None

        from core.player import Player

        player = Player(
            data.get("name", "Player"),
            player_class,
            {
                "max_hp": data.get("max_hp", 100),
                "max_mana": data.get("max_mana", 50),
                "attack": data.get("attack", 10),
                "defense": data.get("defense", 10),
                "crit_chance": data.get("crit_chance", 5)
            }
        )

        player.level = data.get("level", 1)
        player.experience = data.get("experience", 0)
        player.gold = data.get("gold", 100)
        player.hp = data.get("hp", player.max_hp)
        player.mana = data.get("mana", player.max_mana)
        player.attack = data.get("attack", player.attack)
        player.defense = data.get("defense", player.defense)
        player.crit_chance = data.get("crit_chance", player.crit_chance)
        player.crit_damage = data.get("crit_damage", player.crit_damage)
        player.bosses_defeated = data.get("bosses_defeated", 0)
        player.enemies_defeated = data.get("enemies_defeated", 0)
        player.highest_region_unlocked = data.get("highest_region_unlocked", 1)

        inventory_data = data.get("inventory", {})

        for weapon_id in inventory_data.get("weapons", []):
            weapon = self.database.get_weapon(weapon_id)
            if weapon is not None:
                player.add_item(weapon)

        for armor_id in inventory_data.get("armors", []):
            armor = self.database.get_armor(armor_id)
            if armor is not None:
                player.add_item(armor)

        for potion_id in inventory_data.get("potions", []):
            potion = self.database.get_potion(potion_id)
            if potion is not None:
                player.add_item(potion)

        for material_id in inventory_data.get("materials", []):
            if material_id is not None:
                player.inventory["materials"].append(material_id)

        for quest_item_id in inventory_data.get("quest_items", []):
            if quest_item_id is not None:
                player.inventory["quest_items"].append(quest_item_id)

        equipped_weapon_id = data.get("equipped_weapon")
        if equipped_weapon_id:
            weapon = next(
                (item for item in player.inventory["weapons"] if item.item_id == equipped_weapon_id),
                None
            )

            if weapon is None:
                weapon = self.database.get_weapon(equipped_weapon_id)
                if weapon is not None:
                    player.add_item(weapon)

            if weapon is not None:
                player.equipped_weapon = weapon
                weapon.equip()

        equipped_armor_id = data.get("equipped_armor")
        if equipped_armor_id:
            armor = next(
                (item for item in player.inventory["armors"] if item.item_id == equipped_armor_id),
                None
            )

            if armor is None:
                armor = self.database.get_armor(equipped_armor_id)
                if armor is not None:
                    player.add_item(armor)

            if armor is not None:
                player.equipped_armor = armor
                armor.equip()

        return player

    def save_exists(self):

        return self.save_path.exists()
