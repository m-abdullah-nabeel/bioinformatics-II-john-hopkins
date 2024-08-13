# !/c/Windows/py

def EulerianCycle(graph):
    print(graph)

    # form a cycle Cycle by randomly walking in Graph
    eulerian_path = [list(graph.keys())[0]]
    current_node = eulerian_path[-1]
    print(f"Initial Values: Path = {eulerian_path}, Node = {current_node}")

    for i in range(20):
        next_nodes = graph[current_node]
        eulerian_path.append(next_nodes[0])
        
        if len(next_nodes) == 1:
            del graph[current_node]
        elif len(next_nodes) > 1:
            graph[current_node] = graph[current_node][1:]
        
        current_node = eulerian_path[-1]
        
        print(graph)
        print(eulerian_path)
        print(current_node)

        print(f"Ending iteration {i}")

        
        
    print(eulerian_path)

    

with open("EulerianCycle\\inputs\\input_1.txt") as file:
    graph = {}
    for line in file:
        data = line.split(": ")
        graph[int(data[0])] = [int(i.strip()) for i in data[1].split(" ")]

cycle = EulerianCycle(graph)
print(cycle)
# print(" ".join(map(str, cycle)))