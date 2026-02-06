export XLA_PYTHON_CLIENT_PREALLOCATE=true
export XLA_CLIENT_MEM_FRACTION=0.95

source /opt/conda/etc/profile.d/conda.sh

conda activate /home/postyr/.conda/envs/openfold-3

run_openfold predict \
    --query_json /home/postyr/openfold-3/openfold3/OF3_input/all_queries.json \
    --use_msa_server=False \
    --output_dir /home/postyr/openfold-3/openfold3/of3_run1/ \
    --runner_yaml /home/postyr/openfold-3/openfold3/inference_precomputed.yml \

