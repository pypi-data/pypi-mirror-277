import sys

import heapq
import math
from typing import List

from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


class AStarStrategy(PathfindingStrategy):

    allowed_directions = [Position(-1, 0), Position(0, -1), Position(0, 1), Position(1, 0)]

    @staticmethod
    def find_path(grid:List[List[Node]], start:Node, end:Node):
        """
        Performs the A* algorithm to find the shortest path from start to goal.

        Args:
        - start: The starting node.
        - goal: The goal node.

        Returns:
        - A tuple containing two elements:
            1. A list of nodes representing the path from start to goal.
            2. The total cost of the path.
        """
        # Priority queue to hold nodes to be evaluated
        g_score = {node: sys.maxsize for row in grid for node in row}
        f_score = {start: AStarStrategy.calculate_distance(start, end)}
        previous_nodes = {node: None for row in grid for node in row}
        priority_queue = [(0, start)]

        while priority_queue:
            _, current_node = heapq.heappop(priority_queue)

            if current_node == end:
                path = []
                while current_node:
                    path.insert(0, current_node)
                    current_node = previous_nodes[current_node]
                return path[1:]

            for neighbor in AStarStrategy.get_neighbors(grid, current_node):
                new_g_score = g_score[current_node] + AStarStrategy.calculate_distance(current_node, neighbor)
                if new_g_score < g_score[neighbor]:
                    previous_nodes[neighbor] = current_node
                    g_score[neighbor] = new_g_score
                    f_score[neighbor] = new_g_score + AStarStrategy.calculate_distance(neighbor, end)
                    heapq.heappush(priority_queue, (f_score[neighbor], neighbor))

        return None

    @staticmethod
    def get_neighbors(grid:List[List[Node]], node:Node) -> List[Node]:
        rows = len(grid)
        cols = len(grid[0])

        neighbors = []
        for offset in AStarStrategy.allowed_directions:
            neighbor_position = node.position - offset
            if 0 <= neighbor_position.x < rows and 0 <= neighbor_position.y < cols:
                neightbor = grid[neighbor_position.x][neighbor_position.y]
                neighbors.append(neightbor)

        return neighbors

    @staticmethod
    def calculate_distance(_:Node, node2: Node) -> float:
        # here we are assuming will only be doing orthogonal movements as defined in `allowed_directions`
        return node2.weight
