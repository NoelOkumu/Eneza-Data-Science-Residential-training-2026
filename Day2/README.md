# Data Resolve and Cleaning

### Data Resolve
- Shape of original data (2505, 335)
- Filter columns:
    ```
    "RefID","Species","Type", "Method", "NNRTIDRMs", 'CompleteMutationListAvailable', 'Author','NonDRMs', 'Author','RefYear', 'MedlineID', 'Title',  'PtID'
    ```

- Abstract drugs
    Drugs  that do not meet a threshold of >1000 completeness were removed
  
  ```
  FTC : 557, DDC :502, TAF: 96, ISL: 32
  ```
    
### Data Cleaning Checklist

- [x] Removing Duplicate rows (Isolates_ID)
- [x] Quantifying 'Missingness' in Data
- [x] Handling missing values
- [ ] Mutation Frequency and filtering mutations
- [ ] Data transformation (If fold resistance values are skewed)

### Task Allocation:

_Lucy_: Data retrieval from Stanford HIV Database (HIVDB) and transformation to long format using R, Data Cleaning

_Irene_: Retrieval of PhenoSense Clinical assay cutoff values and Data cleaning

_Getnet_: Matrix generation workflow development


Step 1: Removing Duplicates

Added to the main .ipynb file. Isolate_IDs were unique, no duplicate values encountered

Step 2: Quantifying 'Missingness' in Data

All null values in individual columns were quantified, summed up and stored in a data frame called "Missing"


| Variable | Missing Count | Percent (%) |
| :--- | :---: | ---: |
| **NRTIDRMs** | 3072 | 20.44% |
| **foldchange** | 1354 | 9.01% |
| **IsolateID** | 0 | 0.00% |
| **IsolateName** | 0 | 0.00% |
| **drugs** | 0 | 0.00% |

Step 3 : Handling missing values

Dropped rows (Isolates) that lack the Nucleoside/ Nucleotide Reverse Transcriptase Inhibitor Drug-Resistance mutations (NRTI-DRMs)

Justification : Isolates would inflate background noise and reduce model prediction accuracy

Challenge: Fold change variable still contains missing values (Column is very sensitive to imputation) - Need to resolve

Step 4 : Retrieval of PhenoSense Clinical assay cutoff values

These values provide a threshold for determining whether the isolate was susceptible or Resistant to the drug. Values above cutoff are considered resistant while those below are deemed susceptible


_Noella_: Quantifying and Handling missing values and Data cleaning




