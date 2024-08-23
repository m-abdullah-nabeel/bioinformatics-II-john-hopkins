def deBruijnGraph(kmers):
    graph = {}
    for kmer in kmers:
        suffix = kmer[1:]
        prefix = kmer[:-1]
        if prefix in graph:
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]

    # for k in (sorted(res.keys())):
    #     print(k + ": " + " ".join(sorted(res[k])))
    return graph

def EulerianPath(graph, kmers):
    all_nodes = [n for v in graph.values() for n in v]
    all_edges = list(graph.keys())
    comb_nodes = list(set(all_nodes + all_edges))

    print("Graph:", graph)
    print("All nodes:", all_nodes)
    print("Combined nodes:", comb_nodes)

    don = None
    rec = None

    for n in comb_nodes:
        outdeg = all_nodes.count(n) # names are probab reversed!! but working
        indeg = len(graph.get(n, []))

        if indeg == outdeg:
            # print(f"{n} => Balanced")
            continue
        elif indeg < outdeg:
            print(f"{n} is unbalanced! {n} should be a donor")
            don = n
        elif indeg > outdeg:
            print(f"{n} is unbalanced! {n} should be a receiver")
            rec = n

        print(f"\t{n} out-deg = {outdeg}")
        print(f"\t{n} in-deg = {indeg}")
    print(f"Donor = {don}, Receiver = {rec}")

    # if don is not None and rec is not None:
    #     if don not in graph:
    #         graph[don] = [rec]
    #     else:
    #         graph[don].append(rec)
    print("Updated Graph:", graph)

    eulerian_path = [all_edges[0]]
    if rec:
        eulerian_path = [rec]
    current_node = eulerian_path[-1]

    # print(len(all_edges))
    # print(len(all_edges[0]))
    # print(f"Initial Values: Path = {eulerian_path}, Node = {current_node}")
    
    db = {}
    while len(graph) != 0 or len(db) != 0:
        # print(eulerian_path)
        # print(graph)
        # print(current_node)
        # print(db)
        if current_node in graph:
            next_nodes = graph[current_node]
            # print(f"Next nodes: {next_nodes}")
            eulerian_path.append(next_nodes[0])
            
            if len(next_nodes) == 1:
                # eulerian_path.append(next_nodes[0])
                del graph[current_node]
            elif len(next_nodes) > 1:
                # eulerian_path.append(next_nodes[0])
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
        
    print(eulerian_path)
    seq = combine_by_last2(eulerian_path)
    path = eulerian_path[:-1]

    print(seq)
    n_kmers, k = len(kmers), len(kmers[0])
    if len(seq) == n_kmers+k:
        seq = seq[:-1]
    print("Final Seq:")
    print(seq)
    return path

# def EulerianPath(graph):
#     out_degree = {}
#     in_degree = {}

#     for node in graph:
#         out_degree[node] = len(graph[node])
#         for neighbor in graph[node]:
#             in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

#     donor = None
#     receiver = None

#     for node in set(list(out_degree.keys()) + list(in_degree.keys())):
#         out_deg = out_degree.get(node, 0)
#         in_deg = in_degree.get(node, 0)
#         if out_deg > in_deg:
#             donor = node
#         elif in_deg > out_deg:
#             receiver = node

#     print(f"Donor = {donor}, Receiver = {receiver}")

#     if donor and receiver:
#         if donor in graph:
#             graph[donor].append(receiver)
#         else:
#             graph[donor] = [receiver]

#     print("Updated Graph:", graph)
#     return graph

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
    # StringReconstruction\inputs\input_4
    with open("3.quiz.log") as file:
        k = file.readline().strip()
        data = file.readline().strip()
        # print(data)
        kmers = data.split()
        print(kmers)

    print("Data collected from the file.\n")
    dbruijnGraph = deBruijnGraph(kmers)
    print("Built De-bruijn Graph!\n")
    path = EulerianPath(dbruijnGraph, kmers)

if __name__ == "__main__":
    main()

