import shutil
from pathlib import Path

"""
Organize precomputed MSAs and fasta files into the required directory structure for HelixFold3.
See "alignment_generation_scripts" folder for how to prepare the correct alignment files.
"""

# Input directories
json_dir = Path("") # Specify the directory containing HelixFold3 JSON files
binder_alignments_dir = Path("") # Specify the directory containing binder alignment subdirectories
egfr_alignments_dir = Path("") # Specify the directory containing EGFR alignment files

# Output directories
output_base = Path("") # Specify the base output directory for HelixFold3 input
output_base.mkdir(exist_ok=True)

def process_entry(json_file: Path):
    name = json_file.stem

    binder_dir = binder_alignments_dir / name
    egfr_dir = egfr_alignments_dir

    if not binder_dir.exists():
        print(f"Warning: No binder alignment directory for {name}, skipping.")
        return

    # Create directory structure
    out_dir = output_base / name
    msas_A = out_dir / "msas" / "protein_A" / "A"
    msas_B = out_dir / "msas" / "protein_B" / "B"
    msas_A.mkdir(parents=True, exist_ok=True)
    msas_B.mkdir(parents=True, exist_ok=True)

    # Copy binder alignments to A
    binder_sto = list(binder_dir.glob("*.sto"))

    if len(binder_sto) == 0:
        print(f"Warning: {name} has no .sto files")
        return

    for sto in binder_sto:
        shutil.copy2(sto, msas_A / sto.name)
    
    # Copy EGFR alignments to B
    egfr_sto = list(egfr_dir.glob("*.sto"))

    if len(egfr_sto) == 0:
        print(f"Warning: {name} has no .sto files")
        return

    for sto in egfr_sto:
        shutil.copy2(sto, msas_B / sto.name)

    print(f"Processed {name}")

# process normal json files
for json_file in json_dir.glob("*.json"):
    process_entry(json_file)
