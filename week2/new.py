# !/c/Windows/py

def EulerianCycle(graph):
    print(graph)
    stack = []
    current_cycle = []
    current_node = list(graph.keys())[0]
    stack.append(current_node)
    print(f"Path: {current_cycle}\nStack: {stack}")

    while stack:
        # If there are edges left from the current node, continue the walk
        if graph[current_node]:
            stack.append(current_node)
            # Remove the edge and move to the next node
            next_node = graph[current_node].pop(0)
            print(next_node)
            current_node = next_node
            print(f"Path: {current_cycle}\nStack: {stack}")
        else:
            # If no more edges left from the current node, backtrack
            current_cycle.append(current_node)
            current_node = stack.pop()
            print(f"Path: {current_cycle}\nStack: {stack}")

    # The current_cycle is currently in reverse order, so reverse it to get the correct order
    current_cycle.reverse()
    return current_cycle


with open("EulerianCycle\\inputs\\input_1.txt") as file:
    graph = {}
    for line in file:
        data = line.split(": ")
        graph[int(data[0])] = [int(i.strip()) for i in data[1].split(" ")]

cycle = EulerianCycle(graph)

print(" ".join(map(str, cycle)))