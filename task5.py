import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque
import matplotlib.animation as animation

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Tree Traversal"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    return tree, pos, colors, labels, title

def get_gradient_color(index, total_steps):
    start_rgb = (70, 70, 140)  # #000066
    end_rgb = (153, 204, 255)  # #99CCFF
    ratio = index / (total_steps - 1) if total_steps > 1 else 1
    r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
    g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
    b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)
    return f"#{r:02x}{g:02x}{b:02x}"

def dfs_traversal(root):
    if not root:
        return []
    order = []
    stack = [(root, 0)]
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        order.append(node)
        max_depth = max(max_depth, depth)
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))
    return order, max_depth

def bfs_traversal(root):
    if not root:
        return []
    order = []
    queue = deque([(root, 0)])
    max_depth = 0
    while queue:
        node, depth = queue.popleft()
        order.append(node)
        max_depth = max(max_depth, depth)
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return order, max_depth

def animate_traversal(root, t_type="dfs"):
    traversal_func = dfs_traversal if t_type == "dfs" else bfs_traversal
    order, max_depth = traversal_func(root)
    total_steps = len(order)

    # Ініціалізація кольорів
    for node in order:
        node.color = "#D3D3D3"  # Сірий для непройдених

    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_title(f"{t_type.upper()} Traversal")
    ax.axis('off')

    def update(frame):
        ax.clear()
        ax.set_title(f"{t_type.upper()} Traversal")
        ax.axis('off')
        if frame < total_steps:
            order[frame].color = get_gradient_color(frame, total_steps)
        tree, pos, colors, labels, _ = draw_tree(root)
        nx.draw(tree, pos=pos, labels = labels, arrows = False, node_size = 2100, node_color = colors, ax = ax)
        return []

    ani = animation.FuncAnimation(fig, update, frames=total_steps + 5, interval=500, repeat=False)
    plt.show()

def heap_to_tree(arr):
    if not arr:
        return None
    nodes = [Node(val) for val in arr]
    for i in range(len(arr)):
        if 2 * i + 1 < len(arr):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(arr):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

# Створення дерева
arr = [11, 6, 9, 4, 2, 7, 10, 1, 3, 5, 8, 12, 13, 14, 15]
heapq.heapify(arr)
root = heap_to_tree(arr)

# Візуалізація обходів
animate_traversal(root, "dfs")  # Обхід у глибину
animate_traversal(root, "bfs")  # Обхід у ширину