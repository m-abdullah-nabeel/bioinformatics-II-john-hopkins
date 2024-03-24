def combine_by_last(kmers):
    genome = kmers[0]
    for i in range(1, len(kmers)):
        # kmer = kmers[i]
        genome += kmers[i][-1]
    return genome

def combine_by_last2(kmers):
    """Working"""
    last = kmers[-1]
    first = "".join([kmers[i][0] for i in range(len(kmers)-1)])
    genome = first+last
    return genome

def combine_by_start(kmers):
    """Working"""
    first_bases = [kmer[0] for kmer in kmers]
    first = "".join(first_bases)
    # print(first)
    end = kmers[-1][1:]
    # print(end)
    genome = first+end
    return genome

# sample = ["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"]
# res = combine(sample)

# print(res)
with open("dataset_30182_3.txt") as f:
    all_kmers = []
    for line in f:
        all_kmers.append(line.split(" "))
    
    sample = all_kmers[0]
    # print(sample)
    res = combine_by_last2(sample)

    print(res)
