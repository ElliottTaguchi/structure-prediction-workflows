from pathlib import Path
import numpy as np
from chai_lab.chai1 import run_inference

# Directories
fasta_dir = Path("./input_fasta_chai_v2")
output_root = Path("./chai_run1")
msa_dir = Path("./precomputed_msa_alignedpqt")

# Loop over each FASTA files
for fasta_files in fasta_dir.glob("*.fasta"):
    output_dir = output_root / fasta_files.stem
    output_dir.mkdir(exist_ok=True)

candidates = run_inference(
    fasta_file=fasta_files,
    output_dir=output_dir,
    # 'default' setup
    num_trunk_recycles=3,
    num_diffn_timesteps=200,
    seed=42,
    device="cuda:0",
    use_esm_embeddings=True,
    # See example .aligned.pqt files in this directory
    msa_directory=msa_dir,
    # Exclusive with msa_directory; can be used for MMseqs2 server MSA generation
    use_msa_server=False,
)

cif_paths = candidates.cif_paths
scores = [rd.aggregate_score for rd in candidates.ranking_data]

# Load pTM, ipTM, pLDDTs and clash scores for sample 2
scores = np.load(output_dir.joinpath("scores.model_idx_2.npz"))
