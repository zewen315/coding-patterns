from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def runBFS(node: Optional[Node]) -> None:
    if node is None:
        return

    visited = {node}
    q = deque([node])

    while q:
        level = [n.val for n in q]
        print(level)

        newq = deque()
        for n in q:
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    newq.append(neighbor)
        q = newq

# The key rule: mark a node visited the moment you decide to process it, 
# before you recurse into its neighbors — not after.
# Why this placement matters, and where people usually go wrong:
# 1. Adding visited too late (after the loop, or after all recursion returns)
# 2. Adding to visited at the call site instead of inside helper
#
# def helper(node: Node) -> None:
#   if node in visited:
#       return
#   visited.add(node)
#   # ... do work, then recurse
#
def runDFS(node: Optional[Node]) -> None:
    visited = set()

    def helper(node: Node) -> None:
        if node in visited:
            return
        visited.add(node)
        print(node.val)
        for neighbor in node.neighbors:
            helper(neighbor)
    
    if node is None:
        return
    helper(node)


def hasCycle(node: Optional[Node]) -> bool:
    visited = set()
    in_stack = set()

    def helper(node: Node) -> bool:
        if node in in_stack:
            return True          # back edge -> cycle found
        if node in visited:
            return False         # already fully explored, safe

        visited.add(node)
        in_stack.add(node)

        for neighbor in node.neighbors:
            if helper(neighbor):
                return True

        in_stack.remove(node)    # done exploring this branch, pop it
        return False

    if node is None:
        return False
    return helper(node)


# This is still correct, as long as you mark before recursing (which you do). 
# But it has a sharp edge: the root node never goes through the if neighbor 
# not in visited check, so you have to remember to seed visited with it 
# manually before the first call. That's exactly the line that got lost/botched
# in your previous version (visited.add(node, set())).
#
# def runDFS(node: Optional[Node]) -> None:
#     visited = set()

#     def helper(node: Node) -> None:
#         print(node.val)
#         for neighbor in node.neighbors:
#             if neighbor not in visited:
#                 visited.add(neighbor)   # marked BEFORE recursing — still correct
#                 helper(neighbor)

#     if node is None:
#         return
#     visited.add(node)   # <-- must remember to do this for the root!
#     helper(node)


def _createGraph(edges: List[List[int]]) -> Optional[Node]:
    mapping = {}

    for edge in edges:
        a, b = (edge[0], edge[1])
        if a not in mapping:
            mapping[a] = Node(val=a)
        if b not in mapping:
            mapping[b] = Node(val=b)
        mapping[a].neighbors.append(mapping[b])
        mapping[b].neighbors.append(mapping[a])
    
    return mapping[1]


if __name__ == "__main__":
    # undirected graph example
    #
    # 1 - 2
    # | \ |
    # 3 - 4 - 5
    edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 1], [4, 5]]

    print("Iteratively run bfs:")
    runBFS(_createGraph(edges))

    print("Recursively run dfs:")
    runDFS(_createGraph(edges))
