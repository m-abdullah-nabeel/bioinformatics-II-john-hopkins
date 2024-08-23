x = "TAATGCCATGGGATGTT"

def kd_composition_illustration(x, k, d):
    print(x)
    for i in range(len(x)-k-k-d+1):
        print(f"{"-"*(i)}{x[i:i+k]}{"-"*d}{x[i+k+d:i+k+k+d]}")

def kd_composition(x, k, d):
    kd_composition_illustration(x, k, d)
    kdmers = []
    print(x)
    for i in range(len(x)-k-k-d+1):
        kd_mer = (x[i:i+k]+'|'+x[i+k+d:i+k+k+d])
        kdmers.append(kd_mer)
        # print(f"{kd_mer}")
    # print(kdmers)
    print(" ".join(["("+kd+")" for kd in sorted(kdmers)]))
    


kd_composition(x, 3, 2)