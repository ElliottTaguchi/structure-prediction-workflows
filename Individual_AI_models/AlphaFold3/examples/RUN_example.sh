export XLA_PYTHON_CLIENT_PREALLOCATE=true
export XLA_CLIENT_MEM_FRACTION=0.95
# we exported hmmer to the path to make sure hmmerbuild and hmmsearch can be found
export PATH="/home/postyr/alphafold3/hmmer/bin:$PATH"

source /opt/conda/etc/profile.d/conda.sh  
conda activate /home/postyr/alphafold3/af3_blackwell



AF3_DIR="/home/postyr/alphafold3"
AF3_DB="/mnt/dsdd_share/AF3/alphafold3/public_databases"
AF3_MODEL="/scratch/AF3_models"
INPUT_DIR="/home/postyr/alphafold3/AF3_input_json"    # this is the input folder
OUTPUT="/home/postyr/alphafold3/AF3_run1_output" # this is the output folder
hmmer="/home/postyr/alphafold3/hmmer/bin/jackhmmer"
JAX_CACHE="cache"

JAX_TRACEBACK_FILTERING=off \
python ${AF3_DIR}/run_alphafold.py \
  --model_dir=${AF3_MODEL} \
  --db_dir=${AF3_DB} \
  --output_dir=${OUTPUT} \
  --input_dir=${INPUT_DIR} \
  --jackhmmer_binary_path=${hmmer} \
  --jax_compilation_cache_dir=${JAX_CACHE} 
