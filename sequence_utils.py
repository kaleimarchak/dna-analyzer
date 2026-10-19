"""
sequence_utils.py
Utilities for cleaning and validating nucleotide sequences.
"""
#from __future__ import annotations

def clean_sequence(raw: str) -> str:
    """
    clean_sequence cleans a raw DNA/RNA sequence string
    
    :param raw: Description
    :type raw: str
    :return: Description
    :rtype: str

    Rules:
    - Remove whitespace (spaces, tabs, newlines)
    - Convert to uppercase
    - Ignore FASTA header lines that start with '>'
    - Reject non-letter characters (digits, punctuation, etc.)
    - Return the cleaned sequence (letters only)

    Raises:
        ValueError: if the input is empty after cleaning or contains invalid characters.
    """
    if raw is None:
        raise ValueError("No input provided.")
    
    lines = raw.splitlines() #splits raw data into a list of new lines

    seq_lines = [] 
    for line in lines:
        stripped = line.strip() #gets rid of new lines and whitespace outside of content
        if stripped.startswith(">"):
            continue
        seq_lines.append(stripped)

    joined = "".join(seq_lines)
    
    characters = []
    for char in joined:
        if not char.isspace():
            characters.append(char)

    clean_seq = "".join(characters).upper()
    if clean_seq == "":
        raise ValueError("Sequence is empty after cleaning.")
    
    bad_chars = [] #set is also sufficient here and would be faster for sorting
    for char in clean_seq:
        if not char.isalpha():
            if char not in bad_chars:
                bad_chars.append(char)

    bad_chars_sorted = sorted(bad_chars)
    if bad_chars_sorted:
        raise ValueError(f"Sequence contains invalid character(s): {bad_chars_sorted}")

    return clean_seq

def identify_sequence_type(seq: str) -> str:
    """
    Docstring for identify_sequence_type
    
    :param seq: takes a clean sequence string that is uppercase letters only
    :type seq: str
    :return: returns the type of sequence, "DNA", "RNA", "INVALID"
    :rtype: str 
    """

    if not seq:
        return "INVALID"
    
    if "T" in seq and "U" in seq:
        return "INVALID"
    
    if "T" in seq and "U" not in seq:
        return "DNA"
    
    if "U" in seq and "T" not in seq:
        return "RNA"
    
    return "INVALID"