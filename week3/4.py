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

Peptide = "LEQN"

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

# x = ["G", "A", "S"]
def Expand(PeptideKmers, Alphabet=Alphabet):
    branches = set()
    for sp in PeptideKmers:
        for a in Alphabet:
            branches.add(sp+a)
    # print(branches)
    # print(len(branches))
    return branches

# # Expand(x)

def Mass(peptide, AminoAcidMass):
    return sum(AminoAcidMass[aa] for aa in peptide)

def ParentMass(Spectrum):
    return max(Spectrum)

def Consistent(peptide, Spectrum, AminoAcidMass):
    peptide_spectrum = LinearSpectrum(peptide, Alphabet, AminoAcidMass)
    for mass in peptide_spectrum:
        if peptide_spectrum.count(mass) > Spectrum.count(mass):
            return False
    return True

def ConvertToMass(peptide, AminoAcidMass):
    return "-".join(str(AminoAcidMass[aa]) for aa in peptide)

def CyclopeptideSequencing(Spectrum):
    CandidatePeptides = {''}
    FinalPeptides = []

    while CandidatePeptides:
        CandidatePeptides = Expand(CandidatePeptides, Alphabet)
        for peptide in list(CandidatePeptides):
            if Mass(peptide, aminoAcidMass) == ParentMass(Spectrum):
                if CyclicSpectrum(peptide, Alphabet, aminoAcidMass) == Spectrum:
                    mass_peptide = ConvertToMass(peptide, aminoAcidMass)
                    if mass_peptide not in FinalPeptides:
                        FinalPeptides.append(mass_peptide)
                CandidatePeptides.remove(peptide)
            elif not Consistent(peptide, Spectrum, aminoAcidMass):
                CandidatePeptides.remove(peptide)
    
    return FinalPeptides

# Example usage:
# Sample Input:
# Spectrum = [0, 113, 128, 186, 241, 299, 314, 427]
# Spectrum = [0, 87, 101, 103, 103, 114, 128, 129, 163, 186, 186, 188, 190, 204, 231, 277, 289, 291, 291, 291, 300, 315, 315, 332, 376, 394, 394, 405, 418, 419, 429, 463, 477, 495, 501, 505, 508, 522, 580, 582, 591, 592, 604, 606, 609, 615, 685, 691, 694, 696, 708, 709, 718, 720, 778, 792, 795, 799, 805, 823, 837, 871, 881, 882, 895, 906, 906, 924, 968, 985, 985, 1000, 1009, 1009, 1009, 1011, 1023, 1069, 1096, 1110, 1112, 1114, 1114, 1137, 1171, 1172, 1186, 1197, 1197, 1199, 1213, 1300]
Spectrum = [0, 71, 113, 115, 128, 128, 131, 131, 147, 156, 186, 199, 218, 228, 243, 259, 262, 284, 299, 303, 314, 317, 346, 356, 374, 390, 414, 415, 427, 430, 431, 448, 461, 502, 502, 542, 545, 546, 561, 562, 574, 576, 613, 617, 630, 633, 673, 676, 689, 693, 730, 732, 744, 745, 760, 761, 764, 804, 804, 845, 858, 875, 876, 879, 891, 892, 916, 932, 950, 960, 989, 992, 1003, 1007, 1022, 1044, 1047, 1063, 1078, 1088, 1107, 1120, 1150, 1159, 1175, 1175, 1178, 1178, 1191, 1193, 1235, 1306]

# Running the function
result = CyclopeptideSequencing(Spectrum)

# Formatting the output
print(" ".join(result))

print(len(result))
