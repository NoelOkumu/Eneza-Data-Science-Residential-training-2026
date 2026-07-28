# Data Resolve and Cleaning

### Data Resolve
- Shape of original data (2505, 335)
- Filter columns:
    ```
    "RefID","Species","Type", "Method", "NNRTIDRMs", 'CompleteMutationListAvailable', 'Author','NonDRMs', 'Author','RefYear', 'MedlineID', 'Title',  'PtID', 'IsolateName'
    ```

- Abstract drugs
    Drugs  that do not meet a threshold of >1000 completeness were removed
  
  ```
  FTC : 557, DDC :502, TAF: 96, ISL: 32
  ```
    
### Data Cleaning Checklist

- [x] Removing Duplicate rows (Isolates_ID)
- [ ] Handling missing values
- [ ] Quantifying 'Missingness' in Data
- [ ] Mutation Frequency and Mutation association studies
- [ ] Data transformation (If fold resistance values are skewed)

### Filtering Mutations 

Step 1: Mutation Association analysis and Mutation Frequency calculations
