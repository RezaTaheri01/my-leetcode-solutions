from collections import deque, defaultdict


class Solution:
    def createGraph(self, genes_set, start_gene):
        def get_neighbors(gene):
            neighbors = []
            for i in range(len(gene)):
                for c in "ACGT":  # Assuming only A, C, G, T are valid
                    if c != gene[i]:
                        mutated_gene = gene[:i] + c + gene[i+1:]
                        if mutated_gene in genes_set:
                            neighbors.append(mutated_gene)
            return neighbors

        graph = defaultdict(list)

        graph[start_gene] = get_neighbors(start_gene)
        for gene in genes_set:  # O(n)
            # O(4 * 8) per gene, total O(32n), O(n)
            graph[gene] = get_neighbors(gene)

        return graph

    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        genes_set = set(bank)  # O(n) lookup

        if startGene == endGene:
            return 0

        if endGene not in bank:
            return -1

        graph = self.createGraph(genes_set, startGene)

        # now using BFS
        queue: deque = deque([startGene])
        visited: set = set()
        degree: int = 0

        while queue:
            for _ in range(len(queue)):  # Process level-wise
                current = queue.popleft()

                if current == endGene:  # Found solution
                    return degree

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        # Mark as visited before enqueuing
                        visited.add(neighbor)
                        queue.append(neighbor)

            degree += 1  # Only increment after processing a full level

        return -1


s = Solution()

# Basic Mutation (Direct)
print(s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # ➝ 1

# No Possible Mutation
print(s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGCTA"]))  # ➝ -1

# Multiple Steps Required
print(s.minMutation("AACCGGTT", "AAACGGTA", [
      "AACCGGTA", "AACCGCTA", "AAACGGTA"]))  # ➝ 2

# Already At Destination
print(s.minMutation("AACCGGTT", "AACCGGTT", ["AACCGGTA"]))  # ➝ 0

# EndGene Not in Bank
print(s.minMutation("AACCGGTT", "CCGGTTAA", ["AACCGGTA", "AACCGCTA"]))  # ➝ -1
