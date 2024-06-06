import networkx as nx
import numpy as np
import random
from scipy import integrate, linalg
from typing import List
import warnings

from .functions.is_maximal_independent_set import is_maximal_independent_set
from .functions.reduced_graph import reduced_graph

def random_priority_parallel(G: nx.Graph) -> List[int]:
    """
    Find a maximal independent set using a parallel random priority algorithm.

    Args:
        G (nx.Graph): An undirected graph.

    Returns:
        List[int]: A list of nodes representing a maximal independent set.
    """
    A = nx.to_numpy_array(G)  # Adjacency matrix of the graph
    n = len(A)
    in_mis = np.zeros(n, dtype=bool)  # Nodes in the maximal independent set
    excluded = np.zeros(n, dtype=bool)  # Nodes excluded from the MIS
    
    while not np.all(excluded):
        # Step 1: Randomly assign a priority to each vertex
        priority = np.random.rand(n)
        
        # Step 2: Select vertices to be in the MIS
        candidates = np.ones(n, dtype=bool)
        for v in range(n):
            if excluded[v]:
                candidates[v] = False
                continue
            neighbors = np.where(A[v] == 1)[0]
            if any(priority[neighbors] > priority[v]):
                candidates[v] = False
        
        # Step 3: Add selected vertices to MIS and exclude them and their neighbors
        for v in range(n):
            if candidates[v]:
                in_mis[v] = True
                excluded[v] = True
                neighbors = np.where(A[v] == 1)[0]
                excluded[neighbors] = True

    return np.where(in_mis)[0].tolist()