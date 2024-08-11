from collections import deque


class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Step 1: Compute in-degrees of all vertices
        in_degree = [0] * V
        for i in range(V):
            for neighbor in adj[i]:
                in_degree[neighbor] += 1

        # Initialize the queue with vertices with in-degree 0
        queue = deque([i for i in range(V) if in_degree[i] == 0])

        topo_order = []
        visited = set()  # To track nodes that have been processed
        visiting = set()  # To track nodes currently in the queue

        while queue:
            u = queue.popleft()
            topo_order.append(u)
            visited.add(u)

            # Process all neighbors
            for neighbor in adj[u]:
                if neighbor not in visited:
                    in_degree[neighbor] -= 1
                    # If in-degree becomes 0, add to queue
                    if in_degree[neighbor] == 0:
                        if neighbor not in visiting:
                            queue.append(neighbor)
                            visiting.add(neighbor)

        # Check if the topological order contains all vertices
        if len(topo_order) != V:
            raise ValueError("Graph has a cycle or is not a DAG")

        return topo_order
