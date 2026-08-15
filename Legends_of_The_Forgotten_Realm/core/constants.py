from pathlib import Path

GAME_TITLE = "Legends of the Forgotten Realm"

# ===============================
# Player Constants
# ===============================

MAX_LEVEL = 100

STARTING_LEVEL = 1
STARTING_EXP = 0
STARTING_GOLD = 100

DEFAULT_CRIT_DAMAGE = 1.5

# ===============================
# Game Constants
# ===============================

DEFEND_DAMAGE_REDUCTION = 0.5
LEVELS_PER_REGION = 10

# ===============================
# Project Directories
# ===============================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIRECTORY = PROJECT_ROOT / "data"
SAVE_DIRECTORY = PROJECT_ROOT / "saves"

# ===============================
# Level System
# ===============================

MAX_LEVEL = 100

BASE_EXP = 100
EXP_MULTIPLIER = 1.25

HP_PER_LEVEL = 12
MANA_PER_LEVEL = 6
ATTACK_PER_LEVEL = 3
DEFENSE_PER_LEVEL = 2
CRIT_CHANCE_PER_LEVEL = 0.2