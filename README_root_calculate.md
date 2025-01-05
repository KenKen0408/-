# README

## **Overview**

This project implements Dijkstra's algorithm to find the shortest distances from a starting node to all other nodes in a graph. The algorithm is designed to work with weighted graphs, where each edge has a cost associated with it. This implementation uses a priority queue (heap) to ensure efficient computation of the shortest paths.

---

## **How It Works**

1. **Graph Representation**:  
   - The graph is represented as a dictionary, where each key is a node, and the value is another dictionary containing neighboring nodes and their respective edge weights.

2. **Priority Queue**:  
   - A priority queue (using Python's `heapq` module) is used to store nodes based on their current shortest distance.

3. **Algorithm Steps**:  
   - Initialize distances to all nodes as infinity (`float('inf')`), except for the starting node, which is set to 0.
   - Extract the node with the smallest distance from the priority queue.
   - Update the distances to its neighboring nodes if a shorter path is found.
   - Repeat until all nodes have been processed.

4. **Output**:  
   - The algorithm returns a dictionary of the shortest distances from the start node to all other nodes.

