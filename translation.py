"""
translation.py
Functions and data for translating RNA sequences into protein sequences.
"""
#dictionary of which codons translate into what amino acids 
CODON_TABLE = {
    # Phenylalanine = F
    "UUU": "F", "UUC": "F",

    # Leucine = L
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",

    # Isoleucine = I
    "AUU": "I", "AUC": "I", "AUA": "I",

    # Methionine (Start) = M
    "AUG": "M",

    # Valine = V
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",

    # Serine = S
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
   
    # Proline = P
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    
    # Threonine = T
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    
    # Alanine = A
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
   
    # Tyrosine = Y
    "UAU": "Y", "UAC": "Y",
   
    # Histidine = H
    "CAU": "H", "CAC": "H",
   
    # Glutamine = Q
    "CAA": "Q", "CAG": "Q",
    
    # Asparagine = N
    "AAU": "N", "AAC": "N",
    
    # Lysine = K
    "AAA": "K", "AAG": "K",
    
    # Aspartic Acid = D
    "GAU": "D", "GAC": "D",
   
    # Glutamic Acid = E
    "GAA": "E", "GAG": "E",
    
    # Cysteine = C
    "UGU": "C", "UGC": "C",
   
    # Tryptophan = W
    "UGG": "W",
   
    # Arginine = R
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
   
    # Glycine = G
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",

    # STOP codons
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}

def translate_rna(rna: str) -> str:
    if rna is None or rna == "":
        raise ValueError("RNA sequence is empty; cannot translate")
    
    if "T" in rna:
        raise ValueError("Invalid RNA. Contains T nucleotide")
    
    allowed_chars = {"A", "C", "G", "U"}
    for char in rna:
        if char not in allowed_chars:
            raise ValueError(f"Invalid RNA base found: {char}")
    
    protein = []
    i = 0
    while i + 3 <= len(rna):
        codon = rna[i: i+3]
        amino = CODON_TABLE.get(codon)

        if amino is None:
            raise ValueError(f"Unknown codon encountered: {codon}")
        
        if amino == "STOP":
            break

        protein.append(amino)
        i += 3

    return "".join(protein)