import json
from core.player import Player
from core.enums import PlayerClass
from core.data_loader import DataLoader

classes = DataLoader.load_json("data/classes.json")

def create_character():
    """
    Creates and returns a new Player object.
    """

    print("\n========== CHARACTER CREATION ==========\n")

    while True:

        player_name = input("Enter Player Name: ").strip()

        if player_name:
            break

        print("Player name cannot be empty.\n")

    print("\nChoose Your Class")
    print("-----------------------")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Assassin")

    CLASS_OPTIONS = {
    "1": PlayerClass.WARRIOR,
    "2": PlayerClass.MAGE,
    "3": PlayerClass.ARCHER,
    "4": PlayerClass.ASSASSIN
}

    while True:

        choice = input("\nEnter choice (1-4): ")

        selected_class = CLASS_OPTIONS[choice]

        stats = classes[selected_class.value]

        player = Player(
        player_name,
        selected_class,
        stats
    )

        print("\nCharacter Created Successfully!")

        return player