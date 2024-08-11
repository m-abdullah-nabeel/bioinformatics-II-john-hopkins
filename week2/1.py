def EulerianCycle(graph):
    # calculate edges number in graph
    print(graph)
    edges = []
    for k in graph.keys():
        for v in graph[k]:
            e = str(k)+str(v)
            edges.append(e)
    
    print(edges)
    print(f"Total Edges = {len(edges)}")

    # difficult thing starts
    current_cycle = edges[0]
    current_node = current_cycle[-1]

    print(f"Initial cycle = {current_cycle}")
    
    for c in range(14):
        print(f"Iter. {c}")
        print(f"Last node = {current_node} Current Cycle = {current_cycle}")
        next_nodes = graph[int(current_node)]
        print(f"{len(next_nodes)} next candidates {next_nodes}")
        for n in next_nodes:
            edge = str(current_node) + str(n)
            if edge not in current_cycle:
                current_cycle = current_cycle + str(n)
                current_node = n
                break
            else: 
                print(f"{edge} already in {current_cycle}")
 
        

            
            
    print(current_cycle)



with open("1.sam.log") as file:
    graph = {}
    for line in file:
        data = line.split(": ")
        graph[int(data[0])] = [int(i.strip()) for i in data[1].split(" ")]

    # print(graph)

    EulerianCycle(graph)