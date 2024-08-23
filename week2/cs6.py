# def MaximalNonBranchingPaths(graph):
#     all_nodes = list(graph.keys())
#     circuit = [all_nodes[0]]
#     current_node = circuit[-1]
#     db_list = []
#     while len(graph) != 0:
#         # print(db_list)
#         if current_node in graph:
#             next_node = graph[current_node]
#             # print(f"Next Nodes of {current_node} are {next_node} code1")
            
#             if len(next_node) == 1:
#                 circuit.append(next_node[0])
#                 del graph[current_node]
#                 current_node = circuit[-1]
#                 print(circuit)
#                 print(f"Current Nodes {current_node} code2")
#             elif len(next_node) > 1:
#                 if len(circuit) != 1:
#                     db_list.append(circuit)
#                     circuit = [current_node]
#                     circuit.append(next_node[0])
#                     graph[current_node] = graph[current_node][1:]
#                     current_node = circuit[-1]
#                     print(circuit)
#                     print(f"current node is {current_node} code3")
#                 if len(circuit) == 1:
#                     # db_list.append(circuit)
#                     # circuit = [current_node]
#                     circuit.append(next_node[0])
#                     graph[current_node] = graph[current_node][1:]
#                     current_node = circuit[-1]
#                     print(circuit)
#                     print(f"current node is {current_node} code3")

#         if current_node not in graph:
#             print("code5")
#             db_list.append(circuit)
#             all_nodes = list(graph.keys())
#             if len(all_nodes) > 0:
#                 circuit = [all_nodes[0]]
#                 current_node = circuit[-1]
#                 print(f"current node is {current_node} code4")

#     print(db_list)
#     return db_list

def MaximalNonBranchingPaths(graph):
    print(graph)
    all_keys = list(graph.keys())
    all_vals = [x for v in graph.values() for x in v]
    all_nodes = list(set(all_keys+all_vals))
    # print(all_keys)
    # print(all_vals)
    
    print(all_nodes)
    all_edges = []
    for k in all_keys:
        for v in graph[k]:
            print(v)
            all_edges.append((k, v))

    db_list = []
    # for e in all_edges:
    #     unit_ = []
    #     unit_.append(e)
    #     suffix = e[1:]
    #     while True:
            

    print("\n\n\n\n\n\n")
    print(db_list)
    return db_list

kmers =[]

# cs6.test.log
# MaximalNonBranchingPaths\inputs
with open("MaximalNonBranchingPaths\\inputs\\input_5.txt") as file:
    graph = {}
    for l in file:
        line = l.strip().split(":")
        k = int(line[0])
        v = [int(v1) for v1 in line[1].strip().split()]
        graph[k] = v
    # print(graph)

mnbp = MaximalNonBranchingPaths(graph)
# print(mnbp)
for _ in mnbp:
    print(" ".join(map(str, _)))