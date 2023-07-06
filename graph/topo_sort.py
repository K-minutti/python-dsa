from graphviz import Digraph

class Node:
    def __init__(self, value: int, children: list= None):
        self.value = value
        self.children = children



def trace(root):
    # builds a set of all nodes and edges in graph
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            if v.children:
                for child in v.children:
                    edges.add((child, v))
                    build(child)
                
    build(root)
    return nodes, edges

def draw_dot(root):
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'})
    # LR = left to right
    
    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        # for any value in the graph, create a rectangular 'record' node for it
        dot.node(name=uid, label = "{ data %.1f }" % (n.value,), shape='record')
    for n1, n2 in edges:
        # connect n1 to the op node of n2
        dot.edge(str(id(n1)), str(id(n2)))

    return dot
        
n2 = Node(2)
n3 = Node(3) 
n1 = Node(1, [n2, n3])
print(draw_dot(n1))

