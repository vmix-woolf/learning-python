from joke import get_random_joke

def main():
    name = input("Введите свое имя:")
    print(f"Приветствую тебя, {name}")

    while True:
        user_response = input(f"{name}, бажаєте почути анекдот? (так/ні): ").lower()
        if user_response == "так":
            print(get_random_joke())
        elif user_response == "ні":
            print(f"До побачення, {name}!")
            break

if __name__ == '__main__':
    main()