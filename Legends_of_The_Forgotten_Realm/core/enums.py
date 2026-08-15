from enum import Enum


class PlayerClass(Enum):
    WARRIOR = "Warrior"
    MAGE = "Mage"
    ARCHER = "Archer"
    ASSASSIN = "Assassin"


class WeaponRarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    SUPER_RARE = "Super Rare"
    EPIC = "Epic"
    MYTHICAL = "Mythical"
    LEGENDARY = "Legendary"


class ArmorRarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    SUPER_RARE = "Super Rare"
    EPIC = "Epic"
    MYTHICAL = "Mythical"
    LEGENDARY = "Legendary"


class PotionType(Enum):
    HEALTH = "Health"
    MANA = "Mana"
    MIXED = "Mixed"
    BUFF = "Buff"