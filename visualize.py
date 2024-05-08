from pyvis.network import Network
from node import Node

def TreeSize(node: Node):
    nodes = [node]
    num_nodes = 0
    while len(nodes) > 0:
        num_nodes += 1
        current = nodes.pop(0)
        if current.children:
            for action in current.children:
                child = current.children[action]
                nodes.append(child)

    return num_nodes

def PrintNode(node: Node):
    net = Network(bgcolor = "#222222",
                font_color = "white",
                height = "750px",
                width = "100%",
                layout= "hierachical"
        )
    
    node_idx = 0
    nodes = [(node, node_idx)]
    net.add_node(node_idx)
    node_idx += 1
    while len(nodes) > 0:
        current, current_idx = nodes.pop(0)
        if current.children:
            for action in current.children:
                child = current.children[action]
                nodes.append((child, node_idx))
                net.add_node(node_idx, label=child.label())
                net.add_edge(current_idx, node_idx, label=str(action))
                node_idx += 1

    net.save_graph("graph.html")
        
    # nodes = list([1, 2, 3, 4, 5, 6, 7])
    # edges = [(1, 2), (2, 3), (2, 4), (2, 5), (5, 6), (6, 7)]
    # net.add_nodes(nodes)
    # net.add_edges(edges)