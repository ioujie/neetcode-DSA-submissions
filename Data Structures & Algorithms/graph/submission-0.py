class Graph:
    
    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self, src: int, dst: int) -> None:
        self.adjList[src].append(dst)
        self.adjList[dst]
        
    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList[src]:
            tmp = [0] * (len(self.adjList[src]) - 1)
            i = 0
            for n in self.adjList[src]:
                if n != dst:
                    tmp[i] = n
                    i += 1
            self.adjList[src] = tmp
            return True
        else:
            return False


    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()

        def dfs(src, dst):
            if dst in self.adjList[src]:
                return True
            
            for n in self.adjList[src]:
                if n in visited:
                    continue
                visited.add(n)
                if dfs(n, dst):
                    return True
                
            return False 

        return dfs(src, dst)