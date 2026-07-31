# Generating a Feature Matrix

Data availability : [Cleaned Data](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/c50416310acc63a211d8e7408e3556877034c2fa/Day4/geno-pheno_clean.tsv)

## Tasks

- [x] Feature Selection (Filtering Mutations)

- [x] Parsing "AZT" Fold change Values

- [x] Sub-setting data for the six drugs

- [x] 3TC Training 


#### Step 1: Feature Selection (Filtering Mutations)

- Creating a list of mutations that meet a threshold based on the mutation frequency calculated prior (Threshold >= 1.0)
  
- Pruned low frequency mutations from the dataset

#### Step 2: Parsing 'AZT' fold change values (Data cleaning)

AZT fold change values were obtained of type 'str' = Object. Binarization required type <float>.

#### Step 3: Sub setting data for the six targets   

Data was subset based on drugs while filtering isolates that lacked Fold Change and binarizing the fold change values based on the [Phenosense scale](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day2/Cutoffs_NRTIs.pdf) obtained from Literature, we binarized targets in all subset data into new columns 'Resistance' 

```
Resistant = 1
Susceptible = 0
```

We obtained 6 data frames :

```
Targets --> 3TC, FTC, AZT, ABC, DDI, D4T, TDF
```

Structure of each data frame:

| Drug | Stanford HIVDB Link | Isolates |
|------|----------------------|---------- |
| Lamivudine (3TC) |[df_3TC](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_3TC.csv) | 2359 |
| Abacavir (ABC) | [df_ABC](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_ABC.csv) | 2231 |
| Tenofovir (TDF) | [df_TDF](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_TDF.csv) | 2012 |
| Zidovudine (AZT) | [df_AZT](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_AZT.csv)| 2381 |
| Stavudine (D4T) | [df_D4T](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_D4T.csv) | 2377 |
| Didanosine (DDI) | [df_DDI](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day4/drug_dfs/df_DDI.csv) | 2377 |

#### Step 4: 3TC Training Prep

1. Create DataFrame for X(Features) and y(target)
2. Split data set into Train and Test set (test_size = 0.2, Random State = 42) # stratify parameter used separately but results converged
3. Inspect dimensionality of Train and Test set (Without stratification based on df_3TC["Resistance"]:
```
X_train, X_test, y_train, y_test = train_test_split (X , y, test_size = 0.2, random_state = 42)
```

   | Set | X | y |
   | Train | 1887 | 1887 |
   | Test | 472 | 472 |

5. Inspecting dimensionality of Train and Test set (test_size = 0.2, Random State = 42, stratify = df_3TC["Resistance"])

```
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.2, random_state = 42, stratify = df_3TC["Resistance"])
```
   | Set | X | y1 | y0 |
   |------|----|---|----|
   | Train | 1187 | 1184 | 703 |
   | Test | 472 | 296 | 176|
