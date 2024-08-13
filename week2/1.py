# !/c/Windows/py

def EulerianCycle(graph):
    # print(graph)

    # form a cycle Cycle by randomly walking in Graph
    # eulerian_path = [list(graph.keys())[0]]
    eulerian_path = [list(graph.values())[0][0]]
    current_node = eulerian_path[-1]
    # print(f"Initial Values: Path = {eulerian_path}, Node = {current_node}")

    
    db = {}
    db_list = []

    # for i in range(20):
    while len(graph) != 0 or len(db) != 0:
        # print(eulerian_path)
        # print(graph)
        # print(current_node)
        # print(db)
        if current_node in graph:
            next_nodes = graph[current_node]
            # print(f"Next nodes: {next_nodes}")
            # eulerian_path.append(next_nodes[0])
            
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
    return eulerian_path
    
# EulerianCycle\\inputs\\input_7.txt
with open("1.test.log") as file:
    graph = {}
    for line in file:
        data = line.split(": ")
        graph[int(data[0])] = [int(i.strip()) for i in data[1].split(" ")]

cycle = EulerianCycle(graph)
# print(cycle)
# print("ANSWER\n\n\n\n#################################################")
print(" ".join(map(str, cycle)))
# reminder! just copying the output can result in wrong answer because
# there may be unwanted linebreaks, so either remove the line breaks or
# push the answer to a file