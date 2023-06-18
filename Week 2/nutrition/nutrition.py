# food_details: dict = {}
# with open('food.csv', 'r') as f:
#     for row in f.readlines():
#         r = row.strip().split(',')
#         food_details[r[0].lower()] = int(r[1])
#     f.close()

food_details: dict = {'apple': 130, 'avocado': 50, 'banana': 110, 'cantaloupe': 50, 'grapefruit': 60, 'grapes': 90, 'honeydew': 50, 'kiwifruit': 90, 'lemon': 15, 'lime': 20, 'nectarine': 60, 'orange': 80, 'peach': 60, 'pear': 100, 'pineapple': 50, 'plums': 70, 'strawberries': 50, 'sweet cherries': 100, 'tangerine': 50, 'watermelon': 80}

def getCaloriesByFood(food_name: str) -> str:
    return str(food_details[food_name.lower()])

def main():
    inp = input("-> ")

    if inp.strip().lower() in food_details:
        print("Calories: " + getCaloriesByFood(inp.strip()))

if __name__ == "__main__":
    main()