# Deep Learning–Based Biomolecular Complex Structure Prediction

A repository containing workflows, scripts, and setup instructions for preparing and running different deep learning–based biomolecular complex structure prediction models.

The repository is intended to provide practical and reproducible workflows for running multiple structure prediction methods using a consistent set of input preparation, sequence alignment, and file conversion steps.

## Repository Structure

.
├── Individual_AI_models/
│   ├── AlphaFold2/
│   ├── AlphaFold3/
│   ├── Boltz-2/
│   ├── Chai-1/
│   ├── HelixFold3/
│   ├── OpenFold2/
│   ├── OpenFold3/
│   ├── Protenix/
│   └── SeedFold/
│
├── alignment_generation_scripts/
│   ├── a3m_to_alignedpqt_chai.py
│   ├── a3m_to_sto_openfold.py
│   ├── fasta_to_a3m_openfold.py
│   ├── fasta_to_sto_EGFR.py
│   └── json_to_a3m.py
│
└── general_conversions/
    ├── pdb_file_reader_func.py
    ├── rename_script.py
    └── split_fasta_files.py

### Individual_AI_models/

Contains model-specific workflows for preparing and running the individual structure prediction models:

- AlphaFold2
- AlphaFold3
- Boltz-2
- Chai-1
- HelixFold3
- OpenFold2
- OpenFold3
- Protenix
- SeedFold

Each directory contains the relevant instructions, scripts, and configuration required to run the corresponding model.

### alignment_generation_scripts/

Contains scripts for generating and converting sequence alignments into formats required by different prediction models.

Examples include:

- Converting A3M files to formats used by Chai-1 and OpenFold
- Generating A3M alignments from FASTA or JSON input
- Generating Stockholm (.sto) alignments
- Preparing alignments for specific targets

### general_conversions/

Contains general-purpose utilities for handling and converting common biomolecular structure and sequence file formats.

These include scripts for:

- Reading PDB files
- Renaming structures or sequences
- Splitting multi-sequence FASTA files
