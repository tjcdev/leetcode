from sortedcontainers import SortedSet

class Query:
    def __init__(self, type_, index):
        self.type = type_
        self.index = index

def answerQueries(queries, N):
    true_indices = SortedSet()
    results = []

    for query in queries:
        if query.type == 1:
            true_indices.add(query.index)
        elif query.type == 2:
            pos = true_indices.bisect_left(query.index)
            if pos == len(true_indices):
                results.append(-1)
            else:
                results.append(true_indices[pos])
    
    return results
