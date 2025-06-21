import matplotlib.pyplot as plt
import math

def draw_branch(start, length, angle, depth, max_depth):
    if depth > max_depth:
        return

    x2 = start[0] + length * math.cos(math.radians(angle))
    y2 = start[1] + length * math.sin(math.radians(angle))
    end = (x2, y2)

    plt.plot([start[0], end[0]], [start[1], end[1]], 'k-', linewidth=1)

    new_length = length * (math.sqrt(2) / 2)  # Коефіцієнт зменшення
    draw_branch(end, new_length, angle + 45, depth + 1, max_depth)  # Права 
    draw_branch(end, new_length, angle - 45, depth + 1, max_depth)  # Ліва 

def plot_pythagoras_tree(max_depth):
    plt.figure(figsize=(7, 7))
    plt.axis('off')    

    initial_length = 2.0
    start_pos = (0, -2)  # Початок дерева
    initial_angle = 90   # Вертикальний напрямок

    draw_branch(start_pos, initial_length, initial_angle, 0, max_depth)

    plt.title(f"Pythagoras Tree (Recursion depth: {max_depth})")
    plt.show()

if __name__ == "__main__":
    max_depth = 7 # Рівень рекурсії 
    plot_pythagoras_tree(max_depth)