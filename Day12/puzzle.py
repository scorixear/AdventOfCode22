"""provides path joining functions annd module joining"""
import os
import sys
import time

INPUT_FILE="sample"

class node:
  connections: list["node"]
  def __init__(self,x: int,y: int,elevation: int):
    self.x = x
    self.y = y
    self.elevation = elevation
  def find_connections(self, grid: list[list["node"]]):
    # upper edge
    if self.y > 0:
      # x00
      if self.x > 0:
        if abs(grid[self.y-1][self.x-1].elevation - self.elevation) <=1:
          self.connections.append(grid[self.y-1][self.x-1])
      # 0x0
      if abs(grid[self.y-1][self.x].elevation - self.elevation) <=1:
        self.connections.append(grid[self.y-1][self.x])
      # 00x
      if self.x < len(grid[self.y-1])-1:        
        if abs(grid[self.y-1][self.x+1].elevation - self.elevation) <=1:
          self.connections.append(grid[self.y-1][self.x+1])
    # x.0
    if self.x > 0:
      if abs(grid[self.y][self.x-1].elevation - self.elevation) <=1:
        self.connections.append(grid[self.y][self.x-1])
    # 0.x
    if self.x < len(grid[self.y])-1:        
      if abs(grid[self.y][self.x+1].elevation - self.elevation) <=1:
        self.connections.append(grid[self.y][self.x+1])
    # lower edge
    if self.y < len(grid)-1:
      # x00
      if self.x > 0:
        if abs(grid[self.y+1][self.x-1].elevation - self.elevation) <=1:
          self.connections.append(grid[self.y+1][self.x-1])
      # 0x0
      if abs(grid[self.y+1][self.x].elevation - self.elevation) <=1:
        self.connections.append(grid[self.y+1][self.x])
      # 00x
      if self.x < len(grid[self.y+1])-1:
        if abs(grid[self.y+1][self.x+1].elevation - self.elevation) <=1:
          self.connections.append(grid[self.y+1][self.x+1])
      
def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  grid: list[list[node]] = [[] for _ in range(len(lines))]
  startNode = None
  endNode = None
  for y,line in enumerate(lines):
    for x,char in enumerate(line.strip()):
      newNode = node(x,y,0)
      if char == "S":
        newNode.elevation = 1
        startNode = newNode
      elif char == "E":
        newNode.elevation = 26
        endNode = newNode
      else:
        newNode.elevation = ord(char)-96
      grid[y].append(newNode)
  for rows in grid:
    for cell in rows:
      cell.find_connections(grid)
      
def dijkstra(graph, startNode, targetNode):
  distances: dict = {}
  previous: dict = {}
  Q: list[node] = []
  initialise(graph, startNode, distances, previous, Q)
  while len(Q) > 0:
    u: node = find_smallest(Q, distances)
    Q.remove(u)
    if u == targetNode:
      break
    for v in u.connections:
      if v in Q:
        distance_update(u,v,distances,previous)
  return previous

def initialise(graph, startNode, distances: dict, previous: dict, Q: list[node]):
  for y in graph:
    for x in y:
      Q.append(x)
      distances[x] = 100_000
      previous[x] = None
  distances[startNode] = 0

def distance_update(u,v,distances, previous):
  alternative = distances[u] + 1
  if alternative < distances[v]:
    distances[v] = alternative
    previous[v]= u

def find_smallest(Q, distances):
  smallestNode = Q[0]
  smallestWeight = distances[smallestNode]
  for n in Q:
    if distances[n] < smallestWeight:
      smallestWeight = distances[n]
      smallestNode = n
  return smallestNode  

if __name__ == "__main__":
  st = time.time()
  main()
  et = time.time()
  evaluationtime = (et-st)*1000
  print(f"Execution time: {evaluationtime}ms")