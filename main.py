from collections import deque
from heapq import heappush, heappop


def shortest_shortest_path(graph, source):
  """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """

  def dijkstra_helper(visited, frontier):
    if len(frontier) == 0:
      return visited
    else:
      distance, edges, node = heappop(frontier)
      if node in visited:
        if visited[node][0] < distance:
          return dijkstra_helper(visited, frontier)
        elif visited[node][0] == distance and visited[node][1] <= edges:
          return dijkstra_helper(visited, frontier)
      visited[node] = (distance, edges)
      for neighbor, weight in graph[node]:
        heappush(frontier, (distance + weight, edges + 1, neighbor))
      return dijkstra_helper(visited, frontier)

  frontier = []
  heappush(frontier, (0, 0, source))  # (distance, edges, node)
  visited = dict()
  return dijkstra_helper(visited, frontier)


def bfs_path(graph, source):
  """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
  frontier = deque([source])  # queue for BFS traversal
  visited = set([source])  # set to keep track of visited nodes
  parent = {}
  parent[
      source] = None  # dict to keep track of parents, initiated with source as key

  while frontier:
    node = frontier.popleft()
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        parent[neighbor] = node
        frontier.append(neighbor)
  return parent


def get_sample_graph():
  return {'s': {'a', 'b'}, 'a': {'b'}, 'b': {'c'}, 'c': {'a', 'd'}, 'd': {}}


def get_path(parents, destination):
  """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
  path = []
  current = parents[destination]
  while current is not None:
    path.append(current)
    current = parents[current]
  return ''.join(path[::-1])
