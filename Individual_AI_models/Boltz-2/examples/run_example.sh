export XLA_PYTHON_CLIENT_PREALLOCATE=true
export XLA_CLIENT_MEM_FRACTION=0.95
export CUDA_VISIBLE_DEVICES=0

set -e

source /opt/conda/etc/profile.d/conda.sh

conda activate /home/alphafold/bz2_conda

boltz predict ./yaml_ind_files --out_dir ./boltz_run1/