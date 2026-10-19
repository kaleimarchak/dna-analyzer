"""
analysis.py
Provides functions to analyze cleaned DNA/RNA sequences, including
nucleotide counts, sequence length, and GC content.
"""

def calculate_stats(seq: str) -> dict:
    if not seq:
        raise ValueError("Sequence is empty; cannot calculate stats.")
    
    length = len(seq)

    #nucleotide count
    counts = {"A": 0, "C": 0, "G": 0, "T": 0, "U": 0}

    for base in seq:
        if base in counts:
            counts[base] += 1
        else:
            raise ValueError(f"Invalid base found in sequence: {base}")
        
    gc_count = counts["G"] + counts["C"]
    gc_content = (gc_count / length) * 100

    return {"length": length, "counts": counts, "gc_content": gc_content}

def transcribe_dna(seq: str) -> str:
    if not seq:
        raise ValueError("Sequence is empty, DNA cannot be transcribed.")
    
    if "U" in seq:
        raise ValueError("This is appears to an RNA sequence; cannot transcribe")
    
    if "T" not in seq:
        raise ValueError("Sequence has no T nucleotide; cannot confidently treat as DNA for transcription" )
    
    return seq.replace("T", "U") #returns the sequence with all T's replaced with U's