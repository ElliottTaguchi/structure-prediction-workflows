from pathlib import Path

"""
Convert an A3M MSA file to multiple Stockholm (.sto) files for different databases. Creates dummy MSA files.
"""


alignments_dir = Path("./a3m_files/alignments_openfold_new/")
"""input your path to the directory containing the alignment subdirectories here"""

for protein_dir in alignments_dir.iterdir():
    if not protein_dir.is_dir():
        continue

    a3m_path = protein_dir / "bfd_uniclust_hits.a3m"



    if not a3m_path.exists():
        print(f"Skipping {protein_dir.name}: no a3m file found")
        continue

    # Read a3m
    with a3m_path.open() as f:
        lines = [line.strip() for line in f if line.strip()]


    #sto_path = protein_dir / "uniprot_hits.sto"
    sto_paths = ["reduced_bfd_hits.sto", "uniref90_hits.sto", "uniprot_hits.sto", "pdb_hits.sto", "mgnify_hits.sto"]
    for sto_filename in sto_paths:
        sto_path = protein_dir / sto_filename
        # Extract sequence (remove lowercase insertions if present)
        sequence = "".join(lines[1:])
        sequence = "".join(c for c in sequence if c.isupper() or c == "-")

        num_res = len(sequence)

        with sto_path.open("w") as out:
            out.write("# STOCKHOLM 1.0\n")
            out.write(f"{protein_dir.name} {sequence}\n")
            out.write(f'#=GC RF '+''.join(['x' for _ in range(num_res)])+'\n')
            out.write("//\n")

        print(f"Created {sto_path}")