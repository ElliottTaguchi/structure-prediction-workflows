#!/bin/bash

export XLA_PYTHON_CLIENT_PREALLOCATE=true
export XLA_CLIENT_MEM_FRACTION=0.95

PYTHON_BIN="/home/postyr/.conda/envs/helixfold/bin/python3" # changes to your python
ENV_BIN="/opt/conda/etc/profile.d/conda.sh"  # change to your env
DATA_DIR="./data" # change to your data directory
input="./helixfold_input_v2" # change to your input json directory
BINARY="/home/postyr/.conda/envs/helixfold/bin" # change to your binary directory

source "$ENV_BIN"

conda activate /home/postyr/.conda/envs/helixfold

while IFS= read -r name; do
    json_path="$input/${name}.json" # Path to the input JSON files
    echo "Running inference for $json_path"

    CUDA_VISIBLE_DEVICES=0 "$PYTHON_BIN" inference.py \
        --jackhmmer_binary_path "$BINARY/jackhmmer" \
        --hhblits_binary_path "$BINARY/hhblits" \
        --hhsearch_binary_path "$BINARY/hhsearch" \
        --kalign_binary_path "$BINARY/kalign" \
        --hmmsearch_binary_path "$BINARY/hmmsearch" \
        --hmmbuild_binary_path "$BINARY/hmmbuild" \
        --nhmmer_binary_path "$BINARY/nhmmer" \
        --preset='reduced_dbs' \
        --reduced_bfd_database_path "$DATA_DIR/small_bfd/bfd-first_non_consensus_sequences.fasta" \
        --uniprot_database_path "$DATA_DIR/uniprot/uniprot.fasta" \
        --pdb_seqres_database_path "$DATA_DIR/pdb_seqres/pdb_seqres.txt" \
        --uniref90_database_path "$DATA_DIR/uniref90/uniref90.fasta" \
        --mgnify_database_path "$DATA_DIR/mgnify/mgy_clusters_2018_12.fa" \
        --template_mmcif_dir "$DATA_DIR/pdb_mmcif/mmcif_files" \
        --obsolete_pdbs_path "$DATA_DIR/pdb_mmcif/obsolete.dat" \
        --ccd_preprocessed_path "$DATA_DIR/ccd_preprocessed_etkdg.pkl.gz" \
        --rfam_database_path "$DATA_DIR/Rfam-14.9_rep_seq.fasta" \
        --max_template_date=2021-09-30 \
        --input_json "$json_path" \
        --output_dir "./helixfold_output_v2/" \
        --model_name allatom_demo \
        --init_model "${DATA_DIR}/init_models/params/HelixFold3-20250714.pdparams" \
        --infer_times 1 \
        --diff_batch_size 1 \
        --precision "fp32"

done < helixfold_binders.txt