import json
class DataLoader:

    @staticmethod
    def load_json(path: str):

        try:

            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:

            print(f"\nERROR: {path} not found.")
            return []

        except json.JSONDecodeError:

            print(f"\nERROR: Invalid JSON in {path}")
            return []