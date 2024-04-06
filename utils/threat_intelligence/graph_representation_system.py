class SystemGraph:
    def __init__(self):
        self.nodes = []  # List of system components
        self.edges = []  # List of tuples (source_component, target_component)

    def add_component(self, component):
        self.nodes.append(component)

    def add_interaction(self, source, target):
        self.edges.append((source, target))

    def visualize(self):
        # Placeholder for graph visualization logic
        # Could use libraries like NetworkX or Graphviz for visualization
        pass
