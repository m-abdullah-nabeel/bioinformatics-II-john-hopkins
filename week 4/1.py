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

# Peptide = "NQEL"

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
    # print(" ".join(map(str, TheoreticalSpectrum)))
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
    # print(" ".join(map(str, TheoreticalSpectrum)))
    return TheoreticalSpectrum



peptide = ""
experimental_spectrum = []
with open("1.quiz.txt") as file:
    peptide = file.readline().strip()
    experimental_spectrum = [int(_) for _ in file.readline().split()]


def Score(peptide, experimental_spectrum):
    print(peptide)
    theoretical_spectrum = CyclicSpectrum(Peptide=peptide, Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)
    print(theoretical_spectrum)
    print(experimental_spectrum)

    score = 0
    for sp in theoretical_spectrum:
        if sp in experimental_spectrum:
            experimental_spectrum.remove(sp)
            score += 1
    print(f"Score: {score}")

# Score(peptide, experimental_spectrum)

def LinearScore(peptide, experimental_spectrum):
    print(peptide)
    theoretical_spectrum = LinearSpectrum(Peptide=peptide, Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)
    print(theoretical_spectrum)
    print(experimental_spectrum)

    score = 0
    for sp in theoretical_spectrum:
        if sp in experimental_spectrum:
            experimental_spectrum.remove(sp)
            score += 1
    print(f"Score: {score}")

LinearScore(peptide, experimental_spectrum)