import pandas as pd

# Sample data
data = pd.DataFrame({
    'bacteria': ['Klebsiella', 'Klebsiella', 'E. coli', 'E. coli', 'Pseudomonas', 'Acinetobacter'],
    'mecanismo': ['KPC', 'NDM', 'NDM', 'CTX-M', 'VIM', 'OXA-48']
})

# Create graph from edges
G = nx.from_pandas_edgelist(data, source='bacteria', target='mecanismo')

# Draw
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=1800, edge_color="black", font_size=9)
plt.title("Red de bacterias y mecanismos de resistencia")
plt.show()
