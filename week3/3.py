## Question Ungraded
# def predict_possible_combs(n):
#     print(f"{(n-1)*n} possible subpeptides for a peptide of length {n}")

# predict_possible_combs(15448)

Alphabet = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W'] 

aminoAcidMass = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113, 
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129, 
    'M': 131, 
    'H': 137, 
    'F': 147, 
    'R': 156, 
    'Y': 163,
    'W': 186
}

# Peptide = "LEQN"
# Peptide = "QVMYECIMFCHIADHDRPASPFMEESAVGHVDNLRILEFHVVMVLI"
# Peptide = "AHRQGMYYQQLMLT"
Peptide = "AQV" # Quiz
# CYCLIC
# 2*2*2*4*3*2

# 1.7 CS: Generating the Theoretical Spectrum of a Peptide
def LinearSpectrum(Peptide, Alphabet, AminoAcidMass):
    PrefixMass = [0] * (len(Peptide)+1)
    # print(PrefixMass)

    for i in range(1, len(Peptide)+1):
        # print(i, i-1, Peptide[i-1], aminoAcidMass[Peptide[i-1]])
        for s in Alphabet:
            if s == Peptide[i-1]:
                PrefixMass[i] = PrefixMass[i - 1] + AminoAcidMass[s]
    # print(PrefixMass)
    
    LinearSpectrum = [0]
    for i in range(len(Peptide)): #i ← 0 to |Peptide| − 1
        # print(f"Processing with {Peptide[i]}, whose mass is {PrefixMass[i]}")
        for j in range(i+1, len(Peptide)+1): #for j ← i + 1 to |Peptide|
            # print(f"\tCalculating for {[j]} whose mass is {PrefixMass[j]} ==> Making {PrefixMass[j] - PrefixMass[i]}")
            LinearSpectrum.append(PrefixMass[j] - PrefixMass[i]) #add PrefixMass(j) − PrefixMass(i) to LinearSpectrum
    TheoreticalSpectrum = list(sorted(list(LinearSpectrum)))
    # print(TheoreticalSpectrum)
    print(" ".join(map(str, TheoreticalSpectrum)))
    return TheoreticalSpectrum

def CyclicSpectrum(Peptide, Alphabet, AminoAcidMass):
    PrefixMass = [0] * (len(Peptide)+1)
    # print(PrefixMass)

    for i in range(1, len(Peptide)+1):
        # print(i, i-1, Peptide[i-1], aminoAcidMass[Peptide[i-1]])
        for s in Alphabet:
            if s == Peptide[i-1]:
                PrefixMass[i] = PrefixMass[i - 1] + AminoAcidMass[s]
    # print(PrefixMass)
    peptideMass = PrefixMass[len(Peptide)]    
    CyclicSpectrum = [0]
    for i in range(len(Peptide)): #i ← 0 to |Peptide| − 1
        # print(f"Processing with {Peptide[i]}, whose mass is {PrefixMass[i]}")
        for j in range(i+1, len(Peptide)+1): #for j ← i + 1 to |Peptide|
            # print(f"\tCalculating for {[j]} whose mass is {PrefixMass[j]} ==> Making {PrefixMass[j] - PrefixMass[i]}")
            CyclicSpectrum.append(PrefixMass[j] - PrefixMass[i]) #add PrefixMass(j) − PrefixMass(i) to CyclicSpectrum
            if i > 0 and j < len(Peptide):
                CyclicSpectrum.append(peptideMass - (PrefixMass[j] - PrefixMass[i]))
    TheoreticalSpectrum = list(sorted(list(CyclicSpectrum)))
    # print(TheoreticalSpectrum)
    print(" ".join(map(str, TheoreticalSpectrum)))
    return TheoreticalSpectrum

# TheoreticalSpectrum = LinearSpectrum(Peptide=Peptide, Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)
# TheoreticalSpectrum = CyclicSpectrum(Peptide=Peptide, Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)
# print(" ".join(TheoreticalSpectrum))

# Quiz question cyclic peptides
# cyclic_pattern = "0 71 101 113 131 184 202 214 232 285 303 315 345 416"

# print(cyclic_pattern == CyclicSpectrum(Peptide="ALTM", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass))
# print(cyclic_pattern == CyclicSpectrum(Peptide="TAIM", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass))
# print(cyclic_pattern == CyclicSpectrum(Peptide="MIAT", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass))
# print(cyclic_pattern == CyclicSpectrum(Peptide="IAMT", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass))
# print(cyclic_pattern == CyclicSpectrum(Peptide="TMLA", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass))
# print(cyclic_pattern == CyclicSpectrum(Peptide="MTAI", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass))

# Quiz question linear peptides
# cyclic_pattern = "0 71 99 101 103 128 129 199 200 204 227 230 231 298 303 328 330 332 333"

# LinearSpectrum(Peptide="ETC", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)
# LinearSpectrum(Peptide="AVQ", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)
# LinearSpectrum(Peptide="QCV", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)
# LinearSpectrum(Peptide="TVQ", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)
# LinearSpectrum(Peptide="TCQ", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)
# LinearSpectrum(Peptide="TCE", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)

# Cogniterra STOP AND THINK
# LinearSpectrum(Peptide="VKF", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)
# LinearSpectrum(Peptide="VKY", Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)

def count_subpeptides(n):
    return (n * (n + 1)) // 2 + 1

# print(count_subpeptides(4))
print(count_subpeptides(15613))