import random
import matplotlib.pyplot as plt

def calc_math_probability():
    dices_stats = {i: 0 for i in range(2, 13)}
    dices_stats['prob'] = {i: 0 for i in range(2, 13)}

    for i in range(2, 13):
        dices_stats[i] = 6 - abs(7 - i)
        dices_stats['prob'][i] = dices_stats[i] / 36

    return dices_stats

def get_y():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum_dice = dice1 + dice2
    return sum_dice

def calc_random_probability(count):
    dices_stats = {i: 0 for i in range(2, 13)}
    dices_stats['prob'] = {i: 0 for i in range(2, 13)}

    for _ in range(count):
        sum_dice = get_y()
        dices_stats[sum_dice] += 1

    for i in range(2, 13):
        dices_stats['prob'][i] = dices_stats[i] / count

    return dices_stats

def plot_probability(dices_stats):
    sums = list(dices_stats['prob'].keys())
    probabilities = list(dices_stats['prob'].values())

    bars = plt.bar(sums, probabilities, color='skyblue')
    # Додаємо значення на стовпці
    for bar, prob in zip(bars, probabilities):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{prob:.4f}', ha='center', va='bottom')

    plt.xlabel('Сума на двох кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність сум на двох кубиках')
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


count = 10000
dice_random_stats = calc_random_probability(count)
dice_math_stats = calc_math_probability()

print(f"Результати для {count} кидків кубика:")
for faces_sum, prob in dice_random_stats['prob'].items():
    print(f"Сума {faces_sum}: {prob:.2%} (математична: {dice_math_stats['prob'][faces_sum]:.2%}) відхилення: {abs(prob - dice_math_stats['prob'][faces_sum]):.4f}")

plot_probability(dice_random_stats)
