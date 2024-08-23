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

def kd_eulerian_cycle(graph):
    all_keys_nodes = list(graph.keys())
    all_vals_nodes = [x for _ in graph.values() for x in _]
    com_nodes = list(set(all_keys_nodes+all_vals_nodes))
    # print(com_nodes)
    
    donor = None
    receiver = None
    receiver_list = []
    for n in com_nodes:
        out_degree = len(graph.get(n, []))
        in_degree = all_vals_nodes.count(n)
        # print(f"{n} => Out: {out_degree}, In: {in_degree}")
        if in_degree == out_degree:
            pass
        if in_degree < out_degree:
            print(f"Out: {out_degree}, In: {in_degree} <= {n}. Reciever.")
            receiver = n
            receiver_list.append(n)
        if in_degree > out_degree:
            print(f"Out: {out_degree}, In: {in_degree} <= {n}. Donor.")
            donor = n
    # print(f"Donor = {donor}, Receiver = {receiver} (They are should be's!)")

    eulerian_circuit = [all_keys_nodes[0]]
    if receiver:
        eulerian_circuit = [receiver]
    current_node = eulerian_circuit[-1]
    # if donor in graph:
    #     graph[donor].append(receiver)
    # elif donor not in graph:
    #     graph[donor] = [receiver]

    db = {}
    while len(graph) != 0 or len(db) != 0: # Developing
        # print(f"Current Node: {current_node}")
        if current_node in graph:
            next_nodes = graph[current_node]
            if len(next_nodes) == 1:
                eulerian_circuit.append(next_nodes[0])
                del graph[current_node]
            elif len(next_nodes) > 1:
                eulerian_circuit.append(next_nodes[0])
                graph[current_node] = graph[current_node][1:]
            current_node = eulerian_circuit[-1]
            # print(eulerian_circuit)
        elif current_node not in graph:
            if current_node in db:
                eulerian_circuit = eulerian_circuit+db[current_node]
                del db[current_node]
            # elif len(eulerian_circuit) == 1:
            #     eulerian_circuit[all_keys_nodes[0]] # choose another start
            else:
                for i in range(len(eulerian_circuit) - 1): 
                    node_checkpoint = eulerian_circuit[i]
                    if node_checkpoint in graph:
                        # print(f"{node_checkpoint} can divert path")
                        db[node_checkpoint] = eulerian_circuit[i+1:]
                        eulerian_circuit = eulerian_circuit[:i+1]
                        current_node = node_checkpoint
                        break

    return eulerian_circuit

def glue_nodes(kmers):
    last = kmers[-1]
    first = "".join([kmers[i][0] for i in range(len(kmers)-1)])
    genome = first+last
    # print("Gluing Checkpoint")
    # print(len(kmers), len(first),len(last))
    return genome

# GappedGenomePath\inputs\input_1.txt
# 6.test.log
def main():
    with open("StringReconstructionReadPairs\inputs\input_6.txt") as file:
    # with open("GappedGenomePath\inputs\input_5.txt") as file:
    # with open("6.test.log") as file:
        kdinfo = file.readline().split()
        k, d = int(kdinfo[0]), int(kdinfo[1])
        read_kdmers = file.readline().strip().split()

        forward = []
        reverse = []
        for read in read_kdmers:
            split_read = read.strip().split("|")
            forward.append(split_read[0])
            reverse.append(split_read[1])

        forward_dbjn_graph = debruijn_graph(forward)
        reverse_dbjn_graph = debruijn_graph(reverse)

        print("Forward")
        forward_eulerian_path = kd_eulerian_cycle(forward_dbjn_graph)
        print("Reverse")
        reverse_eulerian_path = kd_eulerian_cycle(reverse_dbjn_graph)

        forward_string = glue_nodes(forward_eulerian_path)
        reverse_string = glue_nodes(reverse_eulerian_path)

        # print(forward_string)
        # print(reverse_string)

        # print(forward_string[k+d:])
        # print(reverse_string[:-k-d])
        # print(reverse_string[-k-d:])
        # print(reverse_string[:-k-d],reverse_string[-k-d:])
        # print(reverse_string)
        # for i = k + d + 1 to |PrefixString|
        #     if the i-th symbol in PrefixString does not equal the (i - k - d)-th symbol in SuffixString
        #         return "there is no string spelled by the gapped patterns"
        # return PrefixString concatenated with the last k + d symbols of SuffixString

        if forward_string[k+d:] == reverse_string[:-k-d]:
            spelled_string = forward_string+reverse_string[-k-d:]
            print("Spelled String")
            print(spelled_string)
            print(len(spelled_string))
            print(k + d + k + len(forward) - 1)
            # print(len(read_kdmers))
            # print(k+d)
            return spelled_string
        else: return "No String Spelled by these gapped reads"
    
        # for index in range((k + d), len(forward_string)):
        #     if forward_string[index] != reverse_string[index - k - d]:
        #         return "There is no string spelled by the gapped patterns!"
        # print(forward_string + reverse_string[-(k+d):])
        # print(reverse_string[-(k+d):])
        # print(len(forward_string + reverse_string[-(k+d):]))
        # return forward_string + reverse_string[-(k+d):]

        # print("\nK,d-mers: ")
        # print(read_kdmers)
        # db_graph = kd_dbruijn_graph(read_kdmers)
        # print("\nDe-Bruijn Graph: ")
        # for k in db_graph.keys():
        #     print(k, " => ", db_graph[k])
        # cycle = kd_eulerian_cycle(db_graph)
        # print("\nEulerian Path from Eulerian Circuit: ")
        # print(cycle)



main()