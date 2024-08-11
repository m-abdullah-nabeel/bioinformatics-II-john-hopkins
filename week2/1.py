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
    # current_cycle = edges[7] # this will give accurate result in our case
    current_node = current_cycle[-1]
    current_cycle_len = len(current_cycle)
    # # print(f"Initial cycle = {current_cycle}")
    for start in range(len(edges)):
        current_cycle = edges[start]
        # current_cycle = edges[7] # this will give accurate result in our case
        current_node = current_cycle[-1]
        current_cycle_len = len(current_cycle)
        # print(f"Initial cycle = {current_cycle}")

        while True:
            print(f"Iter.")
            print(f"Last node = {current_node} Current Cycle = {current_cycle}")
            next_nodes = graph[int(current_node)]
            print(f"{len(next_nodes)} next candidates {next_nodes}")
            
            prev_len = current_cycle_len
            for n in next_nodes:
                edge = str(current_node) + str(n)
                if edge not in current_cycle:
                    current_cycle = current_cycle + str(n)
                    current_node = n
                    current_cycle_len = len(current_cycle)
                    break
                else: 
                    print(f"{edge} already in {current_cycle}")
            
            print(f"Current Lens. {len(current_cycle)} == {current_cycle_len}")
            if prev_len == current_cycle_len:
                print("FATAL FATAL FATAL FATAL FATAL FATAL!!!!!!!!!!!!")
                # current_cycle = edges[7]
                break

            if len(current_cycle) > len(edges):
                # break
                print(current_cycle)
                print(" ".join(current_cycle))
                return False
    
                
            
    print(current_cycle)



with open("EulerianCycle\inputs\input_6.txt") as file:
    graph = {}
    for line in file:
        data = line.split(": ")
        graph[int(data[0])] = [int(i.strip()) for i in data[1].split(" ")]

    # print(graph)

    EulerianCycle(graph)