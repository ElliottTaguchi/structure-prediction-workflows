export XLA_PYTHON_CLIENT_PREALLOCATE=true
export XLA_CLIENT_MEM_FRACTION=0.95

set -e

source /opt/conda/etc/profile.d/conda.sh

conda activate /home/postyr/.conda/envs/chai-lab

python predict_with_msas_batch.py
