def EulerianCycle(graph):
    # calculate edges number in graph
    # One Way
    # graph_values = graph.values()
    # edges = []
    # for v in graph_values:
    #     for e in v:
    #         edges.append(e)
    # total_edges = len(edges)
    # print(f"Total Edges = {total_edges}")

    print(graph)
    edges = []
    for k in graph.keys():
        for v in graph[k]:
            e = str(k)+str(v)
            edges.append(e)
    
    print(edges)
    print(f"Total Edges = {len(edges)}")

    # verify operations
    # print(edges[0][1:])
    # print(edges[4][:-1])
    # print(edges[0][1:] == edges[4][:-1])

    # e_cycle = []
    # # make a functionality to glue edges by overlap
    # for e in edges:
    #     # print(e)
    #     suffix = e[1:]
    #     for ep in edges:
    #         prefix = ep[:-1]
    #         if suffix == prefix:
    #             s2 = ep[1:]
    #             # print(f"{e} ==> {ep}, {suffix} == {prefix}")
    #             print(f"{e+s2}")
    # the above functioanlty glues two adjacent nodes, lets try another way

    last_stable_string = ""
    e_cycle = edges[0]
    while len(e_cycle) <= 5:
        for e in edges:
            # print(e)
            if len(graph[int(e[1])]) > 1:
                # print(f"More than 1 paths for {e[1]}")
                last_stable_string = e_cycle
            prefix = e[:1]
            suffix = e[1:]
            # print(f"{e}, {prefix}, {suffix}")
            # print(e_cycle[-1])
            # print(f"{e_cycle[-1]} VS {prefix}")
            if e_cycle[-1] == prefix:
                # print(f"{e_cycle[-1]} == {prefix}")
                if e in e_cycle:
                    print(f"{e} already in {e_cycle}")
                    e_cycle = last_stable_string
                    next
                else:
                    e_cycle = e_cycle+suffix
                    print(e_cycle)
            

    # print(e_cycle)

    # start from any random node / edge
    # say always start from first node / edge
    eulerian_string = ""
    last_high_connection = ""


with open("1.sam.log") as file:
    graph = {}
    for line in file:
        data = line.split(": ")
        graph[int(data[0])] = [int(i.strip()) for i in data[1].split(" ")]

    print(graph)

    EulerianCycle(graph)