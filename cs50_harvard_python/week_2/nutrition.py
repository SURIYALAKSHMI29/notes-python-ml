"""

Question:
Iimplement a program that prompts users to input a fruit (case-insensitively) and then outputs the
number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available
as text. Ignore any input that isn’t a fruit.

"""


def get_calories(fruit: str) -> int:

    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }

    return fruit_calories.get(fruit.lower())


def main():
    fruit = input("Fruit: ").lower()
    calories = get_calories(fruit)
    if calories:
        print(f"Calories: {calories}")


if __name__ == "__main__":
    main()
