from pathlib import Path

"""
A short Python script made to rename all files named in the for loop below.
"""

base_dir = Path("./output_helixfold")

count = 0
for file in base_dir.rglob("bfd_uniclust_hits.a3m"):
    new_path = file.with_name("small_bfd_hits.a3m")
    file.rename(new_path)
    count += 1

print(f"renamed {count} completed.")

