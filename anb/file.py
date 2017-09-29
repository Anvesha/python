



import numpy as np
import pandas as pd
import re
import os


class GetDefaultParameters(object):
    force = 0
    workspace = "/home/anvesha/Desktop/Nextstep"

    # Phrasing parameters.
    max_phrase_levels = 3 # Maximum phrasing level
    max_phrase_length = 5 # Maximum phrase length at any level.
    cooc_threshold = 2  # Ignore co-occurrence counts below this.
    consy_threshold = 0.01 # Ignore consistencies below this.
    coherence_threshold= 0.1 # Ignore phrases with smaller coherence value.
    coherence_factor = 0.1 # tfidf ~ tf * idf * (1 + coherence_factor)

    # Similarity parameters.
    similarity_threshold = 0.01  # Ignore similarity if less than this.

    # Clustering parameters.
    num_clusters = "10,20,30" # Two levels of hierarchy.