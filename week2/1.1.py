import random

def eulerian_cycle(graph):
    path = []
    print(graph)

    all_edges = [item for val in graph.values() for item in val ]
    print(f"Length of Edges is {len(all_edges)}.")
    print(all_edges)

    # start = random.choice(all_edges)
    # print(f"random node key is {start}")
    # path.append(start)

    print("Finding...")
    while len(path) < len(all_edges):
        # print(len(path), len(all_edges))
        print(f"{path} <= Current Path")

        if len(path) == 0:
            start = random.choice(all_edges)
            # print(f"random node key to start is {start}")
            path.append(start)

        last = path[-1]
        next = graph[last]
        next_choice = random.choice(next)
        # print(next)
        occ_in_path = path.count(next_choice)
        occ_in_nodes = all_edges.count(next_choice)
        if occ_in_path < occ_in_nodes:
            path.append(next_choice)
        else:
            tried = []
            tried.append(next_choice)
            while len(tried) < len(next):
                print(f"tried next to {last} => {tried}")
                for i in next:
                    if i not in tried:
                        occ_in_path = path.count(i)
                        occ_in_nodes = all_edges.count(i)
                        if occ_in_path >= occ_in_nodes:
                            tried.append(i)
                        elif occ_in_path < occ_in_nodes:
                            path.append(next_choice)
            else: path.clear()

    return path

with open("1.sam.log") as file:
    graph = {}
    for line in file:
        data = line.split(": ")
        graph[int(data[0])] = [int(i.strip()) for i in data[1].split(" ")]

    print(graph)

    # print(graph)
    # predicted_path = eulerian_cycle(graph)
    # predicted_path = [str(i) for i in predicted_path]
    # formatted_predicted_path = " ".join(predicted_path)
    # with open("1.ans.sam.log", "w") as ans_file:
    #     ans_file.write(formatted_predicted_path)

    # print(formatted_predicted_path)
