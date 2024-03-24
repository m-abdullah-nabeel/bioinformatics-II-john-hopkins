patterns = ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"]

def edges_to_nodes(edges):
    nodes = []
    for e in edges:
        prefix = e[:-1]
        nodes.append(prefix)
        suffix = e[1:]
        nodes.append(suffix)
    
    nodes = list(set(nodes))
    return nodes

def pathgraph(kmers):
    graph = {}
    for kmer in kmers:
        suffix = kmer[1:]
        prefix = kmer[:-1]
        if prefix in graph:
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]
    return graph

def deBruijnGraph(patterns = patterns):
    res = pathgraph(patterns)

    for k in (sorted(res.keys())):
        print(k + ": " + " ".join(sorted(res[k])))

    
with open("5.test.log") as file:
    text = file.readline()
    edges = text.split(" ")
    deBruijnGraph(patterns=edges)
