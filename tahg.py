import networkx as nx
import json
import csv
from collections import defaultdict

class TextAttributedHypergraph:
    def __init__(self):
        self.hypergraph = nx.Graph()  # Using bipartite graph to model hypergraph
        self.node_attributes = {}  # Store text attributes for MeSH codes

    def add_hyperedge(self, hyperedge_id, mesh_codes, abstract_text):
        """ Adds a hyperedge (abstract) connecting multiple MeSH codes. """
        self.hypergraph.add_node(hyperedge_id, type="hyperedge", text=abstract_text)
        for mesh_code in mesh_codes:
            if mesh_code not in self.hypergraph:
                self.hypergraph.add_node(mesh_code, type="node")
            self.hypergraph.add_edge(mesh_code, hyperedge_id)  # Connect MeSH code to hyperedge

    def set_text_attributes(self, mesh_definitions):
        """ Assign text attributes (definitions) to MeSH nodes. """
        for mesh_code, definition in mesh_definitions.items():
            if mesh_code in self.hypergraph:
                self.hypergraph.nodes[mesh_code]['text_attribute'] = definition

    def save_hypergraph(self, filename="tahg.json"):
        """ Saves the hypergraph structure to a JSON file. """
        data = {
            "nodes": {n: self.hypergraph.nodes[n] for n in self.hypergraph.nodes},
            "edges": list(self.hypergraph.edges)
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Hypergraph saved to {filename}")

    def load_data_from_csv(self, mesh_file, abstract_file):
        """ Loads MeSH codes and abstracts from CSV files. """
        mesh_definitions = {}
        with open(mesh_file, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                mesh_code, definition = row
                mesh_definitions[mesh_code] = definition

        abstract_data = defaultdict(list)
        with open(abstract_file, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                abstract_id, mesh_codes, abstract_text = row[0], row[1].split(";"), row[2]
                abstract_data[abstract_id] = (mesh_codes, abstract_text)

        return mesh_definitions, abstract_data
