import random, pathlib

current_dir = pathlib.Path(__file__).parent

def get_random_joke():
    try:
        with open(current_dir / "jokes.txt", 'r', encoding="utf-8") as fh:
            jokes = fh.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError as e:
        return "Не смог найти файл с шутками"