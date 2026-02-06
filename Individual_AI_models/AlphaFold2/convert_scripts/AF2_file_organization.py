import shutil
from pathlib import Path

"""
Organize precomputed MSAs and fasta files into the required directory structure for AF2.
"""

# Input directories
fasta_dir = Path("./FASTA_files/individual_fasta_v2/")
alignments_dir = Path("./a3m_files/alignments_openfold_new/")

# Output directories
output_base = Path("organized_fasta_AF2_v2")
output_base.mkdir(exist_ok=True)

def process_entry(fasta_file: Path):

    name = fasta_file.stem
    alignment_dir = alignments_dir / name
    if not alignment_dir.exists():
        print(f"Warning: No alignment directory for {name}, skipping.")
        return

    # Create directory structure
    out_dir = output_base / name
    msas_A = out_dir / "msas" / "A"
    msas_A.mkdir(parents=True, exist_ok=True)

    # Copy fasta
    shutil.copy2(fasta_file, out_dir / fasta_file.name)

    # Copy alignments
    a3m_file = list(alignment_dir.glob("*.a3m"))
    sto_file = list(alignment_dir.glob("*.sto"))

    if len(a3m_file) != 1 or len(sto_file) != 4:
        print(f"Warning: {name} does not have exactly one .a3m and .sto")
        return

    shutil.copy2(a3m_file[0], msas_A / a3m_file[0].name)
    for sto in sto_file:
        shutil.copy2(sto, msas_A / sto.name)

    print(f"Processed {name}")

# process normal Fasta files
for fasta_file in fasta_dir.glob("*.fasta"):
    process_entry(fasta_file)
