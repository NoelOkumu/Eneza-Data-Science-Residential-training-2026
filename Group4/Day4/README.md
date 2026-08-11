# Generating a Feature Matrix

Data availability : [Cleaned Data](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/c50416310acc63a211d8e7408e3556877034c2fa/Day4/geno-pheno_clean.tsv)

## Tasks

- [x] Feature Selection (Filtering Mutations)

- [x] Parsing "AZT" Fold change Values

- [x] Sub-setting data for the six drugs

- [x] 3TC Training 


#### _Step 1: Feature Selection (Filtering Mutations)_

- Creating a list of mutations that meet a threshold based on the mutation frequency calculated prior (Threshold >= 1.0)
  
- Pruned low frequency mutations from the dataset

#### _Step 2: Parsing 'AZT' fold change values (Data cleaning)_

AZT fold change values were obtained of type 'str' = Object. Binarization required type <float>.

#### _Step 3: Sub setting data for the six targets_   

Data was grouped by drugs while filtering isolates that lacked Fold Change and binarizing the fold change values based on the [Phenosense scale](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/d7496c5e01d710afb7ef0273d261401db4598f3d/Day2/Cutoffs_NRTIs.pdf) obtained from Literature, we binarized targets in all subset data into new columns 'Resistance' 

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

#### _Step 4: 3TC Training Prep_

1. Create DataFrame for X(Features) and y(target)

```
### Create X data frame
X = df_3TC[["IsolateID","MutationListFiltered"]]
X.head(n = 5)

### Create y data frame
y = df_3TC["resistance"]
y.head(n = 10)

### Assess whether stratification is needed based on target y == df_3TC["resistance"]
y.value_counts()
```

3. Split data set into Train and Test set (test_size = 0.2, Random State = 42) # stratify parameter used separately but results converged
4. Inspect dimensionality of Train and Test set (Without stratification based on df_3TC["Resistance"]):
```
X_3TC_train, X_3TC_test, y_3TC_train, y_3TC_test = train_test_split (X , y, test_size = 0.2, random_state = 42)
```

   | Set | X | y1 | y0| y_total |
   |-----|----|----|----| ----- |
   | Train | 1887 | 1192 | 695 | 1887 |
   | Test | 472 | 288 | 154 | 472 |

5. Inspecting dimensionality of Train and Test set (With stratification based on df_3TC["Resistance"])
   
```
X_3TC_train, X_3TC_test, y_3TC_train, y_3TC_test = train_test_split (X, y, test_size = 0.2, random_state = 42, stratify = df_3TC["Resistance"])
```
   | Set | X | y1 | y0 | y_total |
   |------|----|---|----| ----- |
   | Train | 1187 | 1184 | 703 | 1887 |
   | Test | 472 | 296 | 176| 472 |

6. Generating 3TC_Mutation Matrix
   
 _*Note*: y_3TC_test and y_3TC_train do not need transformation because they are already binarised

```
### Generate Mutation matrix (Feature Matrix) for X_train
#Load required libraries
from sklearn.preprocessing import MultiLabelBinarizer

#Mutation matrix:
## X_Train matrix 
mlb_features = MultiLabelBinarizer(classes = relevant_mutations)
X_3TC_train_array = mlb_features.fit_transform(X_3TC_train)
X_3TC_train_array.shape

mlb_features.classes_

### Generate Mutation matrix (Feature Matrix) for X_test
## X_Test matrix
X_3TC_test_array = mlb_features.transform(X_3TC_test)
X_3TC_test_array.shape

### Generate Target Matrix for y_train
y_3TC_train_array = y_3TC_train.values
y_3TC_train_array.shape

###  Generate Target Matrix for y_test
y_3TC_test_array = y_3TC_test.values
y_3TC_test_array.shape
```

7. Saving Feature names as text
   
   import joblib
#joblib.dump(list(mlb_features.classes_), "/home/noel/Desktop/Eneza/eneza_project/HIV-drug-resistance-prediction-from-viral-sequences/DawaFit/models/feature_names.pkl")


