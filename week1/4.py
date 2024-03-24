def composition(text, k):
    all_kmers = []
    for i in range(len(text)+1-k):
        kmer = text[i:i+k]
        all_kmers.append(kmer)
    return all_kmers


def pathgraph(kmers):
    graph = {}
    for kmer in kmers:
        suffix = kmer[1:]
        prefix = kmer[:-1]
        if prefix in graph:
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]
    return graph

def deBruijnGraph(text = "AAGATTCTCTAAGA", k = 4):
    edges = composition(text, k)
    # print(edges)

    # nodes = composition(text, k-1)
    # print(nodes)

    res = pathgraph(edges)

    for k in (sorted(res.keys())):
        print(k + ": " + " ".join(sorted(res[k])))

    
with open("4.test.log") as file:
    text = file.readline()
    # deBruijnGraph()
    # deBruijnGraph(text=text, k=12)
    # deBruijnGraph(text="TAATGCCATGGGATGTT", k=2)
    deBruijnGraph(text="TAATGCCATGGGATGTT", k=3)
    # deBruijnGraph(text="TAATGCCATGGGATGTT", k=4)
    deBruijnGraph(text="TAATGGGATGCCATGTT", k=3)
