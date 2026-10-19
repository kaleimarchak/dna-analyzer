# DNA/RNA Sequence Analyzer (Python)

A command-line bioinformatics tool that cleans and validates nucleotide sequences (DNA/RNA), computes basic sequence statistics, performs DNA→RNA transcription, and translates RNA into a protein sequence using a codon table.

## Features
- Accepts pasted input or file input (.txt / .fasta)
- Cleans input:
  - ignores FASTA headers (`>` lines)
  - removes whitespace
  - converts to uppercase
  - rejects invalid characters
- Classifies sequences as: DNA, RNA, or INVALID (strict rule: sequences without T or U are considered INVALID)
- Computes:
  - length
  - nucleotide counts (A/C/G/T/U)
  - GC content (%)
- Transcribes DNA → RNA (T → U)
- Translates RNA → protein (1-letter amino acid codes), stops at STOP codons

## Project Structure
- `main.py` — CLI application
- `sequence_utils.py` — cleaning + type identification
- `analysis.py` — stats + transcription
- `translation.py` — codon table + RNA translation
- `file_io.py` — file reading helper

## How to Run
From the project folder:

```bash
python main.py
