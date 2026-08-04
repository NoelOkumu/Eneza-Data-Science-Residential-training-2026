#!/usr/bin/env python3

import pickle
import pandas as pd

class MutationEncoder:

    def __init__(self, feature_file):

        with open(feature_file, "rb") as f:
            self.features = pickle.load(f)

    def transform(self, mutations):

        mutation_set = set(mutations)

        X = pd.DataFrame([{feature: int(feature in mutation_set) for feature in self.features}])

        return X#!/usr/bin/env


