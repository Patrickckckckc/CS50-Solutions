fruits_kcal = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloup": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Melon": 50,
    "Kiwi": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Cherries": 100
}

item = input("Item: ").lower().capitalize()
if item in fruits_kcal.keys():
    print(f"Calories: {fruits_kcal[item]}")

