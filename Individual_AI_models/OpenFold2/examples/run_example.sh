export XLA_PYTHON_CLIENT_PREALLOCATE=true
export XLA_CLIENT_MEM_FRACTION=0.95

source /opt/conda/etc/profile.d/conda.sh # Update this path to your conda installation

conda activate /home/postyr/.conda/envs/openfold_env # Update this path to your conda environment

export FASTA_DIR=./input_fasta_openfold_v3      # UPDATE with path to your fasta directory 
export OUTPUT_DIR=./openfold_run2_output       # UPDATE with path to your output directory
export PRECOMPUTED_ALIGNMENT_DIR=./alignments    # UPDATE with path to your alignments directory 
export MMCIF_DIR=/mnt/dsdd_share/AF3/alphafold3/public_databases/mmcif_files    # UPDATE with path to your mmcifs directory

###-- Update the binary paths below to where you're storing them --### 

python3 run_pretrained_openfold.py $FASTA_DIR\
    $MMCIF_DIR \
    --jackhmmer_binary_path /home/postyr/.conda/envs/openfold_env/bin/jackhmmer \  
    --hhblits_binary_path /home/postyr/.conda/envs/openfold_env/bin/hhblits \
    --hmmsearch_binary_path /home/postyr/.conda/envs/openfold_env/bin/hmmsearch \
    --hmmbuild_binary_path /home/postyr/.conda/envs/openfold_env/bin/hmmbuild \
    --kalign_binary_path /home/postyr/.conda/envs/openfold_env/bin/kalign \
    --output_dir $OUTPUT_DIR \
    --use_precomputed_alignments $PRECOMPUTED_ALIGNMENT_DIR \
    --config_preset "model_1_multimer_v3" \
    --model_device "cuda:0" \
