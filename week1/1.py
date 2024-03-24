def composition(text, k):
    all_kmers = []
    for i in range(len(text)+1-k):
        kmer = text[i:i+k]
        # print(kmer)
        all_kmers.append(kmer)
    # all_kmers.sort()
    # print(all_kmers)

    return all_kmers

# sample = "TATGGGGTGC"
sample = "CAATCCAAC"
x = composition(sample, 5)

# test = "CACTGATTGCTTTGCGTATGCTAACAGACTACCTAATTATACTTGCGCTCAAAGTTGCGTTGGCGACTTTCGGTTGTGCTGCGGTTAAAATATGGAGTTGTCGCGCCCGTAAACTTGTATCAGGCTTCCAGTCTGCTAAAGGACCGCGCTCAGTGAAGGCGACCGGCCCCATAAGTCCCCACCTGACATAGCATTCGCATTAGCGTCGCGTCCCGAGCGTCAGAGGCCCAGTGTCACGTGCAGACCGCGTTCCCGCAACTGGATTACCATTGTTGGGGATATTCGGAAATCGGATCAATTTAGATGCTTTCGAGTTCGGTATGGTCTTGAACAAACGGGTCGAGTATATCGCTAAGCTGGGACGGCAGCATGGAGAGCACATTAGGGCAATGCGTGACAAGTGCGCAAGACAACGGATCCCCCCTGGTGTGGTCCTTTGTTGAGAAAACCCACGTCGGGAGGTGGTATTATAGGTGTGGGGCTCTCCGTGACAAATGCGCACAAAGGTCACTCTTACTCTCCGGAACATCGGCAACTCCAGACAAGGTCCGCTACATTGGTTTTAGAAATCTATTTATACTTACATTCACTCACCCTTGTCGTCTCTTGGGTCCTAGGTACTAAGAAGACGCCCCCCAGAGTTGAGGGAGCCACAATCCCATTTAGGGAGCTTAGTATTAGCGGGTTGCCGGCCTCGCGCAGGAGTCGCTAGCCCCACTCGACGGAACAATCCCTAACCGTATACTACACAATATTAGGCAAGATGTTTTAATTATCAGCATCGGCCTATGCCCGGCACTCCTTAGTCCGGAATATTATACAAGGTGGATCGCAGCCCAAATAGGGTGTGGACGAATATAACGGGCTCCTGGTGATATTTATAAGTCCGAAGGTATCTGACAGTGACGTCCCGCCGTTACGGTGTTCAGGACTCACCTATACAACGAAGTGTATGAGTCATCCTAAAAATGAGTATTGACTACATCAGTCCGGGGTGATTATAACCAGACGTCCTAAGGTGATGCACCCCTAAATCACGACGGACCTTTAATCTTCCATGATTGGCATACATCTGTACACACAGAGAAGATGGACGCGTAAACAGAAATACGAGTATTTTCCGTCACTTGCAGAGATCGTGAGAAAAGAACATGCGCCGAGGGCTCGCGTATGCTGCAGCCGAAAGCTCTGAGGGCCCTATCTAGGTATTCCCGAAAGTGATATATGTCGGCGTGTCAGACGCCTTGCACAAGTGAGCAATCGTGCATAAATATCATGCTAACGTTGCCGAGAGACTAGTGAACGTACCGGAGCTAGGGGGCCTTCATCTCAGCCTTTACTCTCGGGAGGGTATCTCTGTGTTTGAATGCGTACTGGGCCAAGTACGCTAGCGCATGATCTCGAGAATTGCACTCCGTACGGCCAGGCATGACCCACAATCTTCAGTCAACAGAGGCGACGGTCTAATCACACTAGCGTACTAAAGTAGTAGAGGCTAATCAAGCATCGATAAGTGGACGGCCAAGCTTTGCAGTGTGTGCGCCTGGACCACTAGCATACTTTGCAGGGAGTGTAGGAGACGGGTGACAATTAAATATGTATCGGACTGCCACATGCTCACGATGGGCTACTCGCGCGTAAAACCCATTTTTTGTACGTGATTGGTGAGTACGAGACCGTCCAATAGGATAATCTATAACTTCTAGCTCTCTATCAGATAGACAACAATATAGGTTTACTCCAGTAGCCTGGGGTTTCGAACTGGCGTACTTTTATGTCAACCTGATGAGTCCGGCTGCCATGAAGCCCGTACTATACTATCAAAAGCCGGCCAAACATGATTGATTCAGCCTTAGAGCGAGCACGATTGGAATTGGATACGATGCGACACAACACAAATTCAGGTATTTGCCAATACTAATCTAGTTGAAGTCATGTAAGGCAACGTGGTAGTCACGGATCTCAAACTTCAGCATCGAGTACCTGATTCTGCGAACCTTGCAATCGATAGGATATGCCTCACGTCGCACGTCTGCACCAGCGCTTATCGCAATTGTAGCAGCGATGTACGAAATTCACAGAGAGTACTGGCAATCTTTAGAGCTAGTCATTGTGCGATATTTCCAAAAATTCTTACTTTTCGTCGTGGGCTGAGACGAACCTGCAAGCTCAGAGGCTGTGGACAACTCACCTCTTTTTTTTGTACGTTCCCCATCGGTACCTTAATACCCTCTAGTTTCAGGGCCCAGACACCGTGAATGGGATGGCTCAAATACGGGATGTGTTCTTAGAATTACCTATCCATCTCGGGGACGCATGGAGGTCGGCCCTGTGATGACGCTCTGGATGTCACCAACCGACCGCCCTTGTTTCTTAACTGAATAGTGGCCACCTTGTTTAACATTCCCCGGTAGATAAGGGCTTCGATGCTGTGACATAATTCCCGCGCGCCGGTATACTATCCTGTTTCGCACGTGATCTTTAGTGGAAGCTACCGTTGGTGGGAGTCTGTTCTCCCGCTGGGTAGCGGTAGTAGGTTTCCCCCTGAGGGTCTGAGTTGGTTCAAGACGTTGTTAACTACTTCGTTGATCTGTAAGGCATGAGCCATCGCCATCATCAATGACTACCTTATTAAAAACAGTAACAGTCGCGATTAAACGAGACTGGATTAATTCTTTACGGTGAATAAAGCCAATCTTCGAGCACCGAGCGGATTATCCTTGAAACTCTATACTGACGTTACCCGTTGAGATACGTGTATTCCGGGGATTACTTGAATGGATCGAACTCATAGTCTAGTGCTACCACGTACGGGTCGTATTTGTGCATTTCTAATTCTCGCTTCGAATGTGGATACAGACGTGCAGAGGAGTGCCGAAAATGAAACGCCATAAACACGATCCTGACATTCTGTAGTACGCTGCGGGCAGACTACGGTGCATAGGCTAATACTGACTCCTGTTATCAACACCTATACCCAGGTGCCTGAGTAATTCCGCCCCGTGGCGCCGCACCGCAAGCATAACATGCTGCTCAGGTCTATACACGGTTATCGATATCTTCCCGATATGACGATACGCCCCATTGCGGGTACACAAGTGGGGTCGAAGGGCCGAGTACTTTTAGGGAATACCACCGATCACAGTCACTACATGTCCTTTCTCTGGCGTGTGGGCTACGAGTTGGTCTAAATTTCGGGAAAAATGGACCTTGTCTATGTGATCCAACAATCGCCGGCCTGATCCAGACAGTGTCAGCAACTCCGCCCGTTTCTTTCCAAGTGGTACCTCACCGGAGCCACATTCAATGTCAGGACTGGTCTCACCTCACTTTGGCCTGAGGTTCTCCTGGGCCACGGCAGGGTTCGTTCCGGCCGTTTCCCCATTAGAGCGAACTTGAGCTTAATGAGTTAAAGGCCCGACAAAGTGCCTATTAGCTATCCGCCCCAAGGATGCCTTATCCGGGCTTAAACCCATTTTTCCAAGCTATGTTCATGCGATCCATTTCTGTGAGTCCCTCTGTTGGGGCGCTGCACAATGATTGGGCTCCATGCGGGTCTAAGCAAGACCTGTCCCCGCAACCTGTATATTGTGGCTGTCTGCTAGTGTTCTATCAAAGTCTACCGCCTGTCAACCACTTTTCGGATCCTCATGGTCTATGACACGGGATGTCAACCTGATGTCTGGTTTCAACGGTTAAAAATGAACTCTGTATTTTCCCACTGATCTGCATGTTCTTTCAGTGCTACATATGAATGCACGACCTCAGCTTGCGGTGGACTCTCGGTTATTTGCCGCCTTTTGTTGGAGGTGATTACGACCTACGGCTTAAGCTCGGATTCCTGCTTTATGGACTATGCTTGGTAATAGGTATACCCCGCGGCCACCGTCGTATTTTTGCAGAGTACCGTAGAGAACTTCCCTGTAGGCAGGGAGACCTGTTCTAACACCAGTAGCGCGTGATCCGCGATGTGTCGCAGGCCTGATGTTAATGATTAAACAGTCCCGATACTGCGCCCCCGTCTCCTGTTCGACCCTGACTACTATGGCAATTACGTCCATCGGTTGTTGAACGGACTCTATCCTAGCGCAAGCATGAGGTAAAGGTGTGAAACCCAACCAGATTGGAAGTACAAACTCGCACACTAATATTAAAAGTAATTCTGTTAAAGCACTAAATATTCAAATTCTGGATCTATCAGTGCAGCCTACGAGGCGATCGGGTAGGCGTTTTGGGGATCTTGACATTTGGATGCGTTCCTTCCGTTTGGGGGGGTGAACTCGGACGTGCTATCGCGACAATCAGAATATCCGCCACGACTACTGAGATGTAGTATCCGGGATGCATTAACCCCCCAGTGCTACTAATCATGGGAACTGAGTTGTATGTCAACACGCTTACGACAAAGTAATATTGAGGCCCTCGTGGGAGTGATATAGTGTAAGTTCCGGGTTTAGCTGATGTCTAGAACACAGAACAGGGGAGCTATACCGGTTTTGTGTTTAGCTTCGCACCACAGGTTACCCGTTTGCAAAGGATTGACGGTACATCCATACATTGATCGTTGTGTCTCGATTACGAACTTGCTTGTACCCTCTATTGCCGGGTGGCAGTTTGTTTATTGGCCTGTCAAAATAGGCCTTAGGTTCTCGAAGCCCCCCCCAAGCATCATATAATCGAGTACTCGATGACTCCCGGAGTCGACGACCATAGACCTCGGGCTGGGGGGCAGACTCTGCGTCGAGCACCCAGAAGTGCCGGAATGTGTTTGATCACGAGGCCACGTTTTACTTGTACACTATCGACCCAGGAGGGCCGTAGGAAATGAGGGGTAACACAAGGCTCAGGCTATTTTAAGGTATAGACTCGCACGCATATGGGTGTATCGGCGCCAACATACTTTTGCCGCTTCTTCAGTCCAACTATTACCGCCAAGAGTGTTTAAAGGACCACAGACATTTTAATTTGTTTATCAGTCGTGCAGTGCGTTCGCGTGAAGG"
# x = composition(test, 100)

# print(x)

for i in x:
    print(i, end=" ")
