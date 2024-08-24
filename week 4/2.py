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

def LinearScore(peptide, experimental_spectrum):
    # print(peptide)
    theoretical_spectrum = LinearSpectrum(Peptide=peptide, Alphabet=Alphabet, AminoAcidMass=aminoAcidMass)
    # print(theoretical_spectrum)
    # print(experimental_spectrum)

    score = 0
    for sp in theoretical_spectrum:
        if sp in experimental_spectrum:
            experimental_spectrum.remove(sp)
            score += 1
    print(f"Score: {score}")
    return score

# LinearScore(peptide, experimental_spectrum)

def Trim(Leaderboard, Spectrum, N):
    scores = [(peptide, LinearScore(peptide, Spectrum.copy())) for peptide in Leaderboard]
    scores.sort(key=lambda x: x[1], reverse=True)

    if N < len(scores):
        cutoff_score = scores[N-1][1]
        trimmed_leaderboard = [peptide for peptide, score in scores if score >= cutoff_score]
    else:
        trimmed_leaderboard = [peptide for peptide, score in scores]

    return trimmed_leaderboard

# def Trim(Leaderboard, Spectrum, N, Alphabet, AminoAcidMass):
#     print(Leaderboard)
#     print(Spectrum)
#     for Peptide in Leaderboard:
#         # print(Peptide, Spectrum)
#         print(LinearScore(Peptide, Spectrum.copy()))


leaderboard = ""
experimental_spectrum = []
N = 0
with open("2.test.txt") as file:
    leaderboard = file.readline().strip().split()
    experimental_spectrum = [int(_) for _ in file.readline().split()]
    N = int(file.readline().strip())

# print(leaderboard)
# print(experimental_spectrum)
# print(N)

final = Trim(
    Leaderboard=leaderboard, 
    Spectrum=experimental_spectrum, 
    N=N, 
    # Alphabet=Alphabet, 
    # AminoAcidMass=aminoAcidMass
)

print("-----------------")

# print(final[:N])
print(" ".join(final))
