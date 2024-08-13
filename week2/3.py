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

    return res

def Path_to_Cycle(graph):
    all_nodes = [n for v in graph.values() for n in v]
    all_edges = list(graph.keys())
    comb_nodes = list(set(all_nodes + all_edges))

    # print("Graph:", graph)
    # print("All nodes:", all_nodes)
    # print("Combined nodes:", comb_nodes)

    don = None
    rec = None

    for n in comb_nodes:
        outdeg = all_nodes.count(n)
        indeg = len(graph.get(n, []))

        if indeg == outdeg:
            # print(f"{n} => Balanced")
            pass
        elif indeg < outdeg:
            print(f"{n} is unbalanced! {n} should be a donor")
            don = n
        elif indeg > outdeg:
            print(f"{n} is unbalanced! {n} should be a receiver")
            rec = n

        # print(f"\t{n} out-deg = {outdeg}")
        # print(f"\t{n} in-deg = {indeg}")

    print(f"Donor = {don}, Receiver = {rec}")

    if don is not None and rec is not None:
        if don not in graph:
            graph[don] = [rec]
        else:
            graph[don].append(rec)

    print("Updated Graph:", graph)
    return graph

def EulerianCycle(graph):
    # print(graph)
    # form a cycle Cycle by randomly walking in Graph
    # eulerian_path = [list(graph.keys())[0]]
    eulerian_path = [list(graph.values())[0][0]]
    current_node = eulerian_path[-1]
    # print(f"Initial Values: Path = {eulerian_path}, Node = {current_node}")

    db = {}

    # for i in range(20):
    while len(graph) != 0 or len(db) != 0:
        # print(eulerian_path)
        # print(graph)
        # print(current_node)
        # print(db)
        if current_node in graph:
            next_nodes = graph[current_node]
            # print(f"Next nodes: {next_nodes}")
            
            if len(next_nodes) == 1:
                eulerian_path.append(next_nodes[0])
                del graph[current_node]
            elif len(next_nodes) > 1:
                eulerian_path.append(next_nodes[0])
                graph[current_node] = graph[current_node][1:]
            
            current_node = eulerian_path[-1]
        elif current_node not in graph:
            if current_node in db:
                eulerian_path = eulerian_path + db[current_node]
                del db[current_node]
            else:
                for n in range(len(eulerian_path)-1):
                    # print(f"Checkpoint: {eulerian_path[n]}")
                    node_checkpoint = eulerian_path[n]
                    if node_checkpoint in graph:
                        # print(f"{node_checkpoint} can divert path")
                        db[node_checkpoint] = eulerian_path[n+1:]
                        eulerian_path = eulerian_path[:n+1]
                        current_node = node_checkpoint
                        break
        
        # print(eulerian_path)
        # print(graph)
        # print(current_node)
        # print(f"Ending iteration {i}")

    # print(eulerian_path)
    cycle_to_path = eulerian_path
    # cycle_to_path = eulerian_path[:-1]
    return cycle_to_path

def combine_by_last2(kmers):
    """Working"""
    last = kmers[-1]
    first = "".join([kmers[i][0] for i in range(len(kmers)-1)])
    genome = first+last
    return genome


def main():
    print("Started!\n")

    kmers = []
    # 3.sam.log
    # StringReconstruction\inputs\input_5
    with open("3.test.log") as file:
        k = file.readline().strip()
        data = file.readline().strip()
        # print(data)
        kmers = data.split()
        print(kmers)

    print("Data collected from the file/hardcoded list.\n")
    dbruijnGraph = deBruijnGraph(kmers)
    print("Built De-bruijn Graph!\n")
    cycle = Path_to_Cycle(dbruijnGraph)
    print("Finding unconnected nodes.\n")
    path = EulerianCycle(cycle)
    print("Path calculated\n")
    print(path)
    print("Final Output\n")
    print(" ".join(path))
    print("Gluing nodes together\n")
    seq = combine_by_last2(path)
    print(seq)

if __name__ == "__main__":
    main()

