# Mutation Frequency Calculation for Feature selection

For effective model prediction, abstracting unnecessary features to focus only on Biologically important mutations is crucial. Today's task focused on ensuring that mutations selected as features are representative of commonly observed mutations known to cause drug resistance to the six drugs in the Nucleoside/ Nucleotide Reverse Transcriptase Inhibitor subclass.

Task:
[x] Creating Mutation list column from NRTIDRMs
[x] Calculating Mutation Frequency 

# Step 1: Creating Mutation list column from NRTIDRMs
Creating a list of Unique mutations from the NRTIDRMs and their respective counts 

```
# Mutation frequency calculation
#Expanding comma-separated mutations into separate rows (Long Format)
df_mut_exploded = df_clean.explode('Mutation_List').dropna(subset=['Mutation_List'])
df_mut_exploded.head()

#Mutation Frequency Analysis
total_isolates = df_clean['IsolateID'].nunique()
global_frequencies = df_mut_exploded['Mutation_List'].value_counts().reset_index()
global_frequencies = global_frequencies[
    (global_frequencies['Mutation_List'] != "") 
]
global_frequencies.columns = ['Mutation_List', 'Absolute_Count']

global_frequencies. head(n = 30)
print(total_isolates)

#Check empty
mut_empty = (df_clean["Mutation_List"].str.len() == 0).sum()
mut_empty

#Calculate proportionality of mutations
global_frequencies['Global_Frequency_%'] = (global_frequencies['Absolute_Count'] / (total_isolates - mut_empty))* 100
global_frequencies.head(30)

## List of mutations that meet the threshold
relevant_mutations = list(retained_mutations["Mutation_List"])
relevant_mutations

# Length of relevant mutation list
print(len(relevant_mutations))
```

Outcome: 
[Relevant Mutations List](https://github.com/NoelOkumu/HIV-drug-resistance-prediction-from-viral-sequences/blob/48da5c6b428a4f05c90dfffe4ebd09fa401065dd/Day3/relevant_mutations.txt)

