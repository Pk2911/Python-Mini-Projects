from core.database import GameDatabase
from core.player import Player
from core.enums import PlayerClass
from core.shop import Shop

db = GameDatabase()

player = Player(
    "Ajel",
    PlayerClass.WARRIOR,
    {
        "max_hp": 180,
        "max_mana": 60,
        "attack": 25,
        "defense": 12,
        "crit_chance": 5
    }
)

player.gold = 5000

shop = Shop(db)

shop.open_shop(player)

player.show_inventory()

print(f"\nRemaining Gold: {player.gold}")
