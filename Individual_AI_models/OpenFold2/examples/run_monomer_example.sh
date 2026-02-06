export XLA_PYTHON_CLIENT_PREALLOCATE=true
export XLA_CLIENT_MEM_FRACTION=0.95

source /opt/conda/etc/profile.d/conda.sh

conda activate /home/postyr/.conda/envs/openfold_env

# Library paths
export LIBRARY_PATH=$CONDA_PREFIX/lib:$LIBRARY_PATH
export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH

export FASTA_DIR=./egfr_fasta_monomer/EGFR_target_contest2.fasta     # UPDATE with path to your fasta directory 
export OUTPUT_DIR=./egfr_monomer_run/      # UPDATE with path to your output directory
export MMCIF_DIR=/mnt/dsdd_share/AF3/alphafold3/public_databases/mmcif_files    # UPDATE with path to your mmcifs directory
export BASE_DATA_DIR=/mnt/dsdd_share/AF3/alphafold3/public_databases

python3 run_pretrained_openfold.py \ 
    $FASTA_DIR \
    $MMCIF_DIR \
    --output_dir $OUTPUT_DIR \
    --config_preset model_1_ptm \
    --uniref90_database_path $BASE_DATA_DIR/uniref90_2022_05.fa \
    --mgnify_database_path $BASE_DATA_DIR/mgy_clusters_2022_05.fa \
    --pdb70_database_path ./openfold/data/pdb70 \
    --uniclust30_database_path ./openfold/data/uniclust30/uniclust30_2018_08 \
    --bfd_database_path /mnt/dsdd_share/weights_databases/openfold/af2/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt.ffdata \
    --model_device "cuda:0" 
