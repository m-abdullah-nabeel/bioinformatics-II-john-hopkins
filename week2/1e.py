def eulerian_cycle(edge_dict):
    '''Generates an Eulerian cycle from the given edges.'''
    current_node = edge_dict.keys()[0]
    path = [current_node]

    # Get the initial cycle.
    while True:
        path.append(edge_dict[current_node][0])

        if len(edge_dict[current_node]) == 1:
            del edge_dict[current_node]
        else:
            edge_dict[current_node] = edge_dict[current_node][1:]

        if path[-1] in edge_dict:
            current_node = path[-1]
        else:
            break

    # Continually expand the initial cycle until we're out of edge_dict.
    while len(edge_dict) > 0:
        for i in xrange(len(path)):
            if path[i] in edge_dict:
                current_node = path[i]
                cycle = [current_node]
                while True:
                    cycle.append(edge_dict[current_node][0])

                    if len(edge_dict[current_node]) == 1:
                        del edge_dict[current_node]
                    else:
                        edge_dict[current_node] = edge_dict[current_node][1:]

                    if cycle[-1] in edge_dict:
                        current_node = cycle[-1]
                    else:
                        break

                path = path[:i] + cycle + path[i+1:]
                break
    return path

if __name__ == '__main__':

    # Read the input data.
    with open('1.sam.log') as input_data:
        edges = {}
        for edge in [line.strip().split(' -> ') for line in input_data.readlines()]:
            print(edge)
            if ',' in edge:
                edges[int(edge[0])] = map(int,edge[1].split(','))
            else:
                edges[int(edge[0])] = [int(edge)]

    # Get the Eulerian cycle.
    path = eulerian_cycle(edges)

    # Print and save the answer.
    print('->'.join(map(str,path)))
    with open('output/Assignment_04E.txt', 'w') as output_data:
        output_data.write('->'.join(map(str,path)))