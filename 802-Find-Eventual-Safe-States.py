class Solution(object):
    def eventualSafeNodes(self, graph):
        visited = [0] *len(graph)

        def cycle(node):
            if visited[node] == -1:
                return True
            if visited[node] == 1:
                return False
            visited[node] = -1
            for n in graph[node]:
                if cycle(n):
                    return True
            visited[node] = 1
            return False
        return [node for node in range(len(graph)) if not cycle(node)]


        