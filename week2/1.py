# this script works well if all nodes are comprising only one character like 1, 10
# this doesnt work correctly if the nodes are more than one number
# like 10, 20, this is not being interpreted by this function yet

# SOLUTION
# instead of using a string path, use a list
# instead of starting from an edge, start from a node
# lets see if there is anything more to change

def EulerianCycle(graph):
    # calculate edges number in graph
    print(f"Graph: {graph}")
    # print(list(graph.keys())[0])
    # print(list(graph.values()))
    nodes = []
    for v in graph.values():
        for n in v:
            nodes.append(n)
    
    print(f"Nodes: {nodes}")
    print(f"Total Nodes = {len(nodes)}")

    # difficult thing starts
    # current_cycle = edges[0]
    # current_cycle = [list(graph.keys())[0]]
    current_cycle = [nodes[0]]
    current_cycle_string = " ".join(map(str, current_cycle))
    # current_cycle = edges[7] # this will give accurate result in our case
    current_node = current_cycle[-1]
    current_cycle_len = len(current_cycle)
    print(f"Initial cycle = {current_cycle} and last node yet is: {current_node}")
    print(f"The current cycle string becomes {current_cycle_string} with length = {current_cycle_len}")
    for start in range(len(nodes)):
        current_cycle = [nodes[start]]
        current_node = current_cycle[-1]
        current_cycle_len = len(current_cycle)
        print(f"Iteration {start}: Cycle` = {current_cycle}")

        while True:
            print(f"Iter.")
            print(f"Last node = {current_node} Current Cycle = {current_cycle}")
            next_nodes = graph[int(current_node)]
            print(f"{len(next_nodes)} next candidates {next_nodes}")
            
            prev_len = current_cycle_len
            for n in next_nodes:
                edge = str(current_node) + str(n)
                if edge not in current_cycle_string:
                    current_cycle.append(n)
                    current_cycle_string = current_cycle_string + str(n)
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

            if len(current_cycle) > len(nodes):
                # break
                print(current_cycle)
                print(" ".join(map(str, current_cycle)))
                return False
    
                
            
    print(current_cycle)



with open("EulerianCycle\inputs\input_3.txt") as file:
    graph = {}
    for line in file:
        data = line.split(": ")
        graph[int(data[0])] = [int(i.strip()) for i in data[1].split(" ")]

    # print(graph)

    EulerianCycle(graph)