# Project Structure and Setup

##### 1. Package managers 

To ensure enhanced reproducibility for different user preferences, we made sure to store version of tools in three files:

- [environment.yml](https://github.com/NoelOkumu/Eneza-Data-Science-Residential-training-2026/blob/eee5261b64065db7ac5bdcfe523bda9101e9570e/Group4/tools/environment.yml) file for conda users
- [Requirements.txt](https://github.com/NoelOkumu/Eneza-Data-Science-Residential-training-2026/blob/eee5261b64065db7ac5bdcfe523bda9101e9570e/Group4/tools/requirements.txt) file for venv users

_NB_: Find all the tools used in this project [here](https://github.com/NoelOkumu/Eneza-Data-Science-Residential-training-2026/tree/eee5261b64065db7ac5bdcfe523bda9101e9570e/Group4/tools)

----

##### 2. Timeline

- [x] [Day 1](https://github.com/NoelOkumu/Eneza-Data-Science-Residential-training-2026/tree/eee5261b64065db7ac5bdcfe523bda9101e9570e/Group4/Day1): Project familiarisation & dataset exploration
- [x] [Day 2](https://github.com/NoelOkumu/Eneza-Data-Science-Residential-training-2026/tree/eee5261b64065db7ac5bdcfe523bda9101e9570e/Group4/Day2): Data cleaning & preprocessing
- [x] [Day 3](https://github.com/NoelOkumu/Eneza-Data-Science-Residential-training-2026/tree/eee5261b64065db7ac5bdcfe523bda9101e9570e/Group4/Day3): Mutation data processing
- [x] [Day 4](https://github.com/NoelOkumu/Eneza-Data-Science-Residential-training-2026/tree/eee5261b64065db7ac5bdcfe523bda9101e9570e/Group4/Day4): Exploratory Data Analysis (EDA)
- [x] [Day 5](https://github.com/NoelOkumu/Eneza-Data-Science-Residential-training-2026/tree/eee5261b64065db7ac5bdcfe523bda9101e9570e/Group4/Day5): Feature selection & mutation association analysis
- [x] [Day 6]():Machine learning model development
- [x] [Day 7](): Model optimization & handling class imbalance
- [x] [Day 8](): Model evaluation
- [x] [Day 9](): Model interpretation & visualization
- [x] [Day 10](): Integration, interpretation & project documentation

----
##### 3. 

##### 4. Directory Structure

For a seamless input-output redirection, our directory structure was created as follows:  

```
.
├── DawaFit
│   ├── app.py
│   ├── environment.yml
│   ├── models
│   │   ├── best_model_3TC.pkl
│   │   ├── best_model_ABC.pkl
│   │   ├── best_model_AZT.pkl
│   │   ├── best_model_TDF.pkl
│   │   └── feature_names.pkl
│   ├── notebooks
│   │   └── mutatio_profile1.ipynb
│   ├── requirements.txt
│   ├── temp.fasta
│   ├── test.fasta
│   ├── tests
│   │   ├── test_encoder.py
│   │   ├── test_predictor.py
│   │   └── test_sierra.py
│   ├── training
│   ├── uploads
│   └── utils
│       ├── encoder.py
│       ├── predictor.py
│       ├── __pycache__
│       │   ├── encoder.cpython-312.pyc
│       │   ├── encoder.cpython-313.pyc
│       │   ├── encoder.cpython-314.pyc
│       │   ├── predictor.cpython-312.pyc
│       │   ├── predictor.cpython-313.pyc
│       │   ├── predictor.cpython-314.pyc
│       │   ├── sierra_client.cpython-312.pyc
│       │   ├── sierra_client.cpython-313.pyc
│       │   └── sierra_client.cpython-314.pyc
│       └── sierra_client.py
├── Day1
│   ├── geno-pheno_clean.tsv
│   ├── geno-pheno.dataset.tsv
│   ├── hiv_ml.yml
│   ├── missing_foldchange_barplot.pdf
│   ├── mutatio_profile1.ipynb
│   ├── output_file
│   └── README.md
├── Day2
│   ├── Cutoffs_NRTIs.pdf
│   ├── geno-pheno_clean.tsv
│   ├── genopheno_stan.tsv
│   └── README.md
├── Day3
│   ├── README.md
│   └── relevant_mutations.txt
├── Day4
│   ├── drug_dfs
│   │   ├── df_3TC.csv
│   │   ├── df_ABC.csv
│   │   ├── df_AZT.csv
│   │   ├── df_D4T.csv
│   │   ├── df_DDI.csv
│   │   ├── df_TDF.csv
│   │   └── geno-pheno_clean.tsv
│   ├── geno-pheno_clean.tsv
│   └── README.md
├── Day5
│   ├── README.md
│   └── README.md.save
├── Day9
│   └── Classification_Reports_Per_Drug.tsv
└── Pictures
    └── modeltraining_workflow.png
```
