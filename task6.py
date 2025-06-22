
def greedy_algorithm(amount, items):
    item_list = [(name, item['cost'], item['calories'], item['cost']/item['calories']) for name, item in items.items()]
    item_list.sort(key=lambda x: x[3])  # Сортуємо за вартістю/калоріями

    total_cost = 0
    total_calories = 0
    used = {}
    for name, cost, calories in item_list:
        if total_cost + cost <= amount:
            total_cost += cost
            total_calories += calories
            used[name] = used.get(name, 0) + 1

    return total_cost, total_calories, used

def dynamic_programming(amount, items):
    item_list = [(name, item['cost'], item['calories']) for name, item in items.items()]
    n = len(item_list)

    dp = [-float('inf')] * (amount + 1)
    dp[0] = 0  # Нульовий бюджет дає нуль калорій
    used = [{} for _ in range(amount + 1)]  
    min_cost = [float('inf')] * (amount + 1)  # Мінімальна вартість для досягнення калорій
    min_cost[0] = 0

    for i in range(n):
        name, cost, calories = item_list[i]
        for budget in range(amount, cost - 1, -1):  
            if dp[budget - cost] + calories > dp[budget]:
                dp[budget] = dp[budget - cost] + calories
                min_cost[budget] = min_cost[budget - cost] + cost
                used[budget] = used[budget - cost].copy()
                used[budget][name] = used[budget].get(name, 0) + 1
                print(used[budget].get(name, 0) + 1)
                print(used[budget].get(name, 0))
            elif dp[budget - cost] + calories == dp[budget] and min_cost[budget - cost] + cost < min_cost[budget]:
                min_cost[budget] = min_cost[budget - cost] + cost
                used[budget] = used[budget - cost].copy()
                used[budget][name] = used[budget].get(name, 0) + 1

    max_calories = max(dp)
    optimal_budget = min(i for i in range(amount + 1) if dp[i] == max_calories and min_cost[i] != float('inf'))

    return min_cost[optimal_budget], max_calories, used[optimal_budget]


def main():

    items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

    amount = 70
    min_cost, max_calories, combination = dynamic_programming(amount, items)

    print('Динамичне програмування.')
    print(f"Мінімальний бюджет {min_cost}: {max_calories} калорій")
    print("Комбінація продуктів:")
    for item, count in combination.items():
        print(f"{item}: {count} шт. (вартість {items[item]['cost']} грн, калорії {items[item]['calories']})")

    print('Жадібний алгоритм.')
    print(f"Мінімальний бюджет {min_cost}: {max_calories} калорій")
    print("Комбінація продуктів:")
    for item, count in combination.items():
        print(f"{item}: {count} шт. (вартість {items[item]['cost']} грн, калорії {items[item]['calories']})")

if __name__ == "__main__":
    main()


















