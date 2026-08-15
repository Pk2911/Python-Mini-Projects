from core.char_creation import create_character
from core.database import GameDatabase
from core.save_manager import SaveManager
from core.world import World
from core.shop import Shop


class Game:

    def __init__(self):

        self.database = GameDatabase()

        self.world = World(self.database)

        self.shop = Shop(self.database)
        self.save_manager = SaveManager(self.database)

        self.player = None
        self.running = True

    def start(self):

        while self.running:

            self.main_menu()

    def main_menu(self):

        print("\n===============================")
        print(" LEGENDS OF THE FORGOTTEN REALM")
        print("===============================")

        print("1. New Game")
        print("2. Continue")
        print("3. Instructions")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            self.new_game()

        elif choice == "2":

            self.continue_game()

        elif choice == "3":

            self.instructions()

        elif choice == "4":

            print("\nThanks for playing!")

            self.running = False

        else:

            print("\nInvalid choice!")

    def new_game(self):

        self.player = create_character()

        self.game_menu()

    def instructions(self):

        print("\n========== HOW TO PLAY ==========")

        print("Defeat enemies.")
        print("Collect equipment.")
        print("Defeat bosses.")
        print("Reach Level 100.")
        print("Defeat the Ancient Demon King.")

        input("\nPress Enter to continue...")

    def continue_game(self):

        if not self.save_manager.save_exists():
            print("\nNo save file found.")
            return

        player = self.save_manager.load_game()

        if player is None:
            print("\nSave file is missing or corrupted.")
            return

        self.player = player
        self.game_menu()

    def game_menu(self):

        while True:

            print("\n========== VILLAGE ==========\n")

            print("1. Explore")
            print("2. Shop")
            print("3. Inventory")
            print("4. Player Stats")
            print("5. Save Game")
            print("6. Return to Main Menu")

            choice = input("\nChoose: ")

            if choice == "1":

                self.world.explore(self.player)

            elif choice == "2":

                self.shop.open_shop(self.player)

            elif choice == "3":

                self.player.show_inventory()

                input("\nPress Enter...")

            elif choice == "4":

                self.player.display_stats()

                input("\nPress Enter...")

            elif choice == "5":

                self.save_manager.save_game(self.player)
                print("\nGame saved successfully!")

            elif choice == "6":

                break

            else:

                print("\nInvalid choice.")