recipes = {
    "bean": {"Gunpowder": 60},
    "explosives": {"Gunpowder": 50, "Sulfur": 10, "---> Total Sulfur": 110},
    "explosive bullet": {"Gunpowder": 10, "Sulfur": 5, "---> Total Sulfur": 25},
    "fart": {"Bean Grenade": 4, "---> Total Gunpowder": 240, "---> Total Sulfur": 480},
    "rocket": {"Gunpowder": 150, "Explosives": 10, "---> Total Gunpowder": 650, "---> Total Sulfur": 1400},
    "c4": {"Explosives": 20, "---> Total Gunpowder": 1000, "---> Total Sulfur": 2200}
}

def calculate(recipe, quantity=1):
    total = {}
    for item, qty in recipes[recipe].items():
        total[item] = qty * quantity
    return total

def display(total):
    for item, qty in total.items():
        print(f"{item}: {qty}")

def main():
    while True:
        print("Choose a recipe:")
        for recipe in recipes:
            print(recipe)
        choice = input("Enter your choice from the list (or type 'exit' to quit): ")
        if choice.lower() == "exit":
            break
        if choice.lower() in recipes:
            amount = int(input("Enter the quantity you desire: "))
            result = calculate(choice, amount)
            display(result)
        else:
            print("Recipe not found. Please try again.")

if __name__ == "__main__":
    main()
