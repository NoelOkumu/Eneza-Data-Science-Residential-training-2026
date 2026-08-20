#!/usr/bin/env python3

import streamlit as st

from utils.sierra_client import SierraClient
from utils.encoder import MutationEncoder
from utils.predictor import ResistancePredictor

# Initialize objects once
sierra = SierraClient()
encoder = MutationEncoder("models/feature_names.pkl")
predictor = ResistancePredictor()

st.title("DawaFit : HIV-1 NRTI Drug Resistance Prediction Tool")

st.sidebar.markdown(
"""
### HIV Drug Resistance Prediction

Upload a HIV-1 FASTA sequence to predict resistance to NRTIs.

Supported drugs

- 3TC
- ABC
- AZT
- TDF
"""
)

uploaded_file = st.file_uploader(
    "Upload RT FASTA",
    type=["fa", "fasta", "fna"]
)

if uploaded_file:

    with open("temp.fasta", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Predict"):

        with st.spinner("Detecting mutations..."):

            mutations = sierra.detect_mutations("temp.fasta")

        st.success("Mutation detection complete!")

        st.write("Detected mutations")

        st.write(mutations)

        X = encoder.transform(mutations)

        predictions = predictor.predict(X)

        st.subheader("Predicted resistance")

        st.write(predictions)
