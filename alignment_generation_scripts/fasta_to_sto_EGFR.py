from pathlib import Path

"""
Convert a FASTA file to multiple Stockholm (.sto) files for different databases. Creates dummy MSA files.
"""

alignments_dir = Path("./a3m_files/EGFRAF2/msas/A/")


fasta_path = Path("./a3m_files/EGFRAF2/EGFR.fasta")

    # Read fasta
with fasta_path.open() as f:
    lines = [line.strip() for line in f if line.strip()]

sto_paths = ["uniref90_hits.sto", "uniprot_hits.sto", "pdb_hits.sto", "mgnify_hits.sto"]
for sto_filename in sto_paths:
    sto_path = alignments_dir / sto_filename
    # Extract sequence (remove lowercase insertions if present)
    sequence = "".join(lines[1:])
    sequence = "".join(c for c in sequence if c.isupper() or c == "-")

    num_res = len(sequence)

    with sto_path.open("w") as out:
        out.write("# STOCKHOLM 1.0\n")
        out.write(f"EGFR {sequence}\n")
        out.write(f'#=GC RF '+''.join(['x' for _ in range(num_res)])+'\n')
        out.write("//\n")

    print(f"Created {sto_path}")