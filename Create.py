import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
terms = [
    
]
G.add_nodes_from(terms)

# Add edges to represent relationships
edges = [
    
]

G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Layout for visualization
nx.draw(
    G, pos, with_labels=True, node_size=3000, node_color='green', 
    font_size=10, font_weight='bold', arrows=True, arrowstyle='-|>', 
    arrowsize=20
)
plt.title("Your Title Here")
plt.show()
