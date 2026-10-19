"""
file_io.py
Functions for reading sequence data from files (e.g., .txt, .fasta).
"""
def read_text_file(path: str) -> str:
    f = open(path, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    return "".join(lines)