# Generating a Feature Matrix

Data availability : [Cleaned Data](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/c50416310acc63a211d8e7408e3556877034c2fa/Day4/geno-pheno_clean.tsv)

## Tasks

- [x] Parsing 'AZT' fold change values

- [x] Feature Selection (Filtering Mutations)

- [x] Sub-setting data for the six drugs

- [x] 3TC Training 


#### Step 1: Feature Selection (Filtering Mutations)

- Creating a list of mutations that meet a threshold based on the mutation frequency calculated prior (Threshold >= 1.0)
- Pruned low frequency mutations from the dataset

#### Step 2: Parsing 'AZT' fold change values (Data cleaning)

AZT fold change values were obtained of type 'str' = Object. Binarization required type <float>.

#### Step 3: Subsetting data for the six targets   

Data was subset based on drugs. We obtained 6 data frames

```
Targets --> 3TC, FTC, AZT, ABC, DDI, D4T, TDF
```
Structure of each data frame:
| Drug | Stanford HIVDB Link |
|------|----------------------|
| Lamivudine (3TC) |[df_3TC](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_3TC.csv) |
| Abacavir (ABC) | [df_ABC](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_ABC.csv) |
| Tenofovir (TDF) | [df_TDF](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_TDF.csv) |
| Zidovudine (AZT) | [df_AZT](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_AZT.csv)|
| Stavudine (D4T) | [df_D4T](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_D4T.csv) |
| Didanosine (DDI) | [df_DDI](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_DDI.csv) |

#### Step 3: Binarization of Drug Fold Change values (Target)

Using the [Phenosense scale](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day2/Cutoffs_NRTIs.pdf) obtained from Literature, we binarized targets in all subset data into new columns 'Resistance' 

Dropped Isolates with missing mutations, Retained:

| Drug_df | Isolates | 
|------|----------------------|
| Lamivudine (3TC) | 2359 |
| Abacavir (ABC) | 2231 |
| Tenofovir (TDF) | 2012 |
| Zidovudine (AZT) | 2381 |
| Stavudine (D4T) | 2377 |
| Didanosine (DDI) | 2377 |
