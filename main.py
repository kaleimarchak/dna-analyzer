"""
main.py
CLI for the DNA/RNA Sequence Analyzer project.
"""

from sequence_utils import clean_sequence, identify_sequence_type
from analysis import calculate_stats, transcribe_dna
from translation import translate_rna
from file_io import read_text_file


def print_menu() -> None:
    print("\n==============================")
    print(" DNA / RNA Sequence Analyzer")
    print("==============================")
    print("1) Paste sequence")
    print("2) Load sequence from file (.txt/.fasta)")
    print("3) Identify sequence type")
    print("4) Show sequence stats")
    print("5) Transcribe DNA -> RNA")
    print("6) Translate RNA -> Amino Acid Chain")
    print("7) Show current cleaned sequence")
    print("0) Exit")


def main() -> None:
    current_seq = ""  # always store the CLEANED sequence here

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            raw = input("\nPaste sequence (FASTA allowed) then press Enter:\n> ")
            try:
                current_seq = clean_sequence(raw)
                print("Sequence loaded and cleaned.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            path = input("Enter file path: ").strip()
            try:
                raw = read_text_file(path)
                current_seq = clean_sequence(raw)
                print("Sequence loaded from file and cleaned.")
            except FileNotFoundError:
                print("Error: File not found.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            if not current_seq:
                print("No sequence loaded yet.")
            else:
                seq_type = identify_sequence_type(current_seq)
                print(f"Sequence type: {seq_type}")

        elif choice == "4":
            if not current_seq:
                print("No sequence loaded yet.")
            else:
                try:
                    stats = calculate_stats(current_seq)
                    print(f"Length: {stats['length']}")
                    print(f"Counts: {stats['counts']}")
                    print(f"GC%: {stats['gc_content']:.2f}")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == "5":
            if not current_seq:
                print("No sequence loaded yet.")
            else:
                try:
                    rna = transcribe_dna(current_seq)
                    current_seq = rna
                    print("Transcription successful. Current sequence is now RNA.")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == "6":
            if not current_seq:
                print("No sequence loaded yet.")
            else:
                try:
                    protein = translate_rna(current_seq)
                    print(f"Protein: {protein}")
                    print(f"Protein length: {len(protein)}")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == "7":
            if not current_seq:
                print("No sequence loaded yet.")
            else:
                print(f"Current cleaned sequence:\n{current_seq}")

        else:
            print("Invalid choice. Please enter 0–7.")

if __name__ == "__main__":
    main()

