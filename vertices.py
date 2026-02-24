import matplotlib.pyplot as plt
import networkx as nx


num_vertices = int(input("Enter number of vertices (>=3): "))
if num_vertices < 3:
    print("Number of vertices must be at least 3.")
    exit()

vertex_labels = []
for i in range(num_vertices):
    label = input(f"Enter label for vertex {i+1}: ")
    vertex_labels.append(label)

G = nx.complete_graph(num_vertices)


plt.figure(figsize=(8, 6))
pos = nx.circular_layout(G)  


labels = {i: vertex_labels[i] for i in range(num_vertices)}

nx.draw(
    G, pos,
    with_labels=True,
    labels=labels,         
    node_color='skyblue',
    node_size=1000,
    font_size=12,
    edge_color='gray'
)

plt.title("Complete Graph with User-Defined Vertices")
plt.show()
