#!/usr/bin/env python3

import requests
from Bio import SeqIO


class SierraClient:

    def __init__(self):
        self.url = "http://localhost:8111/sierra/rest/graphql"

    def detect_mutations(self, fasta_file):

        record = next(SeqIO.parse(fasta_file, "fasta"))

        query = """
        query($seqs: [UnalignedSequenceInput]) {
          sequenceAnalysis(sequences: $seqs) {
            mutations {
              text
            }
          }
        }
        """

        variables = {
            "seqs": [{
                "header": record.id,
                "sequence": str(record.seq)
            }]
        }

        response = requests.post(
            self.url,
            json={
                "query": query,
                "variables": variables
            }
        )

        result = response.json()

        mutations = [
            m["text"]
            for m in result["data"]["sequenceAnalysis"][0]["mutations"]
        ]

        return mutations

