import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.database import GameDatabase
from core.save_manager import SaveManager
from core.player import Player
from core.enums import PlayerClass


def test_database_loads_without_missing_enemy_loot_fields():
    db = GameDatabase()

    assert len(db.enemies) > 0
    assert len(db.bosses) > 0
    assert db.enemies[0].loot_type in {"Weapon", "Armor"}


def test_save_and_load_round_trip_restores_player_state():
    db = GameDatabase()
    save_manager = SaveManager(db)

    player = Player(
        "Ariel",
        PlayerClass.WARRIOR,
        {
            "max_hp": 180,
            "max_mana": 60,
            "attack": 25,
            "defense": 12,
            "crit_chance": 5
        }
    )

    player.level = 7
    player.experience = 250
    player.gold = 420
    player.hp = 150
    player.mana = 55
    player.attack = 35
    player.defense = 18
    player.crit_chance = 8
    player.crit_damage = 2.0
    player.bosses_defeated = 2
    player.enemies_defeated = 18
    player.highest_region_unlocked = 3
    weapon = db.get_weapon("WPN001")
    armor = db.get_armor("ARM001")
    player.inventory["weapons"].append(weapon)
    player.inventory["armors"].append(armor)
    player.inventory["potions"].append(db.get_potion("POT001"))

    player.equipped_weapon = weapon
    player.equipped_armor = armor
    weapon.equip()
    armor.equip()

    save_manager.save_game(player)
    loaded_player = save_manager.load_game()

    assert loaded_player is not None
    assert loaded_player.name == "Ariel"
    assert loaded_player.level == 7
    assert loaded_player.experience == 250
    assert loaded_player.gold == 420
    assert loaded_player.hp == 150
    assert loaded_player.max_hp == 180
    assert loaded_player.mana == 55
    assert loaded_player.max_mana == 60
    assert loaded_player.attack == 35
    assert loaded_player.defense == 18
    assert loaded_player.crit_chance == 8
    assert loaded_player.crit_damage == 2.0
    assert loaded_player.bosses_defeated == 2
    assert loaded_player.enemies_defeated == 18
    assert loaded_player.highest_region_unlocked == 3
    assert len(loaded_player.inventory["weapons"]) == 1
    assert len(loaded_player.inventory["armors"]) == 1
    assert len(loaded_player.inventory["potions"]) == 1
    assert loaded_player.equipped_weapon is not None
    assert loaded_player.equipped_armor is not None
    assert loaded_player.equipped_weapon.item_id == "WPN001"
    assert loaded_player.equipped_armor.item_id == "ARM001"
