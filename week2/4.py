import itertools

# using stackoverflow to generate binary combinations
def generate_unique_binary_kmers(k):
    lst = list(itertools.product([0, 1], repeat=k))
    kmers = [list(_) for _ in lst]
    print(f"Generated {len(kmers)} unique combinations")
    text_kmers = ["".join(map(str, c)) for c in kmers]

    return text_kmers

def debruijn_graph(kmers):
    graph = {}
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        if prefix in graph:
            graph[prefix].append(suffix)
        elif prefix not in graph:
            graph[prefix] = [suffix]

    return graph

def eulerian_cycle(graph):
    all_nodes = list(graph.keys())
    circuit = [all_nodes[0]]
    current_node = circuit[-1]
    db = {}
    while len(graph) != 0 or len(db) != 0:
        if current_node in graph:
            next_node = graph[current_node]
            if len(next_node) == 1:
                circuit.append(next_node[0])
                del graph[current_node]
            elif len(next_node) > 1:
                circuit.append(next_node[0])
                graph[current_node] = graph[current_node][1:]
            current_node = circuit[-1]
            # print(f"node changed code: {1}")
        if current_node not in graph:
            if current_node in db:
                circuit = circuit + db[current_node]
                del db[current_node]
                # print(f"node changed code: {4}")
            else:
                for i in range(len(circuit)):
                    node = circuit[i]
                    if node in graph:
                        db[node] = circuit[i+1:]
                        circuit = circuit[:i+1]
                        current_node =circuit[-1]
                        # print(f"node changed code: {5}")
                        break
    return circuit

def glue_bin_nodes(cycle):
    return "".join([n[0] for n in cycle[1:]])

def universal_string(k):
    str_kmers = generate_unique_binary_kmers(k)
    dbjn_graph = debruijn_graph(str_kmers)
    cycle = eulerian_cycle(dbjn_graph)
    glued = glue_bin_nodes(cycle)

    # print(cycle)
    print(glued)
    return glued

universal_string(9)