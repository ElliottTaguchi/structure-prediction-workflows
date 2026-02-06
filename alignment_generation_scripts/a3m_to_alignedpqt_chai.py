from pathlib import Path
from chai_lab.data.parsing.msas import a3m
from chai_lab.data.parsing.msas.aligned_pqt import (a3m_to_aligned_dataframe, expected_basename,)
from chai_lab.data.parsing.msas.data_source import MSADataSource

"""
Convert an A3M MSA file to an aligned Parquet file.
"""

a3m_path = Path("./precomputed_msa/egfr_msa_AF3_generated.a3m")

df = a3m_to_aligned_dataframe(
    a3m_path=a3m_path,
    source_database=MSADataSource.UNIREF90,
    insert_pairing_key=True,
)

out_dir = Path("./precomputed_msa_alignedpqt/")

query_seq = df.iloc[0]["sequence"]
out_path = out_dir / expected_basename(query_seq)

df.to_parquet(out_path)

print(f"wrote aligned MSA to {out_path}")

"""Convert an A3M MSA file to an aligned Parquet file."""