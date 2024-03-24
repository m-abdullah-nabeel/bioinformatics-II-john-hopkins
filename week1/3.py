def overlap(kmers):
    # print("all kmers")
    # for i in kmers:
    #     print(i)
    graph = {}
    for kmer1 in kmers:
        prefix = kmer1[1:]
        # print(f"kmer = {kmer1}, prefix = {prefix}")
        for kmer2 in kmers:
            suffix = kmer2[:-1]
            if prefix == suffix and kmer1 != kmer2:
                if kmer1 in graph:
                    # print("Kmer exist already")
                    graph[kmer1].append(kmer2)
                    # graph[kmer1].append(kmer2)
                else:
                    graph[kmer1] = [kmer2]
    return graph

# def overlap(patterns):
#     dprefix = {}
#     ladj = []
#     for e in patterns:
#         prefix = e[:-1]
#         dprefix.setdefault(prefix, []).append(e)
#     for e in sorted(patterns):
#         suffix = e[1:]
#         for ee in dprefix.get(suffix, []):
#             ladj.append((e,ee))
#     return ladj


with open("3.txt") as file:
    data = file.readline()
    patterns = data.split(" ")
    res = overlap(patterns)
    # print(res)
    # for k, v in res.items():
    #     print(k,": ",v)

    for k in (res.keys()):
        print(k + ": " + " ".join(sorted(res[k])))
        # # print(k)
        # print((sorted(res[k])))
        # print(", ".join(sorted(res[k])))
        